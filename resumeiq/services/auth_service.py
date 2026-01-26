from werkzeug.security import generate_password_hash, check_password_hash
from resumeiq.data.db import get_db

def create_user(name, email, password, role):
    db = get_db()
    cursor = db.cursor()

    password_hash = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
            (name, email, password_hash, role)
        )
        db.commit()
        return True
    except Exception as e:
        print("CREATE USER ERROR:", e)
        return False
    finally:
        db.close()

from werkzeug.security import check_password_hash
from resumeiq.data.db import get_db

def authenticate_user(email, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT email, role, password_hash FROM users WHERE email = ?",
        (email,)
    )
    user = cursor.fetchone()
    db.close()
    if not user:
        return "NO_ACCOUNT"
    if not check_password_hash(user["password_hash"], password):
        return "INVALID_PASSWORD"
    return user