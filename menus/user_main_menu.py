import questionary 
from menus.user_jobtitles_menu import show_jobtitle_menu
from Interview.user_show_interviews import show_all_interviews
#========================================================================================
def show_main_menu(user) -> None :
    """
    This function displays the regular user main menu after login and handles user interaction
    """
    
    while True: 
        
        #Questions 
        choice = questionary.select(
            "Please select an option:",
            choices=["New Interview", "Interview History", "Exit"]
            ).ask()
        
        #Check choices 
        match choice:
            case "New Interview":
                show_jobtitle_menu(user)
            case "Interview History":
                show_all_interviews(user)
            case "Exit":
                break
#========================================================================================
