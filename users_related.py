import json
import os 

USERS_FILE:str = "users.json"

def default_admin():
    default_admin = [{
        "name": "admin",
        "username" : "admin",
        "password" : "admin",
        "type" : "admin"
        }]
    with open(USERS_FILE,"w",encoding="UTF-8",) as file:
        json.dump(default_admin, file, indent=2)  # python object -> json file
        

def load_users():
    if not os.path.exists(USERS_FILE):
        default_admin()
    with open('users.json', 'r', encoding="UTF-8") as file:
        return json.load(file) #Decode
        

def save_users(users:list):
    with open(USERS_FILE,"w",encoding="UTF-8",) as file:
        json.dump(users, file, indent=2)  # python object -> json file