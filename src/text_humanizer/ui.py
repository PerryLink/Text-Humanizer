"""Rich UI components for displaying analysis results."""

from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class HumanityUI:
    """Display analysis results with Rich formatting."""

    def __init__(self):
        self.console = Console()

    def display(self, results: Dict, verbose: bool = False):
        """
        Display analysis results in a beautiful format.

        Args:
            results: Analysis results dictionary
            verbose: Show additional details
        """
        self._display_score_panel(results)
        self.console.print()
        self._display_metrics_table(results, verbose)

        if results["ai_words"]:
            self.console.print()
            self._display_ai_warnings(results["ai_words"])

    def _display_score_panel(self, results: Dict):
        """Display the main humanity score panel with gauge."""
        score = results["humanity_score"]
        status = results["status"]

        gauge = self._create_gauge(score)

        content = Text()
        content.append(f"Humanity Score: {score}/100\n\n", style="bold")
        content.append(gauge)
        content.append(f"\n\nStatus: {status['emoji']} {status['message']}",
                      style=f"bold {status['color']}")

        panel = Panel(
            content,
            border_style=status['color'],
            padding=(1, 2),
        )

        self.console.print(panel)

    def _create_gauge(self, score: int) -> Text:
        """
        Create a visual gauge showing the humanity score.

        Args:
            score: Humanity score from 0-100

        Returns:
            Rich Text object with colored gauge
        """
        gauge_width = 50
        position = int((score / 100) * gauge_width)

        gauge = Text()
        gauge.append("🔴", style="red")

        for i in range(gauge_width):
            if i < position:
                if score < 30:
                    gauge.append("━", style="red")
                elif score < 60:
                    gauge.append("━", style="yellow")
                else:
                    gauge.append("━", style="green")
            else:
                gauge.append("━", style="dim")

        gauge.append("🟢", style="green")
        gauge.append("\n")
        gauge.append("Robot", style="red")
        gauge.append(" " * (gauge_width - 10))
        gauge.append("Human", style="green")

        return gauge

    def _display_metrics_table(self, results: Dict, verbose: bool):
        """Display detailed metrics in a table."""
        from text_humanizer.analyzer import TextAnalyzer

        analyzer = TextAnalyzer()
        flesch_interpretation = analyzer.get_flesch_interpretation(
            results["flesch_score"]
        )

        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Metric", style="cyan", width=30)
        table.add_column("Value", style="white", width=30)

        table.add_row(
            "Flesch Reading Ease",
            f"{results['flesch_score']:.1f} ({flesch_interpretation})"
        )
        table.add_row(
            "Average Sentence Length",
            f"{results['avg_sentence_length']:.1f} words"
        )

        if verbose:
            table.add_row(
                "Total Sentences",
                str(results['total_sentences'])
            )
            table.add_row(
                "Total Words",
                str(results['total_words'])
            )

        self.console.print(table)

    def _display_ai_warnings(self, ai_words):
        """Display AI shame words warnings."""
        self.console.print("⚠️  [yellow]AI Hall of Shame detected:[/yellow]")

        for word, line_numbers in ai_words:
            lines_str = ", ".join(f"line {ln}" for ln in line_numbers[:3])
            if len(line_numbers) > 3:
                lines_str += f" (+{len(line_numbers) - 3} more)"

            self.console.print(f"  • [red]\"{word}\"[/red] ({lines_str})")
