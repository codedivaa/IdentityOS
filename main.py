from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.align import Align
from time import sleep
from core.shell import start_shell
from core.dashboard import show_dashboard
console = Console()

console.clear()

console.print()

console.print(
    Align.center(
        Panel.fit(
            "[bold yellow]IdentityOS[/bold yellow]\n\n"
            "[white]The Operating System For Your Digital Identity[/white]",
            border_style="yellow",
            padding=(1, 8),
        )
    )
)

sleep(1)

steps = [
    "Loading Identity Kernel",
    "Reading Digital Footprint",
    "Parsing Digital Memories",
    "Building Identity Graph",
    "Generating Identity Signals",
    "Finalizing Identity",
]

with Progress(
    TextColumn("[bold yellow]{task.description}"),
    BarColumn(bar_width=40),
    TextColumn("[green]{task.percentage:>3.0f}%"),
    console=console,
) as progress:

    for step in steps:

        task = progress.add_task(step, total=100)

        for i in range(100):
            sleep(0.01)
            progress.update(task, advance=1)

console.print()

console.print(
    Panel.fit(
        "[bold green]✓ Identity Boot Complete[/bold green]",
        border_style="green",
    )
)

console.print()

print("\nPaste your resume below.")
print("When finished, type END on a new line.\n")

lines = []

while True:

    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

text = "\n".join(lines)

from core.analyzer import analyze

identity = analyze(text)

show_dashboard(identity)
console = Console()


console.print("\n[bold yellow]Press ENTER to open IdentityOS Terminal...[/bold yellow]")
input()

start_shell(identity)