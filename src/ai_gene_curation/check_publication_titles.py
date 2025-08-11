#!/usr/bin/env python
"""Check that publication titles in gene files match actual PubMed titles."""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set, Any
import typer
from typing_extensions import Annotated
from yaml import safe_load, safe_dump, YAMLError  # type: ignore
from Bio import Entrez  # type: ignore[import-untyped]
import time
import csv
import sys
import copy

# Set email for NCBI (required for Entrez)
Entrez.email = "ai-gene-curation@example.com"  # type: ignore

app = typer.Typer()

# Cache for fetched titles to avoid repeated API calls
title_cache: Dict[str, Optional[str]] = {}
# Statistics for cache usage
cache_stats = {"local_hits": 0, "api_fetches": 0}


def extract_pmid(reference: str) -> Optional[str]:
    """
    Extract PMID from reference string.
    
    >>> extract_pmid('PMID:12345678')
    '12345678'
    >>> extract_pmid('GO_REF:0000033')
    
    """
    if reference.startswith('PMID:'):
        return reference.replace('PMID:', '')
    return None


def fetch_pubmed_title(pmid: str, publications_dir: Optional[Path] = None) -> Optional[str]:
    """
    Fetch publication title from PubMed.
    
    First checks local cache in publications/ directory, then memory cache,
    then fetches from PubMed API if needed.
    
    Returns title string, or None if not found.
    """
    # Check memory cache first
    if pmid in title_cache:
        return title_cache[pmid]
    
    # Check local file cache in publications/ directory
    if publications_dir and publications_dir.exists():
        cache_file = publications_dir / f"PMID_{pmid}.md"
        if cache_file.exists():
            try:
                content = cache_file.read_text()
                # Parse the frontmatter to get the title
                if content.startswith('---'):
                    lines = content.split('\n')
                    for line in lines[1:]:  # Skip first ---
                        if line.startswith('---'):
                            break
                        if line.startswith('title:'):
                            title = line[6:].strip()
                            # Remove quotes if present
                            if title.startswith('"') and title.endswith('"'):
                                title = title[1:-1]
                            elif title.startswith("'") and title.endswith("'"):
                                title = title[1:-1]
                            title_cache[pmid] = title
                            cache_stats["local_hits"] += 1
                            return title
            except Exception as e:
                typer.echo(f"Error reading cached file for PMID {pmid}: {e}", err=True)
    
    # If not in local cache, fetch from PubMed API
    try:
        # Add small delay to respect NCBI rate limits
        time.sleep(0.35)
        
        # Fetch summary from PubMed
        handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
        summary_records = Entrez.read(handle)
        handle.close()
        
        if not summary_records or 'error' in summary_records[0]:
            title_cache[pmid] = None
            return None
        
        record = summary_records[0]
        title = str(record.get('Title', ''))
        
        # Clean up title - remove trailing period if present
        title = title.rstrip('.')
        
        title_cache[pmid] = title
        cache_stats["api_fetches"] += 1
        return title
        
    except Exception as e:
        typer.echo(f"Error fetching PMID {pmid}: {e}", err=True)
        title_cache[pmid] = None
        return None


def parse_markdown_with_frontmatter(content: str) -> Tuple[Dict, str]:
    """Parse markdown file with YAML frontmatter."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        yaml_content = match.group(1)
        markdown_body = match.group(2)
        try:
            frontmatter = safe_load(yaml_content)
            return frontmatter or {}, markdown_body
        except YAMLError as e:
            typer.echo(f"Error parsing YAML: {e}", err=True)
            return {}, content
    
    return {}, content


def find_evidence_in_data(data: Dict, path: str = "") -> List[Tuple[str, Dict]]:
    """
    Recursively find all Evidence objects in the data structure.
    
    Returns list of (path, evidence_dict) tuples.
    """
    evidence_list = []
    
    if isinstance(data, dict):
        # Check if this is an Evidence object (has 'reference' and optionally 'title')
        if 'reference' in data and isinstance(data['reference'], str):
            evidence_list.append((path, data))
        
        # Recurse into dict values
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            evidence_list.extend(find_evidence_in_data(value, new_path))
            
    elif isinstance(data, list):
        # Recurse into list items
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            evidence_list.extend(find_evidence_in_data(item, new_path))
    
    return evidence_list


def remove_evidence_by_paths(data: Any, paths_to_remove: List[str]) -> Any:
    """
    Remove evidence entries from data structure based on paths.
    
    Handles removal from 'support' lists specifically.
    """
    # Group paths by their parent support list
    support_removals: Dict[str, List[int]] = {}
    
    for path in paths_to_remove:
        # Parse path to find support list and index
        # e.g., "primary_functions[0].activity.support[1]"
        if '.support[' in path:
            parent_path = path.split('.support[')[0]
            index_str = path.split('.support[')[1].rstrip(']')
            try:
                index = int(index_str)
                if parent_path not in support_removals:
                    support_removals[parent_path] = []
                support_removals[parent_path].append(index)
            except ValueError:
                continue
    
    # Sort indices in reverse order for each support list
    for parent_path in support_removals:
        support_removals[parent_path].sort(reverse=True)
    
    # Remove items from support lists
    for parent_path, indices in support_removals.items():
        # Navigate to the parent object
        obj = data
        path_parts = parent_path.replace('[', '.').replace(']', '').split('.')
        
        try:
            for part in path_parts[:-1]:
                if part.isdigit():
                    obj = obj[int(part)]
                else:
                    obj = obj[part]
            
            # Get the final object containing support
            final_part = path_parts[-1]
            if final_part.isdigit():
                parent_obj = obj[int(final_part)]
            else:
                parent_obj = obj[final_part]
            
            # Remove from support list (in reverse order to maintain indices)
            if 'support' in parent_obj and isinstance(parent_obj['support'], list):
                for idx in indices:
                    if 0 <= idx < len(parent_obj['support']):
                        del parent_obj['support'][idx]
        except (KeyError, IndexError, TypeError):
            continue
    
    return data


def check_file_publications(file_path: Path, publications_dir: Optional[Path] = None, 
                           remove_mismatches: bool = False, fix_in_place: bool = False) -> Tuple[List[Dict], bool]:
    """
    Check publication titles in a single file.
    
    Returns tuple of (list of mismatches, whether file was modified).
    """
    mismatches = []
    file_modified = False
    
    # Parse file
    content = file_path.read_text()
    original_content = content
    markdown_body = ""
    
    if file_path.suffix == '.yaml':
        # Pure YAML file
        try:
            data = safe_load(content)
        except YAMLError as e:
            typer.echo(f"Error parsing {file_path}: {e}", err=True)
            return mismatches, False
    else:
        # Markdown with frontmatter
        data, markdown_body = parse_markdown_with_frontmatter(content)
    
    if not data:
        return mismatches, False
    
    # Deep copy data if we might modify it
    if remove_mismatches or fix_in_place:
        data = copy.deepcopy(data)
    
    # Find all evidence objects
    evidence_objects = find_evidence_in_data(data)
    
    # Track which support entries to remove
    paths_to_remove = []
    
    for path, evidence in evidence_objects:
        reference = evidence.get('reference', '')
        provided_title = evidence.get('title', '')
        
        # Only check PMID references
        pmid = extract_pmid(reference)
        if not pmid:
            continue
        
        # Fetch actual title from PubMed (checking local cache first)
        actual_title = fetch_pubmed_title(pmid, publications_dir)
        
        if actual_title is None:
            # Could not fetch title
            if provided_title:
                mismatches.append({
                    'file': file_path.name,
                    'path': path,
                    'reference': reference,
                    'provided_title': provided_title,
                    'actual_title': '[Could not fetch from PubMed]',
                    'status': 'FETCH_ERROR'
                })
                if remove_mismatches:
                    paths_to_remove.append(path)
        elif provided_title and provided_title != actual_title:
            # Title mismatch
            mismatches.append({
                'file': file_path.name,
                'path': path,
                'reference': reference,
                'provided_title': provided_title,
                'actual_title': actual_title,
                'status': 'MISMATCH'
            })
            if remove_mismatches:
                paths_to_remove.append(path)
            elif fix_in_place:
                # Fix the title
                evidence['title'] = actual_title
                file_modified = True
        elif not provided_title and actual_title:
            # Missing title
            mismatches.append({
                'file': file_path.name,
                'path': path,
                'reference': reference,
                'provided_title': '',
                'actual_title': actual_title,
                'status': 'MISSING'
            })
            if fix_in_place:
                # Add the missing title
                evidence['title'] = actual_title
                file_modified = True
    
    # Remove mismatched entries if requested
    if remove_mismatches and paths_to_remove:
        data = remove_evidence_by_paths(data, paths_to_remove)
        file_modified = True
    
    # Write back to file if modified
    if file_modified:
        if file_path.suffix == '.yaml':
            # Write YAML file
            with open(file_path, 'w') as f:
                safe_dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        else:
            # Write markdown with frontmatter
            yaml_str = safe_dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)
            new_content = f"---\n{yaml_str}---\n{markdown_body}"
            file_path.write_text(new_content)
    
    return mismatches, file_modified


@app.command()
def main(
    input_dir: Annotated[Path, typer.Argument(help="Directory containing gene files")],
    output: Annotated[Optional[Path], typer.Option("-o", "--output", help="Output TSV file")] = None,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Verbose output")] = False,
    publications_dir: Annotated[Optional[Path], typer.Option("-p", "--publications-dir", 
                                                            help="Directory with cached publications")] = None,
    remove_mismatches: Annotated[bool, typer.Option("--remove-mismatches", 
                                                     help="Remove support entries with mismatched titles")] = False,
    fix_in_place: Annotated[bool, typer.Option("--fix-in-place", 
                                                help="Fix missing/mismatched titles in place")] = False,
):
    """
    Check publication titles in gene curation files against PubMed.
    
    Validates that title fields in Evidence objects match the actual
    publication titles from PubMed. Uses local cache in publications/ directory
    if available to avoid repeated API calls.
    
    Options:
    --remove-mismatches: Remove all support entries with mismatched or unfetchable titles
    --fix-in-place: Update titles to match PubMed (adds missing, fixes mismatched)
    """
    
    if remove_mismatches and fix_in_place:
        typer.echo("Error: Cannot use both --remove-mismatches and --fix-in-place", err=True)
        raise typer.Exit(1)
    
    # Default to publications/ directory in current working directory
    if publications_dir is None:
        publications_dir = Path("publications")
    
    if publications_dir.exists():
        typer.echo(f"Using local publication cache from {publications_dir}")
    else:
        typer.echo(f"Local publication cache not found at {publications_dir}, will fetch from PubMed")
    
    # Find all markdown and YAML files
    files = list(input_dir.glob("*.md")) + list(input_dir.glob("*.yaml"))
    
    if not files:
        typer.echo(f"No .md or .yaml files found in {input_dir}", err=True)
        raise typer.Exit(1)
    
    typer.echo(f"Checking publication titles in {len(files)} files...")
    
    all_mismatches = []
    modified_files = []
    
    for file_path in files:
        if verbose:
            typer.echo(f"Processing {file_path.name}...")
        
        mismatches, was_modified = check_file_publications(
            file_path, publications_dir, remove_mismatches, fix_in_place
        )
        all_mismatches.extend(mismatches)
        if was_modified:
            modified_files.append(file_path.name)
    
    # Report results
    typer.echo(f"\nFound {len(all_mismatches)} publication title issues")
    
    if modified_files:
        typer.echo(f"\n✏️  Modified {len(modified_files)} files:")
        for fname in modified_files:
            typer.echo(f"  - {fname}")
    
    if all_mismatches:
        # Group by status
        missing = [m for m in all_mismatches if m['status'] == 'MISSING']
        mismatched = [m for m in all_mismatches if m['status'] == 'MISMATCH']
        errors = [m for m in all_mismatches if m['status'] == 'FETCH_ERROR']
        
        if missing:
            typer.echo(f"  - {len(missing)} missing titles")
        if mismatched:
            typer.echo(f"  - {len(mismatched)} mismatched titles")
        if errors:
            typer.echo(f"  - {len(errors)} fetch errors")
        
        # Write to file or stdout
        if output:
            with open(output, 'w', newline='') as f:
                writer = csv.DictWriter(f, 
                                       fieldnames=['file', 'path', 'reference', 
                                                  'status', 'provided_title', 'actual_title'],
                                       delimiter='\t')
                writer.writeheader()
                writer.writerows(all_mismatches)
            typer.echo(f"\nResults written to {output}")
        else:
            # Output to stdout
            writer = csv.DictWriter(sys.stdout,
                                   fieldnames=['file', 'path', 'reference',
                                              'status', 'provided_title', 'actual_title'],
                                   delimiter='\t')
            writer.writeheader()
            writer.writerows(all_mismatches)
    else:
        typer.echo("✅ All publication titles are consistent!")
    
    # Show cache statistics
    if verbose or cache_stats["local_hits"] > 0 or cache_stats["api_fetches"] > 0:
        typer.echo(f"\nCache statistics:")
        typer.echo(f"  - Local cache hits: {cache_stats['local_hits']}")
        typer.echo(f"  - PubMed API fetches: {cache_stats['api_fetches']}")
        typer.echo(f"  - Total unique PMIDs: {len(title_cache)}")


def cli():
    """Entry point for console script."""
    app()


if __name__ == "__main__":
    cli()