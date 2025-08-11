"""CLI interface for ai-gene-curation."""

import typer
from typing_extensions import Annotated

app = typer.Typer(help="ai-gene-curation: Agentic collaborative curation of genes")


@app.command()
def run(
    name: Annotated[str, typer.Option(help="Name of the person to greet")],
):
    """
    Run the main command.
    
    >>> # Example showing how the function formats output
    >>> name = "Alice"
    >>> expected = f"Hello, {name}!"
    >>> expected
    'Hello, Alice!'
    """
    typer.echo(f"Hello, {name}!")

def main():
    """
    Main entry point for the CLI.
    
    >>> import sys
    >>> # This would normally be called from command line
    >>> # app() would process sys.argv
    """
    app()


if __name__ == "__main__":
    main()
