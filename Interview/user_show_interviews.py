import json
import os
import questionary
from rich.console import Console
from Interview.admin_interview_content import show_interview_content

console:Console = Console()
INTERVIEW_FILE:str = "Interview/interviews.json"

#========================================================================================
def show_all_interviews(user:dict) -> None:
    """
    This function displays all the interview for the current regular user 
    """
    username = user["username"]
    
    if not os.path.exists(INTERVIEW_FILE):
        console.print("[red]No interview records found.[/red]")
        return

    with open(INTERVIEW_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    
    #it will show a list of all interviews 
    interviews_history_label:list = []
    interviews_dict:dict = {}
    
    for interview in data[username]:
        text= f"{interview['jobtitle']} - {interview['datetime']}"
        interviews_history_label.append(text)
        interviews_dict[text] = {
            "username": username,
            "jobtitle": interview["jobtitle"],
            "datetime": interview["datetime"]
            }

    choice = questionary.select("Select an interview: ", choices=interviews_history_label).ask()
    
    if choice:
        selected_choice = interviews_dict[choice]
        show_interview_content(selected_choice)
#========================================================================================
