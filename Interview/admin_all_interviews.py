import json
import os
import questionary
from rich.console import Console
from Interview.admin_interview_content import show_interview_content

console:Console = Console()
INTERVIEW_FILE:str = "Interview/interviews.json"

#========================================================================================
def show_all_interviews() -> None:
    """ 
    This function displays to admin a list of all saved interviews from interviews.json file 
    """
    
    #check if the interview.json file is exist
    if not os.path.exists(INTERVIEW_FILE):
        console.print("[red]No interview records found.[/red]")
        return

    #if it exist load data from the interview.json file
    with open(INTERVIEW_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        """ 
        {
            "ahmed": [
                {"datetime": "2025-07-01 14:00", "jobtitle": "Software Engineer", "questions": [...]},
                {"datetime": "2025-06-30 16:45", "jobtitle": "Web Developer", "questions": [...]}
            ],
            "sara": [
                {"datetime": "2025-06-28 13:00", "jobtitle": "Data Analyst", "questions": [...]}
            ]
        }
        """
    
    #it will show a list of all interviews 
    interviews_history_label:list = []
    interviews_dict:dict = {}
    
    #choices for the interview history 
    for username, interviews in data.items():
        for interview in interviews:
            text= f"{username} - {interview['jobtitle']} - {interview['datetime']}"
            interviews_history_label.append(text)
            interviews_dict[text] = {
                "username": username,
                "jobtitle": interview["jobtitle"],
                "datetime": interview["datetime"]
        }

    choice = questionary.select("Select an interview: ", choices=interviews_history_label).ask()
    
    #show interview content based on the valid choice of the admin 
    if choice:
        selected_choice = interviews_dict[choice]
        show_interview_content(selected_choice)
#========================================================================================