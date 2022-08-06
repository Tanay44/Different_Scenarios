#pip install rich
from rich.console import Console

console = Console()
with console.status("[bold red] Loading...") as status:
    a = input()
    b = input()
    aa = (a + b)
    print(aa)