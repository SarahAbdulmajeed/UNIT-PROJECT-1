import json
import inquirer
from colorama import init, Fore


print(Fore.CYAN + "🎤 Welcome to InterviewBot! 🎤")
name = input("Please enter your name: ").strip()

# user menu here...

print(Fore.GREEN + f"\nHi {name}! Let's begin your mock interview...\n")

# interview function here ...

print(Fore.CYAN + f"Thank you {name} for completing the interview!")
