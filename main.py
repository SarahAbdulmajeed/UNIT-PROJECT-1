import inquirer
from colorama import init, Fore
from user_auth import login, signup


init(autoreset=True)  # active colors 
print("Hello, Welcome")


# ========== Main Menu =============
while True:
    login_options_list= [inquirer.List("choice",
                message="Please select an option:",
                choices=[
                    "1. Login",
                    "2. Signup",
                ])]
    user_answer1 = inquirer.prompt(login_options_list)
    user_choice1 = user_answer1["choice"][0]
    match user_choice1:
        case "1":
            login()
        case "2":
            signup()                            
        case _:
            print("Invalid option!")

# ==================================

"""def show_main_menu():
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
"""
"""print(Fore.CYAN + "🎤 Welcome to InterviewBot! 🎤")
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
            print(Fore.YELLOW + "Goodbye! Come back stronger! 👋")
            break
        case _:
            print(Fore.RED + "Invalid option!")"""