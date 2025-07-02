from rich.console import Console
from rich.table import Table
from rich.panel import Panel

import json
import os
import questionary
console = Console()
INTERVIEW_FILE:str = "Interview/interviews.json"

#========================================================================================
def show_interview_content(info: dict) -> None:
    """
    Display full details of selected interview.
    """
    username:str = info["username"]
    jobtitle:str = info["jobtitle"]
    datetime_str:str = info["datetime"]

    #Load the interview data 
    with open(INTERVIEW_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    #looking for interview with the same job title and datetime
    for interview in data.get(username, []):
        if interview["jobtitle"] == jobtitle and interview["datetime"] == datetime_str:
            console.print(Panel.fit(
f"""[bold]{username} Interview
[/bold][#dfa817]{jobtitle}[/#dfa817]
[dim]{datetime_str}[/dim]""",
title="Interview Info", border_style="#327f9d"
            ))

            for i, q in enumerate(interview["questions"], 1):
                console.print(f"[bold]Q{i}:[/bold] {q['question']}")
                console.print(f"[green]Answer:[/green] {q['Answer']}")
                console.print(f"[yellow]Score:[/yellow] {q['score']}")
                console.print(f"[blue]Strengths:[/blue] {', '.join(q['strengths'])}")
                console.print(f"[red]Weaknesses:[/red] {', '.join(q['weaknesses'])}")
                console.print("-" * 45)
            return
        
    #if there is no interview with the sme job title and datetime
    console.print("[red]Interview not found.[/red]")
#========================================================================================