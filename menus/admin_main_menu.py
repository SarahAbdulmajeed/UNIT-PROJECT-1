import questionary 
from Interview.admin_jobtitles_list import show_jobtitle_list 
from Interview.admin_all_interviews import show_all_interviews

#========================================================================================
def show_admin_main_menu(user: dict) -> None:
    """ 
    This function displays the admin main menu to manage the program
    """
    while True: 
        
        choice = questionary.select(
            "Please select an option:",
            choices=["New Job Title", "All Interviews", "Exit"]
            ).ask()
        
        match choice:
            case "New Job Title":
                show_jobtitle_list(user)
            case "All Interviews":
                show_all_interviews()
            case "Exit":
                break
#========================================================================================