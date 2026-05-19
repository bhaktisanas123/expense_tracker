from flask import Flask

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


@app.route("/")
def home():
    return {
        "message": "Expense Tracker API Running"
    }


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)