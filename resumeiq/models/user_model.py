from werkzeug.security import generate_password_hash, check_password_hash

# Temporary in-memory store
USERS = []

def create_user(name, email, password, role):
    user = {
        "name": name,
        "email": email,
        "password": generate_password_hash(password),
        "role": role
    }
    USERS.append(user)
    return user

def get_user_by_email(email):
    for user in USERS:
        if user["email"] == email:
            return user
    return None

def verify_user(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user["password"], password):
        return user
    return None
