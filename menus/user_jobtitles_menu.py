import os
import json
import questionary
from rich.console import Console 
from Interview.user_interview import start_interview

JOBTITLES_FILE:str = "Interview/jobtitles.json"
console:Console = Console()
jobtitles:list = []

#========================================================================================
def show_jobtitle_menu(user):
    """
    This function displays all the job title list for the regular user to choose from 
    """
    #if the jobtitles.json file not exist 
    if not os.path.exists(JOBTITLES_FILE):
        console.print("[red]There is no jobtitles yet..[/red]")
    else:
        #if the jobtitles.json file is exist, load it in jobtitles list variable
        with open(JOBTITLES_FILE, "r", encoding="utf-8") as file:
            jobtitles = json.load(file)
    
        #Question 
        choice = questionary.select(
            "Please select an job title:",
            choices = [item["jobtitle"] for item in jobtitles]
            ).ask()
        
        start_interview(user,choice)
#========================================================================================