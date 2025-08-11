#!/usr/bin/env python3
"""Compare local gene curations with UniProt data."""

import argparse
import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import requests
import yaml
from tabulate import tabulate

logger = logging.getLogger(__name__)


class UniProtComparator:
    """Compare local gene curations with UniProt data."""
    
    UNIPROT_API_URL = "https://rest.uniprot.org/uniprotkb"
    
    def __init__(self, verbose: bool = False):
        """Initialize the comparator.
        
        Args:
            verbose: Whether to show detailed output
        """
        self.verbose = verbose
        logging.basicConfig(
            level=logging.DEBUG if verbose else logging.INFO,
            format='%(levelname)s: %(message)s'
        )
    
    def fetch_uniprot_data(self, uniprot_id: str) -> Optional[Dict[str, Any]]:
        """Fetch UniProt data for a given ID.
        
        Args:
            uniprot_id: UniProt accession (e.g., P42224)
            
        Returns:
            UniProt JSON data or None if fetch fails
        """
        # Clean the ID
        uniprot_id = uniprot_id.replace("UniProtKB:", "").strip()
        
        url = f"{self.UNIPROT_API_URL}/{uniprot_id}.json"
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch UniProt data for {uniprot_id}: {e}")
            return None
    
    def extract_go_terms(self, uniprot_data: Dict[str, Any], 
                        aspect: Optional[str] = None) -> Dict[str, Set[str]]:
        """Extract GO terms from UniProt data.
        
        Args:
            uniprot_data: UniProt JSON data
            aspect: Optional GO aspect filter (F, P, C)
            
        Returns:
            Dictionary mapping GO IDs to evidence codes
        """
        go_terms = defaultdict(set)
        
        for xref in uniprot_data.get("uniProtKBCrossReferences", []):
            if xref.get("database") == "GO":
                go_id = xref.get("id")
                properties = xref.get("properties", [])
                
                # Extract aspect and evidence
                term_aspect = None
                evidence_codes = []
                
                for prop in properties:
                    if prop["key"] == "GoAspect":
                        term_aspect = prop["value"]
                    elif prop["key"] == "GoEvidenceType":
                        evidence_codes.append(prop["value"].split(":")[0])
                
                # Filter by aspect if specified
                if aspect is None or term_aspect == aspect:
                    for code in evidence_codes:
                        go_terms[go_id].add(code)
        
        return dict(go_terms)
    
    def extract_disease_associations(self, uniprot_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract disease associations from UniProt data.
        
        Args:
            uniprot_data: UniProt JSON data
            
        Returns:
            List of disease associations
        """
        diseases = []
        
        for comment in uniprot_data.get("comments", []):
            if comment.get("commentType") == "DISEASE":
                disease = comment.get("disease", {})
                if disease:
                    disease_info = {
                        "name": disease.get("diseaseId", "Unknown"),
                        "id": disease.get("diseaseAccession", ""),
                        "description": disease.get("description", ""),
                        "acronym": disease.get("acronym", ""),
                    }
                    
                    # Get cross-references for MIM
                    for xref in disease.get("diseaseCrossReferences", []):
                        if xref.get("database") == "MIM":
                            disease_info["mim"] = xref.get("id")
                            break
                    
                    diseases.append(disease_info)
        
        return diseases
    
    def extract_functions(self, uniprot_data: Dict[str, Any]) -> List[str]:
        """Extract functional descriptions from UniProt data.
        
        Args:
            uniprot_data: UniProt JSON data
            
        Returns:
            List of function descriptions
        """
        functions = []
        
        for comment in uniprot_data.get("comments", []):
            if comment.get("commentType") == "FUNCTION":
                for text in comment.get("texts", []):
                    functions.append(text.get("value", ""))
        
        return functions
    
    def load_local_curation(self, file_path: Path) -> Dict[str, Any]:
        """Load local gene curation from markdown file.
        
        Args:
            file_path: Path to the gene markdown file
            
        Returns:
            Parsed YAML frontmatter
        """
        content = file_path.read_text()
        
        # Extract YAML frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                return yaml.safe_load(yaml_content)
        
        return {}
    
    def extract_local_go_terms(self, curation: Dict[str, Any]) -> Set[str]:
        """Extract GO terms from local curation.
        
        Args:
            curation: Local curation data
            
        Returns:
            Set of GO term IDs
        """
        go_terms = set()
        
        # Extract from primary_functions
        for func in curation.get("primary_functions", []):
            # Activity
            if "activity" in func:
                go_terms.add(func["activity"].get("term", {}).get("id"))
            
            # Location
            if "location" in func:
                go_terms.add(func["location"].get("term", {}).get("id"))
            
            # Complex
            if "complex" in func:
                go_terms.add(func["complex"].get("term", {}).get("id"))
            
            # Process-related terms
            for field in ["upstream", "downstream", "processes", "roles"]:
                for item in func.get(field, []):
                    if "term" in item:
                        go_terms.add(item["term"].get("id"))
                    # Handle is_any_of
                    for alt in item.get("is_any_of", []):
                        if "term" in alt:
                            go_terms.add(alt["term"].get("id"))
        
        # Remove None values
        go_terms.discard(None)
        
        return go_terms
    
    def compare_gene(self, gene_file: Path, 
                    check_go: bool = True,
                    check_functions: bool = True,
                    check_diseases: bool = True,
                    show_missing_only: bool = False) -> Dict[str, Any]:
        """Compare a single gene file with UniProt.
        
        Args:
            gene_file: Path to gene markdown file
            check_go: Whether to compare GO terms
            check_functions: Whether to compare functions
            check_diseases: Whether to compare diseases
            show_missing_only: Only show missing items
            
        Returns:
            Comparison results
        """
        # Load local curation
        local_data = self.load_local_curation(gene_file)
        if not local_data:
            logger.error(f"Failed to load {gene_file}")
            return {}
        
        # Get UniProt ID
        uniprot_id = local_data.get("id", "").replace("UniProtKB:", "")
        if not uniprot_id:
            logger.error(f"No UniProt ID found in {gene_file}")
            return {}
        
        # Fetch UniProt data
        uniprot_data = self.fetch_uniprot_data(uniprot_id)
        if not uniprot_data:
            return {}
        
        results = {
            "gene": local_data.get("symbol"),
            "uniprot_id": uniprot_id,
            "file": str(gene_file)
        }
        
        # Compare GO terms
        if check_go:
            local_go = self.extract_local_go_terms(local_data)
            uniprot_go = self.extract_go_terms(uniprot_data)
            
            results["go_comparison"] = {
                "local_count": len(local_go),
                "uniprot_count": len(uniprot_go),
                "overlap": len(local_go & set(uniprot_go.keys())),
                "local_only": local_go - set(uniprot_go.keys()),
                "uniprot_only": set(uniprot_go.keys()) - local_go
            }
        
        # Compare functions
        if check_functions:
            uniprot_functions = self.extract_functions(uniprot_data)
            results["functions"] = {
                "uniprot_descriptions": uniprot_functions
            }
        
        # Compare diseases
        if check_diseases:
            uniprot_diseases = self.extract_disease_associations(uniprot_data)
            results["diseases"] = {
                "uniprot_diseases": uniprot_diseases
            }
        
        return results
    
    def compare_directory(self, directory: Path, **kwargs) -> List[Dict[str, Any]]:
        """Compare all gene files in a directory.
        
        Args:
            directory: Directory containing gene markdown files
            **kwargs: Arguments to pass to compare_gene
            
        Returns:
            List of comparison results
        """
        results = []
        
        for gene_file in sorted(directory.glob("*.md")):
            logger.info(f"Comparing {gene_file.name}")
            result = self.compare_gene(gene_file, **kwargs)
            if result:
                results.append(result)
        
        return results
    
    def format_results(self, results: List[Dict[str, Any]], 
                      output_format: str = "table") -> str:
        """Format comparison results.
        
        Args:
            results: List of comparison results
            output_format: Output format (table, json, tsv)
            
        Returns:
            Formatted output
        """
        if output_format == "json":
            return json.dumps(results, indent=2, default=str)
        
        elif output_format == "tsv":
            rows = []
            for r in results:
                if "go_comparison" in r:
                    go = r["go_comparison"]
                    rows.append([
                        r["gene"],
                        r["uniprot_id"],
                        go["local_count"],
                        go["uniprot_count"],
                        go["overlap"],
                        len(go["local_only"]),
                        len(go["uniprot_only"])
                    ])
            
            headers = ["Gene", "UniProt", "Local GO", "UniProt GO", 
                      "Overlap", "Local Only", "UniProt Only"]
            return "\n".join(["\t".join(headers)] + 
                           ["\t".join(map(str, row)) for row in rows])
        
        else:  # table
            rows = []
            for r in results:
                if "go_comparison" in r:
                    go = r["go_comparison"]
                    rows.append([
                        r["gene"],
                        r["uniprot_id"],
                        f"{go['local_count']}",
                        f"{go['uniprot_count']}",
                        f"{go['overlap']}",
                        f"{len(go['local_only'])}",
                        f"{len(go['uniprot_only'])}"
                    ])
            
            headers = ["Gene", "UniProt", "Local GO", "UniProt GO", 
                      "Overlap", "Local Only", "UniProt Only"]
            return tabulate(rows, headers=headers, tablefmt="grid")
    
    def print_detailed_comparison(self, result: Dict[str, Any]):
        """Print detailed comparison for a single gene.
        
        Args:
            result: Comparison result for one gene
        """
        print(f"\n{'='*60}")
        print(f"Gene: {result['gene']} ({result['uniprot_id']})")
        print(f"File: {result['file']}")
        print(f"{'='*60}")
        
        if "go_comparison" in result:
            go = result["go_comparison"]
            print(f"\nGO Terms:")
            print(f"  Local: {go['local_count']} terms")
            print(f"  UniProt: {go['uniprot_count']} terms")
            print(f"  Overlap: {go['overlap']} terms")
            
            if go["local_only"]:
                print(f"\n  Terms only in local curation:")
                for term in sorted(go["local_only"]):
                    print(f"    - {term}")
            
            if self.verbose and go["uniprot_only"]:
                print(f"\n  Terms only in UniProt:")
                for term in sorted(list(go["uniprot_only"])[:10]):
                    print(f"    - {term}")
                if len(go["uniprot_only"]) > 10:
                    print(f"    ... and {len(go['uniprot_only']) - 10} more")
        
        if "functions" in result and self.verbose:
            print(f"\nUniProt Function Descriptions:")
            for func in result["functions"]["uniprot_descriptions"]:
                print(f"  - {func[:100]}...")
        
        if "diseases" in result and result["diseases"]["uniprot_diseases"]:
            print(f"\nUniProt Disease Associations:")
            for disease in result["diseases"]["uniprot_diseases"]:
                name = disease.get('name', 'Unknown')
                disease_id = disease.get('id', '')
                mim = disease.get('mim', '')
                if mim:
                    print(f"  - {name} ({disease_id}, MIM: {mim})")
                else:
                    print(f"  - {name} ({disease_id})")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Compare local gene curations with UniProt data"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input gene file or directory"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Output file (optional)"
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["table", "json", "tsv"],
        default="table",
        help="Output format (default: table)"
    )
    parser.add_argument(
        "--no-go",
        action="store_true",
        help="Skip GO term comparison"
    )
    parser.add_argument(
        "--no-functions",
        action="store_true",
        help="Skip function comparison"
    )
    parser.add_argument(
        "--no-diseases",
        action="store_true",
        help="Skip disease comparison"
    )
    parser.add_argument(
        "--missing-only",
        action="store_true",
        help="Only show missing items"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output"
    )
    parser.add_argument(
        "--detailed",
        "-d",
        action="store_true",
        help="Show detailed comparison for each gene"
    )
    
    args = parser.parse_args()
    
    # Initialize comparator
    comparator = UniProtComparator(verbose=args.verbose)
    
    # Prepare comparison arguments
    compare_kwargs = {
        "check_go": not args.no_go,
        "check_functions": not args.no_functions,
        "check_diseases": not args.no_diseases,
        "show_missing_only": args.missing_only
    }
    
    # Run comparison
    if args.input.is_file():
        results = [comparator.compare_gene(args.input, **compare_kwargs)]
    elif args.input.is_dir():
        results = comparator.compare_directory(args.input, **compare_kwargs)
    else:
        print(f"Error: {args.input} is not a file or directory")
        return 1
    
    # Filter out empty results
    results = [r for r in results if r]
    
    if not results:
        print("No results to display")
        return 0
    
    # Show detailed comparison if requested
    if args.detailed:
        for result in results:
            comparator.print_detailed_comparison(result)
    else:
        # Format and output results
        output = comparator.format_results(results, args.format)
        
        if args.output:
            args.output.write_text(output)
            print(f"Results written to {args.output}")
        else:
            print(output)
    
    # Summary statistics
    if args.format == "table" and "go_comparison" in results[0]:
        total_local = sum(r["go_comparison"]["local_count"] for r in results)
        total_uniprot = sum(r["go_comparison"]["uniprot_count"] for r in results)
        total_overlap = sum(r["go_comparison"]["overlap"] for r in results)
        
        print(f"\nSummary:")
        print(f"  Genes compared: {len(results)}")
        print(f"  Total local GO terms: {total_local}")
        print(f"  Total UniProt GO terms: {total_uniprot}")
        print(f"  Average overlap: {total_overlap/len(results):.1f} terms")
    
    return 0


if __name__ == "__main__":
    exit(main())