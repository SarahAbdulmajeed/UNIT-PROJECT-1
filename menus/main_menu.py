import inquirer
from colorama import Fore

def show_main_menu(user: dict):
    print(Fore.GREEN + f"Welcome {user['name']}")

    while True:
        main_menu_list = [
            inquirer.List(
                "choice",
                message="Please select an option:",
                choices=[
                    "1. 🎤 Start New Interview",
                    "2. 📂 View Past Interviews",
                    "3. 📊 View My Skill Summary",
                    "4. ℹ️ Help & How it works",
                    "5. ❌ Exit"
                ]
            )
        ]
        main_menu_choice = inquirer.prompt(main_menu_list)["choice"][0]

        match main_menu_choice:
            case "1":
                print("Starting new interview...")
            case "2":
                print("Loading past interviews...")
            case "3":
                print("Generating skill summary...")
            case "4":
                print("Smart preparation...")
            case "5":
                print("Showing help...")
            case "6":
                print(Fore.YELLOW + "Goodbye! Come back stronger! 👋")
                break
            case _:
                print(Fore.RED + "Invalid option!")
