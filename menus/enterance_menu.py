import questionary 
from rich.console import Console
from Enterance import signup,login,create_admin
from menus.user_main_menu import show_main_menu
from menus.admin_main_menu import show_admin_main_menu

console:Console = Console()

#========================================================================================
def show_menu() -> None:
    """
    This function displays the main entrance menu and handles user interaction.
    """
    
    #create users.json file if not exist with admin account 
    create_admin() 
    
    while True:
        
        #Questions 
        choice = questionary.select(
            "Please select an option:",
            choices=["Login", "Signup", "Exit"]
            ).ask()
        
        #Check choices 
        match choice:
            case "Login":
                login_username = questionary.text("username? ").ask()
                login_password = questionary.password("password? ").ask()
                user = login(login_username,login_password)
                if user:
                    if user['type'] == "user": 
                        show_main_menu(user)
                    elif user['type'] == "admin":
                        show_admin_main_menu(user)
                    else:
                        console.print("[red]Invalid user type[/red]")
            case "Signup":
                signup_name = questionary.text("name? ").ask()
                signup_username = questionary.text("username? ").ask()
                signup_password = questionary.password("password? ").ask()
                user = signup(signup_name, signup_username, signup_password)
            case "Exit":
                print("See ya!")
                break
            case _:
                print("Invalid choice!")
#========================================================================================     