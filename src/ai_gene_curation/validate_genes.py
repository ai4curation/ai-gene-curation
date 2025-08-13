#!/usr/bin/env python
"""Command-line tool for validating gene curation files using the new validation framework."""

import sys
from pathlib import Path
from typing import List, Optional
import typer
from typing_extensions import Annotated
import yaml
import csv

from ai_gene_curation.validators import (
    TermValidator,
    EvidenceValidator,
    validate_tree,
    ValidationReport
)

app = typer.Typer()


def load_oak_adapters(ontologies: List[str], verbose: bool = False):
    """Load OAK adapters for specified ontologies."""
    adapters = {}
    try:
        from oaklib import get_adapter
        
        for ont in ontologies:
            if verbose:
                typer.echo(f"Loading adapter for {ont}...")
            try:
                # Use sqlite adapters for better performance
                if ont == "GO":
                    adapter = get_adapter("sqlite:obo:go")
                elif ont == "HP":
                    adapter = get_adapter("sqlite:obo:hp")
                elif ont == "MONDO":
                    adapter = get_adapter("sqlite:obo:mondo")
                elif ont == "CL":
                    adapter = get_adapter("sqlite:obo:cl")
                elif ont == "UBERON":
                    adapter = get_adapter("sqlite:obo:uberon")
                else:
                    # Try generic OBO adapter
                    adapter = get_adapter(f"sqlite:obo:{ont.lower()}")
                adapters[ont] = adapter
            except Exception as e:
                if verbose:
                    typer.echo(f"  Warning: Could not load adapter for {ont}: {e}", err=True)
    except ImportError:
        if verbose:
            typer.echo("OAK not available, term validation will be limited", err=True)
    
    return adapters


def print_report_summary(report: ValidationReport, verbose: bool = False):
    """Print a summary of the validation report."""
    summary = report.get_summary()
    
    typer.echo("\n" + "=" * 60)
    typer.echo("VALIDATION SUMMARY")
    typer.echo("=" * 60)
    
    if report.file_path:
        typer.echo(f"File: {report.file_path}")
    
    typer.echo(f"Total checks: {summary['total_checks']}")
    typer.echo(f"✅ Success: {summary['success']}")
    
    if summary['errors'] > 0:
        typer.echo(f"❌ Errors: {summary['errors']}", err=True)
    else:
        typer.echo(f"✅ Errors: 0")
    
    if summary['warnings'] > 0:
        typer.echo(f"⚠️  Warnings: {summary['warnings']}")
    else:
        typer.echo(f"✅ Warnings: 0")
    
    if summary['repairs_made'] > 0:
        typer.echo(f"🔧 Repairs made: {summary['repairs_made']}")
    
    if summary['duration_seconds']:
        typer.echo(f"Duration: {summary['duration_seconds']:.2f} seconds")
    
    typer.echo("=" * 60)
    
    # Show details if verbose
    if verbose:
        if report.errors:
            typer.echo("\n❌ ERRORS:", err=True)
            for error in report.errors[:10]:  # Show first 10
                typer.echo(f"  [{error.path}] {error.message}", err=True)
            if len(report.errors) > 10:
                typer.echo(f"  ... and {len(report.errors) - 10} more errors", err=True)
        
        if report.warnings:
            typer.echo("\n⚠️  WARNINGS:")
            for warning in report.warnings[:10]:  # Show first 10
                typer.echo(f"  [{warning.path}] {warning.message}")
            if len(report.warnings) > 10:
                typer.echo(f"  ... and {len(report.warnings) - 10} more warnings")
        
        if report.repairs_made:
            typer.echo("\n🔧 REPAIRS:")
            for repair in report.repairs_made[:10]:  # Show first 10
                typer.echo(f"  [{repair.path}] {repair.message}")
            if len(report.repairs_made) > 10:
                typer.echo(f"  ... and {len(report.repairs_made) - 10} more repairs")


@app.command()
def validate(
    input_path: Annotated[Path, typer.Argument(help="Path to gene file or directory")],
    repair: Annotated[bool, typer.Option("--repair", "-r", help="Attempt to repair issues")] = False,
    output: Annotated[Optional[Path], typer.Option("--output", "-o", help="Output path for repaired file(s)")] = None,
    report_file: Annotated[Optional[Path], typer.Option("--report", help="Save report to TSV file")] = None,
    check_terms: Annotated[bool, typer.Option("--terms/--no-terms", help="Validate ontology terms")] = True,
    check_evidence: Annotated[bool, typer.Option("--evidence/--no-evidence", help="Validate evidence/references")] = True,
    check_titles: Annotated[bool, typer.Option("--titles/--no-titles", help="Check publication titles")] = True,
    publications_dir: Annotated[Optional[Path], typer.Option("--publications-dir", "-p", help="Publications cache directory")] = None,
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Verbose output")] = False,
):
    """
    Validate gene curation files using the new validation framework.
    
    Examples:
        # Validate a single file
        validate-genes genes/STAT1.yaml
        
        # Validate and repair all files in a directory
        validate-genes genes/ --repair --output fixed/
        
        # Generate a validation report
        validate-genes genes/ --report validation_report.tsv
    """
    
    # Setup validators
    validators = []
    
    if check_terms:
        # Load OAK adapters if available
        ontologies = ["GO", "HP", "MONDO", "CL", "UBERON"]
        oak_adapters = load_oak_adapters(ontologies, verbose)
        
        term_validator = TermValidator(
            oak_adapters=oak_adapters,
            check_labels=True,
            check_obsolete=True
        )
        validators.append(term_validator)
    
    if check_evidence:
        evidence_validator = EvidenceValidator(
            publications_dir=publications_dir or Path("publications"),
            check_titles=check_titles,
            check_evidence_codes=True,
            use_pubmed_api=False  # Don't use API by default
        )
        validators.append(evidence_validator)
    
    if not validators:
        typer.echo("No validators enabled. Use --terms and/or --evidence", err=True)
        raise typer.Exit(1)
    
    # Process files
    all_reports = []
    
    if input_path.is_file():
        files = [input_path]
    else:
        # Find all YAML and markdown files
        files = list(input_path.glob("*.yaml")) + list(input_path.glob("*.yml")) + list(input_path.glob("*.md"))
    
    if not files:
        typer.echo(f"No files found in {input_path}", err=True)
        raise typer.Exit(1)
    
    typer.echo(f"Validating {len(files)} file(s)...")
    
    for file_path in files:
        if verbose:
            typer.echo(f"\nProcessing {file_path.name}...")
        
        # Load file
        with open(file_path) as f:
            if file_path.suffix == '.md':
                # Parse markdown frontmatter
                content = f.read()
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        data = yaml.safe_load(parts[1])
                    else:
                        typer.echo(f"Skipping {file_path.name}: No frontmatter found", err=True)
                        continue
                else:
                    typer.echo(f"Skipping {file_path.name}: No frontmatter found", err=True)
                    continue
            else:
                data = yaml.safe_load(f)
        
        # Validate
        repaired_data, report = validate_tree(data, validators, repair=repair)
        report.file_path = str(file_path)
        all_reports.append(report)
        
        # Save repaired file if requested
        if repair and output:
            output_path = output
            if output.is_dir():
                output_path = output / file_path.name
                output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w') as f:
                if file_path.suffix == '.md':
                    # Write as markdown with frontmatter
                    f.write('---\n')
                    yaml.safe_dump(repaired_data, f, sort_keys=False, allow_unicode=True)
                    f.write('---\n')
                    if len(parts) >= 3:
                        f.write(parts[2])
                else:
                    yaml.safe_dump(repaired_data, f, sort_keys=False, allow_unicode=True)
            
            if verbose:
                typer.echo(f"  Saved repaired file to {output_path}")
    
    # Print summary
    total_errors = sum(len(r.errors) for r in all_reports)
    total_warnings = sum(len(r.warnings) for r in all_reports)
    total_repairs = sum(len(r.repairs_made) for r in all_reports)
    
    typer.echo("\n" + "=" * 60)
    typer.echo(f"OVERALL SUMMARY FOR {len(files)} FILES")
    typer.echo("=" * 60)
    typer.echo(f"Total errors: {total_errors}")
    typer.echo(f"Total warnings: {total_warnings}")
    if repair:
        typer.echo(f"Total repairs: {total_repairs}")
    
    # Save report if requested
    if report_file:
        rows = []
        for report in all_reports:
            for row in report.to_tsv_rows():
                row['file'] = Path(report.file_path).name if report.file_path else ""
                rows.append(row)
        
        with open(report_file, 'w', newline='') as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
                writer.writeheader()
                writer.writerows(rows)
        
        typer.echo(f"\nReport saved to {report_file}")
    
    # Show file-by-file summary if verbose
    if verbose:
        for report in all_reports:
            if report.errors or report.warnings:
                print_report_summary(report, verbose=True)
    
    # Exit with error code if there were errors
    if total_errors > 0 and not repair:
        raise typer.Exit(1)


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()