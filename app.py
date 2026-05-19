from flask import Flask
from extensions import login_manager
from config import Config

from routes.auth import auth_bp
from models.user import User

app = Flask(__name__)

app.config.from_object(Config)

login_manager.init_app(app)

app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route("/dashboard")
def dashboard():
    return "Dashboard Working"

if __name__ == "__main__":
    app.run(debug=True)
