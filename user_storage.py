import json
import os

USER_FILE = "user.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    
    with open(USER_FILE, "r") as file:
        return json.load(file)
    

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def register_user_data(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username:
            return False
        
    users.append({
        "username": username,
        "password": password
    })

    save_users(users)
    return True

def login_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
        
        return False

