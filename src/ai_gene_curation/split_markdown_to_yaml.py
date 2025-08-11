#!/usr/bin/env python
"""Utility to split markdown files with frontmatter into separate YAML files."""

from pathlib import Path
import re
import typer
from typing_extensions import Annotated
from yaml import safe_load, dump  # type: ignore


def split_markdown_to_yaml(input_dir: Path, output_dir: Path) -> None:
    """
    Split markdown files with YAML frontmatter into pure YAML files.
    
    Args:
        input_dir: Directory containing markdown files with frontmatter
        output_dir: Directory where YAML files will be written
    
    >>> import tempfile
    >>> import shutil
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     input_dir = Path(tmpdir) / "input"
    ...     output_dir = Path(tmpdir) / "output"
    ...     input_dir.mkdir()
    ...     # Create a test markdown file with frontmatter
    ...     test_file = input_dir / "test.md"
    ...     _ = test_file.write_text('''---
    ... id: test123
    ... name: Test
    ... ---
    ... 
    ... This is the markdown content.
    ... ''')
    ...     # Run the split function
    ...     split_markdown_to_yaml(input_dir, output_dir)
    ...     # Check output file exists and contains expected content
    ...     output_file = output_dir / "test.yaml"
    ...     output_file.exists()
    ...     data = safe_load(output_file.read_text())
    ...     data['id'] == 'test123'
    ...     data['description'] == 'This is the markdown content.'
    Converted test.md -> test.yaml
    True
    True
    True
    """
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all markdown files
    for md_file in input_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and markdown content
        pattern = r'^---\n(.*?)\n---\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)
        
        if match:
            frontmatter = match.group(1)
            markdown_body = match.group(2).strip()
            
            # Parse YAML frontmatter
            data = safe_load(frontmatter)
            
            # Add markdown content as 'description' field
            if markdown_body:
                data['description'] = markdown_body
            
            # Write to YAML file
            output_file = output_dir / f"{md_file.stem}.yaml"
            with open(output_file, 'w', encoding='utf-8') as f:
                dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            print(f"Converted {md_file.name} -> {output_file.name}")
        else:
            print(f"Warning: {md_file.name} doesn't have proper frontmatter format")


app = typer.Typer(help="Split markdown files with frontmatter into YAML")


@app.command(name="split")
def split_command(
    input_dir: Annotated[Path, typer.Option("--input", "-i", help="Input directory with markdown files")] = Path("genes"),
    output_dir: Annotated[Path, typer.Option("--output", "-o", help="Output directory for YAML files")] = Path("yaml"),
):
    """Split markdown files with YAML frontmatter into pure YAML files."""
    
    if not input_dir.exists():
        typer.echo(f"Error: {input_dir} directory not found", err=True)
        raise typer.Exit(1)
    
    split_markdown_to_yaml(input_dir, output_dir)
    typer.echo(f"\nCompleted: Markdown files split to {output_dir}/")


def main():
    """Main function to run the split utility."""
    app()


if __name__ == "__main__":
    main()