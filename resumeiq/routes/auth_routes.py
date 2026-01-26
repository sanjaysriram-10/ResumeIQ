from flask import Blueprint, render_template, request, redirect, session
from resumeiq.services.auth_service import create_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        success = create_user(name, email, password, role)
        if not success:
            return render_template(
                "auth/signup.html",
                error="Email already exists"
            )

        session["user_id"] = email
        session["role"] = role
        return redirect("/candidate" if role == "candidate" else "/recruiter")

    return render_template("auth/signup.html")

@auth_bp.route("/login", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        result = authenticate_user(email, password)

        if result == "NO_ACCOUNT":
            return render_template(
                "auth/login.html",
                error="Account doesn't exist, signup to create an account"
            )

        if result == "INVALID_PASSWORD":
            return render_template(
                "auth/login.html",
                error="Invalid credentials"
            )

        # ✅ Successful login
        session["user_id"] = result["email"]
        session["role"] = result["role"]

        return redirect(
            "/candidate" if result["role"] == "candidate" else "/recruiter"
        )

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
