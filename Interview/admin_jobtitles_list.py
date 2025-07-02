import os 
import json 
import questionary 
from rich.console import Console 
from Interview.admin_create_jobtitle import create_jobtitle

console:Console = Console()
JOBTITLES_FILE:str = "Interview/jobtitles.json"

#========================================================================================
def show_jobtitle_list(user:dict) -> None:
    """
    This function display all the current job titles from the jobtitle.json file
    """
    
    if os.path.exists(JOBTITLES_FILE):
        with open(JOBTITLES_FILE, "r") as file:
            data = json.load(file)
    else:
        data = [] 
         
    try:
        if len(data) == 0:
            console.print("[red]There is no job title yet...[/red]")
            
            choice = questionary.select( "Want to add new jobtitle? :", choices=["Yes", "Exit"]).ask()
            if choice == "Yes":
                create_jobtitle(user)
                
        else:

            print("All jobtitles: ")
            for jobtitle in data:
                print(jobtitle['jobtitle'])
            
            choice = questionary.select( "Want to add new jobtitle? :", choices=["Yes", "Exit"]).ask()
            if choice == "Yes":
                create_jobtitle(user)
                        
    except Exception as e:
        print(e)
#========================================================================================  