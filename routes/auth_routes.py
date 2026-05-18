from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from extensions import db
from models.user_model import User

auth = Blueprint("auth", __name__) 

@auth.route("/register",methods=["POST"])
def register():

    data=request.get_json()

    username=data.get("username")
    email=data.get("email")
    password=data.get("password")
    
    existing_user=User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message":"email already exit"
        }),404  
    
    hashed_password=generate_password_hash(password) 

    new_user=User( 
        username=username,
        email=email,
        password=hashed_password
    ) 

    db.session.add(new_user)
    db.session.commit() 

    return jsonify({
        "message":"user registered successfully"
    }),201