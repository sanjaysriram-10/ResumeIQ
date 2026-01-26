from flask import Blueprint, render_template, session, redirect
from resumeiq.data.db import get_db

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT name, email, role FROM users WHERE email = ?",
        (session["user_id"],)
    )
    user = cursor.fetchone()
    db.close()

    if not user:
        session.clear()
        return redirect("/login")

    return render_template("profile.html", user=user)
