import json
import os 
from rich.console import Console

console:Console = Console()
users:list = []
JSON_FILE:str = "users.json"

#========================================================================================
def create_admin() -> None:
    """
    This function checks if JSON file that store users data exists.
    If the JSON file not exist, it will create new file with a default admin account 
    If the JSON file exist, the function will do nothing
    """
    if not os.path.exists(JSON_FILE):
        new_admin:dict = {
            "name" : "admin",
            "username" : "admin",
            "password" : "admin",
            "type" : "admin"
            }
        users.append(new_admin) 
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)
    else:
        return None
#========================================================================================
#========================================================================================        
def load_users() -> list[dict]:
    """
    This function will loads all the users from the JSON file 
    """
    with open(JSON_FILE, 'r', encoding="UTF-8") as file:
        return json.load(file)
#========================================================================================
#========================================================================================
def save_users(users:list[dict]) -> None:
    """
    This function will saves all the changes in the user list to the JSON file
    """
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)
#========================================================================================
#========================================================================================
def signup(name:str, username:str, password:str) -> None:
    """
    This function will register new user by adding thier name, username, and password to the users.json file
    """
    users = load_users() 
    
    found:bool = False 
    for user in users:
        
        #check if the username is already exist 
        if username == user["username"]:
            found = True
            console.print("[red]Sorry, the username already exists![/red]")
            return None
        
    # create new account
    new_user:dict = {
        "name" : name,
        "username" : username,
        "password" : password,
        "type" : "user"
        }
    # add the user information to the users list 
    users.append(new_user)
    save_users(users)
    console.print("[green]You have been successfully registered![/green]")
#========================================================================================
#========================================================================================
def login(username:str, password:str) -> dict | None :
    """This function check if the user authorized or not by checking if the usename and password match the one in the users.json file

    Returns:
        dict: the username and password for the user is correct 
        None: the username or password for the user is incorrect
    """
    for user in load_users():
        if username == user["username"] and password == user["password"]:
            console.print("[green]You have successfully logged in![/green]")
            return user
     
    console.print("[red]Incorrect username or password[/red]")
    return None
#========================================================================================