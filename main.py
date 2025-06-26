import json
import inquirer
from colorama import init, Fore

init(autoreset=True)  # active colors 

def show_main_menu():
    print(Fore.GREEN + f"📋 Main Menu 📋")
    main_menu_list:list = [
        inquirer.List(
            "choice",
            message="Please select an option:",
            choices=[
                "1. 🎤 Start New Interview",
                "2. 📂 View Past Interviews",
                "3. 📊 View My Skill Summary",
                "4. 🤖 Smart Preparation",
                "5. ℹ️ Help & How it works",
                "6. ❌ Exit"
            ]
        )
    ]
    main_menu_choice = inquirer.prompt(main_menu_list)
    return main_menu_choice["choice"][0]

print(Fore.CYAN + "🎤 Welcome to InterviewBot! 🎤")
name:str = input("Please enter your name: ").strip()
while True:
    
    main_menu_choice:list = show_main_menu()
    match main_menu_choice:
        case "1":
            print("Starting new interview...")
        case "2":
            print("Loading past interviews...")
        case "3": 
            print("Generating skill summary...")
        case "4":
            print("...")
        case "5":
            print("...")
        case "6":
            print(Fore.YELLOW + "👋 Goodbye! Come back stronger!")
            break
        case _:
            print(Fore.RED + "Invalid option!")