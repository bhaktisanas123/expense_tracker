from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db
from models.expense_model import Expense

expense = Blueprint("expense", __name__)  

@expense.route("/expenses",methods=["POST"]) 
@jwt_required()
def add_expense():

    current_user=get_jwt_identity()

    data=request.get_json() 

    title=data.get("title")
    amount=data.get("amount")
    category=data.get("category") 

    new_expense=Expense(
        title=title,
        amount=amount,
        category=category,
        user_id=current_user
    ) 

    db.session.add(new_expense)
    db.session.commit() 

    return jsonify({
        "message":"Expense added successfully"
    }),201 

