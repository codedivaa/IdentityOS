from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table

console = Console()


def bar(value):
    filled = int(value / 10)
    return "🟨" * filled + "⬜" * (10 - filled)


def show_dashboard(identity):

    left = Table(show_header=False, box=None)

    left.add_row("🪪 Alias", identity["alias"])
    left.add_row("🧬 Archetype", identity["archetype"])
    left.add_row("🌍 Presence", f"{identity['score']}%")
    left.add_row("💬 Reputation", identity["reputation"])

    right = Table(show_header=False, box=None)

    right.add_row("⚡ Execution", bar(identity["execution"]))
    right.add_row("🎨 Creativity", bar(identity["creativity"]))
    right.add_row("📚 Learning", bar(identity["learning"]))
    right.add_row("💬 Communication", bar(identity["communication"]))

    console.print(
        Panel(
            Columns(
                [
                    left,
                    right,
                ]
            ),
            title="[bold yellow]Identity Card[/bold yellow]",
            border_style="yellow",
        )
    )

    skills = Table(title="🚀 Identity Footprint")

    skills.add_column("Technology", style="cyan")

    if identity["skills"]:
        for skill in identity["skills"]:
            skills.add_row(skill)
    else:
        skills.add_row("Nothing detected")

    console.print(skills)
    console.print()

    rec = Table(title="🚀 Next Up")

    rec.add_column("Recommendation", style="yellow")

    for item in identity["recommendations"]:
        rec.add_row(item)

    console.print(rec)