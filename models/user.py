from flask_login import UserMixin
from database import get_db

class User(UserMixin):

    def __init__(self, user_data):
        self.id = user_data["id"]
        self.name = user_data["name"]
        self.email = user_data["email"]
        self.password_hash = user_data["password_hash"]
        self.role = user_data["role"]

    @staticmethod
    def get_by_id(user_id):
        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE id=?",
            (user_id,)
        ).fetchone()

        if user:
            return User(user)

        return None

    @staticmethod
    def get_by_email(email):
        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        if user:
            return User(user)

        return None
