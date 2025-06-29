import inquirer
from users.user_auth import login, signup
from menus.main_menu import show_main_menu

def show_entrance_menu():
    while True:
        login_options_list = [
            inquirer.List("choice",
                message="Please select an option:",
                choices=[
                    "1. Login",
                    "2. Signup",
                ])
        ]
        user_answer = inquirer.prompt(login_options_list)
        user_choice = user_answer["choice"][0]

        match user_choice:
            case "1":
                user_object = login()
                if user_object is not None:
                    show_main_menu(user_object)
            case "2":
                signup()
            case _:
                print("Invalid option!")
