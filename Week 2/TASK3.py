import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("User already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login Successful")
    else:
        print("Invalid credentials")

register("john", "mypassword")      
login("john", "mypassword")       
login("john", "wrongpassword")      
register("john", "anotherpassword")  