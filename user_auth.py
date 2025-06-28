from users_related import load_users, save_users 

def login():
    username = input("username: ")
    password = input("password: ")
    
    if len(username) == 0 or len(password) == 0:
        print("username or password cannot be empty")
        return None
    
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login sucess")
            return user
    
    print("Invalid username or password")
    return None

def signup():
    name = input("name :")
    username = input ("username: ")
    password = input("password: ")
    
    if len(name) == 0 or len(username) == 0 or len(password) == 0:
        print("name, username or password cannot be empty")
        return None
    
    users = load_users()
    
    for user in users:
        if user["username"] == username:
            print("username is already exist!")
            return None
    
    new_user = {
        "name": name,
        "username" : username,
        "password" : password,
        "type": "user"
        }
    users.append(new_user)
    save_users(users)
    print("signup sucessfully")
