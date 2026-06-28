from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def start_shell(identity):

    console.print()

    console.print(
        Panel.fit(
            "[bold yellow]IdentityOS Terminal[/bold yellow]\n"
            "Type [cyan]help[/cyan] to see commands.",
            border_style="yellow",
        )
    )

    while True:

        command = console.input("\n[bold green]IdentityOS > [/bold green]").strip().lower()
        if not command:
            continue

        if command == "exit":
            console.print("\n👋 Goodbye.\n")
            break

        elif command == "help":

            table = Table(title="Commands")

            table.add_column("Command", style="cyan")
            table.add_column("Description", style="yellow")

            table.add_row("profile", "View identity card")
            table.add_row("skills", "Show detected skills")
            table.add_row("signals", "View identity signals")
            table.add_row("future", "Future prediction")
            table.add_row("upgrade", "Recommended next skill")
            table.add_row("reputation", "Internet reputation")
            table.add_row("clear", "Clear screen")
            table.add_row("exit", "Quit IdentityOS")

            console.print(table)

        elif command == "profile":

            console.print(
                Panel.fit(
                    f"""
[bold]🪪 DIGITAL IDENTITY[/bold]

Alias:
[cyan]{identity['alias']}[/cyan]

Archetype:
[yellow]{identity['archetype']}[/yellow]

Presence:
[green]{identity['score']}%[/green]
""",
                    border_style="green",
                )
            )

        elif command == "skills":

            table = Table(title="Detected Skills")

            table.add_column("Skill")

            for skill in identity["skills"]:
                table.add_row(f"🚀 {skill}")

            console.print(table)

        elif command == "signals":

            console.print()

            console.print(f"⚡ Execution      {identity['execution']}%")
            console.print(f"🎨 Creativity    {identity['creativity']}%")
            console.print(f"📚 Learning      {identity['learning']}%")
            console.print(f"💬 Communication {identity['communication']}%")

        elif command == "future":

            console.print(
                Panel.fit(
                    "[bold green]Prediction[/bold green]\n\n"
                    "Likely to build an AI startup.\n\n"
                    "Confidence: 84%",
                    border_style="cyan",
                )
            )

        elif command == "upgrade":

            console.print(
                Panel.fit(
                    "[bold yellow]Recommended Upgrade[/bold yellow]\n\n"
                    "☁ Learn AWS\n"
                    "📊 Learn System Design\n"
                    "🐳 Improve Docker",
                    border_style="yellow",
                )
            )

        elif command == "reputation":

            console.print(
                Panel.fit(
                    identity["reputation"],
                    title="Internet Reputation",
                    border_style="magenta",
                )
            )

        elif command == "clear":

            console.clear()

        else:

            console.print("[red]Unknown command.[/red]")