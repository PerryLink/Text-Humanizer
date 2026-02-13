"""CLI interface for text-humanizer using Typer."""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from text_humanizer.analyzer import TextAnalyzer
from text_humanizer.cleaner import TextCleaner
from text_humanizer.ui import HumanityUI

app = typer.Typer(
    name="check-human",
    help="Stop sounding like a bot. Check your text's Humanity Score.",
    add_completion=False,
)
console = Console()


@app.command()
def main(
    file_path: Optional[str] = typer.Argument(
        None,
        help="Path to text file (.txt or .md). Use '-' to read from stdin.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show detailed analysis information.",
    ),
):
    """
    Analyze text and display its Humanity Score.

    Examples:
        check-human draft.md
        check-human article.txt
        pbpaste | check-human -
        cat file.md | check-human -
    """
    try:
        if file_path == "-" or file_path is None and not sys.stdin.isatty():
            text = sys.stdin.read()
            if not text.strip():
                console.print("[red]Error: No input provided via stdin.[/red]")
                raise typer.Exit(1)
        elif file_path:
            path = Path(file_path)
            if not path.exists():
                console.print(f"[red]Error: File '{file_path}' not found.[/red]")
                raise typer.Exit(1)

            if not path.is_file():
                console.print(f"[red]Error: '{file_path}' is not a file.[/red]")
                raise typer.Exit(1)

            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                console.print(
                    "[red]Oops, looks like binary data. Please feed me text![/red]"
                )
                raise typer.Exit(1)
        else:
            console.print("[yellow]Usage: check-human <file> or pipe text via stdin[/yellow]")
            console.print("\nExamples:")
            console.print("  check-human draft.md")
            console.print("  pbpaste | check-human -")
            raise typer.Exit(0)

        if not text.strip():
            console.print("[red]Error: File is empty.[/red]")
            raise typer.Exit(1)

        cleaner = TextCleaner()
        cleaned_text = cleaner.clean(text)

        if not cleaned_text.strip():
            console.print("[red]Error: No readable text found after cleaning.[/red]")
            raise typer.Exit(1)

        analyzer = TextAnalyzer()
        results = analyzer.analyze(cleaned_text)

        ui = HumanityUI()
        ui.display(results, verbose=verbose)

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user.[/yellow]")
        raise typer.Exit(130)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        if verbose:
            raise
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
