from flask import Flask,redirect
from flask import render_template

from config import Config
from extensions import db, jwt

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

from models.user_model import User 
from models.expense_model import Expense 

from routes.auth_routes import auth
app.register_blueprint(auth) 

from routes.expense_routes import expense 
app.register_blueprint(expense)


@app.route("/")
def register_page():

    return render_template("register.html") 

@app.route("/login")
def login_page():

    return render_template("login.html") 

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)