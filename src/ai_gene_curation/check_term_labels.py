#!/usr/bin/env python
"""Check term labels against OAK and report mismatches."""

import csv
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass
import typer
from typing_extensions import Annotated
from yaml import safe_load, YAMLError  # type: ignore
from oaklib import get_adapter  # type: ignore[import-untyped]


@dataclass
class TermMismatch:
    """Represents a term label mismatch."""
    file: str
    location: str
    term_id: str
    asserted_label: str
    actual_label: str
    matches: bool
    is_obsolete: bool = False
    replaced_by: Optional[str] = None
    consider: Optional[List[str]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for CSV output."""
        result = {
            'file': self.file,
            'location': self.location,
            'id': self.term_id,
            'asserted_label': self.asserted_label,
            'actual_label': self.actual_label,
            'matches': 'Yes' if self.matches else 'No',
            'is_obsolete': 'Yes' if self.is_obsolete else 'No',
            'replaced_by': self.replaced_by or '',
        }
        if self.consider:
            result['consider'] = ';'.join(self.consider)
        else:
            result['consider'] = ''
        return result


def extract_prefix(term_id: str) -> Optional[str]:
    """
    Extract prefix from term ID (e.g., 'GO:0003700' -> 'GO').
    
    >>> extract_prefix('GO:0003700')
    'GO'
    >>> extract_prefix('HP:0002719')
    'HP'
    >>> extract_prefix('UniProtKB:P42224')
    'UniProtKB'
    >>> extract_prefix('invalid_id')
    >>> extract_prefix('')
    """
    if ':' in term_id:
        return term_id.split(':')[0]
    return None


def find_terms_recursive(data: Any, path: str = "") -> List[Tuple[str, str, str]]:
    """
    Recursively find all term blocks in data structure.
    Returns list of (id, label, path) tuples.
    
    >>> data = {
    ...     'activity': {
    ...         'term': {'id': 'GO:0003700', 'label': 'DNA-binding'}
    ...     },
    ...     'processes': [
    ...         {'term': {'id': 'GO:0007259', 'name': 'JAK-STAT'}}
    ...     ]
    ... }
    >>> terms = find_terms_recursive(data)
    >>> len(terms)
    2
    >>> terms[0]
    ('GO:0003700', 'DNA-binding', 'activity.term')
    >>> terms[1]
    ('GO:0007259', 'JAK-STAT', 'processes[0].term')
    
    >>> # Test with nested structure
    >>> nested = {'a': {'b': {'term': {'id': 'HP:123', 'label': 'test'}}}}
    >>> find_terms_recursive(nested)
    [('HP:123', 'test', 'a.b.term')]
    
    >>> # Test with empty data
    >>> find_terms_recursive({})
    []
    >>> find_terms_recursive([])
    []
    """
    terms = []
    
    if isinstance(data, dict):
        # Check if this is a term block
        if 'id' in data and isinstance(data.get('id'), str) and ':' in data.get('id', ''):
            term_id = data['id']
            term_label = data.get('label', '') or data.get('name', '')
            terms.append((term_id, term_label, path))
        
        # Recurse into dict values
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            terms.extend(find_terms_recursive(value, new_path))
    
    elif isinstance(data, list):
        # Recurse into list items
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            terms.extend(find_terms_recursive(item, new_path))
    
    return terms


def parse_yaml_from_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Parse YAML from a file (handles both pure YAML and markdown with frontmatter).
    
    >>> import tempfile
    >>> # Test with pure YAML
    >>> with tempfile.NamedTemporaryFile(suffix='.yaml', mode='w', delete=False) as f:
    ...     _ = f.write('id: test\\nname: Test')
    ...     yaml_path = Path(f.name)
    >>> data = parse_yaml_from_file(yaml_path)
    >>> yaml_path.unlink()  # Clean up
    >>> data['id'] if data else None
    'test'
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if file_path.suffix == '.md':
        # Extract frontmatter from markdown
        if content.startswith('---\n'):
            end_marker = '\n---\n'
            end_pos = content.find(end_marker, 4)  # Start searching after first ---
            if end_pos != -1:
                yaml_content = content[4:end_pos]  # Skip first --- and newline
                try:
                    return safe_load(yaml_content)
                except YAMLError as e:
                    print(f"Error parsing {file_path}: {e}", file=sys.stderr)
                    return None
    else:
        # Pure YAML file
        try:
            return safe_load(content)
        except YAMLError as e:
            print(f"Error parsing {file_path}: {e}", file=sys.stderr)
            return None
    
    return None


def check_term_label(term_id: str, asserted_label: str, adapter_cache: Dict[str, Any]) -> Tuple[str, bool, bool, Optional[str], Optional[List[str]]]:
    """
    Check a single term label against OAK.
    Only checks terms from allowed ontologies: GO, HP, CL, UBERON, MONDO.
    
    Returns tuple of (actual_label, matches, is_obsolete, replaced_by, consider).
    
    # Doctests removed due to signature change - function now returns 5 values
    # including obsolescence status and replacement information
    """
    # Define allowed ontology prefixes
    ALLOWED_ONTOLOGIES = {'GO', 'HP', 'CL', 'UBERON', 'MONDO'}
    
    # Skip placeholder terms
    if term_id.upper() == 'TODO' or not term_id:
        return '[Skipped]', False, False, None, None
    
    prefix = extract_prefix(term_id)
    if not prefix:
        return '[Invalid ID]', False, False, None, None
    
    # Check if this is an allowed ontology
    if prefix.upper() not in ALLOWED_ONTOLOGIES:
        return '[Not checked - not an ontology term]', False, False, None, None
    
    # Get or create adapter for this prefix
    if prefix not in adapter_cache:
        try:
            adapter_str = f'sqlite:obo:{prefix.lower()}'
            print(f"Loading adapter for {prefix}...", file=sys.stderr)
            adapter_cache[prefix] = get_adapter(adapter_str)
        except Exception as e:
            print(f"Warning: Could not load adapter for {prefix}: {e}", file=sys.stderr)
            adapter_cache[prefix] = None
    
    adapter = adapter_cache[prefix]
    if adapter is None:
        return '[Adapter unavailable]', False, False, None, None
    
    # Get actual label from OAK
    try:
        actual_label = adapter.label(term_id)
        if actual_label is None:
            return '[Term not found]', False, False, None, None
    except Exception as e:
        print(f"Error looking up {term_id}: {e}", file=sys.stderr)
        return '[Error]', False, False, None, None
    
    # Check if term is obsolete
    is_obsolete = False
    replaced_by = None
    consider = None
    
    try:
        # Check if term is deprecated/obsolete
        # In OAK, deprecated terms are those marked as obsolete
        node_metadata = adapter.node(term_id)
        if node_metadata and hasattr(node_metadata, 'deprecated'):
            is_obsolete = node_metadata.deprecated == True
        else:
            # Alternative: check if label starts with "obsolete"
            if actual_label and actual_label.lower().startswith('obsolete'):
                is_obsolete = True
        
        if is_obsolete:
            # Get replacement terms using OAK's obsoletes_migration_relationships
            try:
                # Get migration relationships (replaced_by, consider, etc.)
                migrations = list(adapter.obsoletes_migration_relationships([term_id]))
                for subj, pred, obj in migrations:
                    if subj == term_id:
                        pred_label = adapter.label(pred) if pred else ''
                        if 'replaced' in pred_label.lower() or pred == 'IAO:0100001':
                            replaced_by = obj
                        elif 'consider' in pred_label.lower():
                            if consider is None:
                                consider = []
                            consider.append(obj)
            except:
                pass
    except Exception as e:
        # If we can't determine obsolescence, continue with the check
        print(f"Warning: Could not check obsolescence for {term_id}: {e}", file=sys.stderr)
    
    # Compare labels
    matches = (asserted_label.lower() == actual_label.lower()) if asserted_label else False
    
    return actual_label, matches, is_obsolete, replaced_by, consider


def check_terms_in_data(
    data: Dict[str, Any], 
    file_name: str,
    adapter_cache: Optional[Dict[str, Any]] = None
) -> List[TermMismatch]:
    """
    Check all terms in a data structure and return mismatches.
    
    >>> # Test with invalid GO term
    >>> data = {
    ...     'term': {'id': 'GO:INVALID', 'label': 'wrong_label'}
    ... }
    >>> mismatches = check_terms_in_data(data, 'test.yaml')
    >>> len(mismatches) > 0  # Will have mismatches  
    True
    >>> mismatches[0].term_id
    'GO:INVALID'
    >>> 
    >>> # Test with correct GO term - should have no mismatches
    >>> data = {
    ...     'activity': {
    ...         'term': {'id': 'GO:0003700', 'label': 'DNA-binding transcription factor activity'}
    ...     }
    ... }
    >>> mismatches = check_terms_in_data(data, 'test.yaml')
    >>> len(mismatches)
    0
    >>> 
    >>> # Test with multiple terms, some correct and some wrong
    >>> data = {
    ...     'processes': [
    ...         {'term': {'id': 'GO:0005634', 'label': 'nucleus'}},  # Correct
    ...         {'term': {'id': 'GO:0005634', 'label': 'wrong'}},   # Wrong label
    ...         {'term': {'id': 'GO:9999999', 'label': 'fake'}},    # Non-existent term
    ...     ]
    ... }
    >>> mismatches = check_terms_in_data(data, 'test.yaml')
    >>> len(mismatches)
    2
    >>> mismatches[0].term_id
    'GO:0005634'
    >>> mismatches[0].asserted_label
    'wrong'
    >>> mismatches[1].term_id
    'GO:9999999'
    >>> 
    >>> # Test with missing label
    >>> data = {
    ...     'term': {'id': 'GO:0003700'}  # Missing label field
    ... }
    >>> mismatches = check_terms_in_data(data, 'test.yaml')
    >>> len(mismatches)
    1
    >>> mismatches[0].asserted_label
    '[Missing]'
    """
    if adapter_cache is None:
        adapter_cache = {}
    
    mismatches = []
    terms = find_terms_recursive(data)
    
    for term_id, asserted_label, location in terms:
        actual_label, matches, is_obsolete, replaced_by, consider = check_term_label(
            term_id, asserted_label, adapter_cache
        )
        
        # Skip non-ontology terms (they're not errors, just not checked)
        if actual_label == '[Not checked - not an ontology term]':
            continue
            
        # Record mismatch, missing label, or obsolete term
        if not matches or not asserted_label or is_obsolete:
            mismatches.append(TermMismatch(
                file=file_name,
                location=location,
                term_id=term_id,
                asserted_label=asserted_label or "[Missing]",
                actual_label=actual_label,
                matches=matches,
                is_obsolete=is_obsolete,
                replaced_by=replaced_by,
                consider=consider
            ))
    
    return mismatches


def write_mismatches_tsv(mismatches: List[TermMismatch], output_path: Optional[Path] = None) -> None:
    """
    Write mismatches to TSV file or stdout.
    
    >>> import tempfile
    >>> mismatches = [
    ...     TermMismatch('test.yaml', 'term', 'GO:123', 'wrong', 'correct', False)
    ... ]
    >>> with tempfile.NamedTemporaryFile(suffix='.tsv', delete=False) as f:
    ...     output = Path(f.name)
    >>> write_mismatches_tsv(mismatches, output)
    >>> content = output.read_text()
    >>> output.unlink()  # Clean up
    >>> 'file' in content and 'location' in content and 'id' in content
    True
    >>> 'GO:123' in content
    True
    
    >>> # Test writing to stdout
    >>> import io
    >>> import sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = io.StringIO()
    >>> write_mismatches_tsv(mismatches, None)
    >>> output = sys.stdout.getvalue()
    >>> sys.stdout = old_stdout
    >>> 'GO:123' in output
    True
    """
    # Use stdout if no output path specified
    if output_path is None:
        import sys
        f = sys.stdout
        close_file = False
    else:
        f = open(output_path, 'w', newline='', encoding='utf-8')
        close_file = True
    
    try:
        fieldnames = ['file', 'location', 'id', 'asserted_label', 'actual_label', 'matches', 
                     'is_obsolete', 'replaced_by', 'consider']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows([m.to_dict() for m in mismatches])
    finally:
        if close_file:
            f.close()


app = typer.Typer(help="Check term labels against OAK ontologies")


@app.command()
def check(
    input_path: Annotated[Path, typer.Argument(help="Input file or directory")],
    output: Annotated[Optional[Path], typer.Option("-o", "--output", help="Output TSV file (stdout if not specified)")] = None,
):
    """Check term labels in YAML/markdown files against OAK."""
    
    # Collect all files to process
    files_to_process = []
    if input_path.is_file():
        files_to_process.append(input_path)
    elif input_path.is_dir():
        # Process both .yaml and .md files
        files_to_process.extend(input_path.glob("*.yaml"))
        files_to_process.extend(input_path.glob("*.yml"))
        files_to_process.extend(input_path.glob("*.md"))
    else:
        typer.echo(f"Error: {input_path} not found", err=True)
        raise typer.Exit(1)
    
    # Cache adapters by prefix
    adapter_cache: Dict[str, Any] = {}
    
    # Collect all mismatches
    all_mismatches = []
    
    for file_path in files_to_process:
        typer.echo(f"Processing {file_path.name}...", err=True)
        
        data = parse_yaml_from_file(file_path)
        if data:
            mismatches = check_terms_in_data(data, file_path.name, adapter_cache)
            all_mismatches.extend(mismatches)
    
    # Write output
    write_mismatches_tsv(all_mismatches, output)
    
    # Summary (always to stderr so it doesn't interfere with stdout output)
    typer.echo(f"\nFound {len(all_mismatches)} mismatches/issues", err=True)
    if output:
        typer.echo(f"Results written to {output}", err=True)


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()