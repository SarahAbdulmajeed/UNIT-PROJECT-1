import json 
import os
import questionary 
from rich.console import Console 

console:Console = Console()
jobtitles:list  = []
JOBTITLES_FILE:str = "Interview/jobtitles.json"

#========================================================================================
def create_jobtitle(user:dict) -> None:
    """
    This function allow the admin to enter a new job title and save it to the jobtitles.json file
    """
    
    new_jobtitle = questionary.text("new jobtitle? ").ask().strip()

    #check if the new job title is empty     
    if not new_jobtitle:
        console.print("[red]Job title cannot be empty[/red]")
        return 

    
    # check if the file is there i will read the content of it 
    if os.path.exists(JOBTITLES_FILE):
        with open(JOBTITLES_FILE, "r") as file:
            data = json.load(file)
    else:
        # if file not there, start with empty array 
        data:list = [] 
        
    # check if job title already exists
    if any(job.get("jobtitle", "").lower() == new_jobtitle.lower() for job in data):
        console.print(f"[yellow]Job title '{new_jobtitle}' already exists.[/yellow]")
        return

    data.append({"jobtitle": new_jobtitle})
    
    # create new file with the previous data array 
    with open(JOBTITLES_FILE, "w") as file:
        json.dump(data, file, indent=4)
    
    console.print(f"[green]Job title '{new_jobtitle}' has been added successfully.[/green]")
#========================================================================================