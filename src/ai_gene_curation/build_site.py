#!/usr/bin/env python3
"""Build static site from gene markdown files."""

import re
from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml import safe_load, YAMLError  # type: ignore


def parse_markdown_with_frontmatter(content: str) -> tuple[Dict[str, Any], str]:
    """Parse markdown file with YAML frontmatter.
    
    Args:
        content: Raw markdown content
        
    Returns:
        Tuple of (frontmatter dict, markdown body)
    """
    # Match YAML frontmatter between --- delimiters
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        yaml_content = match.group(1)
        markdown_body = match.group(2)
        try:
            frontmatter = safe_load(yaml_content)
            return frontmatter or {}, markdown_body
        except YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return {}, content
    
    return {}, content


def render_ontology_term(term: Dict[str, Any]) -> str:
    """Render an ontology term as HTML using bioregistry."""
    if not term:
        return ""
    
    term_id = term.get('id', '')
    label = term.get('label') or term.get('name', '')
    
    if term_id and label:
        return f'<a href="https://bioregistry.io/{term_id}" target="_blank">{label}</a> ({term_id})'
    elif term_id:
        return f'<a href="https://bioregistry.io/{term_id}" target="_blank">{term_id}</a>'
    elif label:
        return label
    return str(term)


def render_evidence(evidence_list: list) -> str:
    """Render evidence list as HTML using bioregistry."""
    if not evidence_list:
        return ""
    
    items = []
    for evidence in evidence_list:
        ref = evidence.get('reference', '')
        ev_type = evidence.get('evidence_type', '')
        title = evidence.get('title', '')
        supporting_text = evidence.get('supporting_text', '')
        
        # Create link using bioregistry for PMIDs and other references
        if ref.startswith('PMID:') or ref.startswith('PMC:'):
            ref_html = f'<a href="https://bioregistry.io/{ref}" target="_blank">{ref}</a>'
        elif ':' in ref:  # Other CURIEs
            ref_html = f'<a href="https://bioregistry.io/{ref}" target="_blank">{ref}</a>'
        else:
            ref_html = f'<code>{ref}</code>'
        
        # Build the evidence string
        evidence_str = f"{ref_html} ({ev_type})"
        if title:
            evidence_str = f'{ref_html} ({ev_type}) - <em>"{title}"</em>'
        
        items.append(evidence_str)
    
    return ", ".join(items)


def process_gene_file(
    input_path: Path,
    output_path: Path,
    template_env: Environment
) -> None:
    """Process a single gene markdown file.
    
    Args:
        input_path: Path to input markdown file
        output_path: Path to output markdown file
        template_env: Jinja2 environment
    """
    # Read input file
    content = input_path.read_text()
    frontmatter, markdown_body = parse_markdown_with_frontmatter(content)
    
    # Get template
    template = template_env.get_template('gene_page.j2')
    
    # Add helper functions to context
    context = {
        'gene': frontmatter,
        'markdown_body': markdown_body,
        'render_term': render_ontology_term,
        'render_evidence': render_evidence,
    }
    
    # Render template
    rendered = template.render(**context)
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered)
    print(f"Processed {input_path.name} → {output_path}")


def build_site(
    genes_dir: Path = Path("genes"),
    output_dir: Path = Path("docs/genes"),
    templates_dir: Path = Path("templates")
) -> None:
    """Build static site from gene markdown files.
    
    Args:
        genes_dir: Directory containing gene markdown files
        output_dir: Output directory for processed files
        templates_dir: Directory containing Jinja2 templates
    """
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Process each gene file
    gene_files = list(genes_dir.glob("*.md"))
    
    if not gene_files:
        print(f"No markdown files found in {genes_dir}")
        return
    
    print(f"Processing {len(gene_files)} gene files...")
    
    for gene_file in gene_files:
        output_file = output_dir / gene_file.name
        process_gene_file(gene_file, output_file, env)
    
    # Create index file
    create_gene_index(gene_files, genes_dir, output_dir, env)
    
    print(f"\n✅ Built site with {len(gene_files)} gene pages")


def create_gene_index(
    gene_files: list[Path],
    genes_dir: Path,
    output_dir: Path,
    template_env: Environment
) -> None:
    """Create an index page listing all genes.
    
    Args:
        gene_files: List of gene markdown files
        genes_dir: Directory containing gene files
        output_dir: Output directory
        template_env: Jinja2 environment
    """
    genes_data = []
    
    for gene_file in gene_files:
        content = gene_file.read_text()
        frontmatter, _ = parse_markdown_with_frontmatter(content)
        
        if frontmatter:
            genes_data.append({
                'filename': gene_file.name,
                'symbol': frontmatter.get('symbol', 'Unknown'),
                'id': frontmatter.get('id', ''),
                'functions_count': len(frontmatter.get('primary_functions', [])),
                'phenotypes_count': len(frontmatter.get('phenotypes', [])),
            })
    
    # Sort by symbol
    genes_data.sort(key=lambda x: x['symbol'])
    
    # Render index template
    template = template_env.get_template('gene_index.j2')
    rendered = template.render(genes=genes_data)
    
    # Write index file
    index_path = output_dir / "index.md"
    index_path.write_text(rendered)
    print(f"Created gene index at {index_path}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build static site from gene markdown files")
    parser.add_argument(
        "--genes-dir",
        type=Path,
        default=Path("genes"),
        help="Directory containing gene markdown files"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("docs/genes"),
        help="Output directory for processed files"
    )
    parser.add_argument(
        "--templates-dir",
        type=Path,
        default=Path("templates"),
        help="Directory containing Jinja2 templates"
    )
    
    args = parser.parse_args()
    
    build_site(args.genes_dir, args.output_dir, args.templates_dir)


if __name__ == "__main__":
    main()