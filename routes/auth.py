from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.get_by_email(email)

        if user and check_password_hash(
            user.password_hash,
            password
        ):

            login_user(user)

            return redirect("/dashboard")

        flash("Invalid credentials")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/login")
