users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(user):
    users.append(user)

def get_user(user_id):
    return next((u for u in users if u["id"] == user_id), None)

def update_user(user_id, name=None, email=None):
    user = get_user(user_id)
    if user:
        if name: user["name"] = name
        if email: user["email"] = email

def delete_user(user_id):
    users[:] = [u for u in users if u["id"] != user_id]


add_user({"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print(get_user(2))
update_user(1, name="Alicia")
delete_user(2)
print(users)
