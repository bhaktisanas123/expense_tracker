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

@expense.route("/expenses",methods=["GET"])
@jwt_required() 

def get_expenses():
    current_user=get_jwt_identity()

    expenses= Expense.query.filter_by(
        user_id=current_user
    ).all() 

    expenses_list=[] 

    for expense_item in expenses:
        
        expenses_list.append({
            "id":expense_item.id,
            "title":expense_item.title,
            "amount":expense_item.amount,
            "category":expense_item.category
        })  

    return jsonify(expenses_list),200  

@expense.route("/expenses/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_expense(id):

    
    current_user = int(get_jwt_identity())

    
    expense_item = Expense.query.get(id)

    
    if not expense_item:
        return jsonify({
            "message": "Expense not found"
        }), 404

    
    if expense_item.user_id != current_user:
        return jsonify({
            "message": "Unauthorized access"
        }), 403

    
    db.session.delete(expense_item)

    db.session.commit()

    return jsonify({
        "message": "Expense deleted successfully"
    }), 200 


@expense.route("/expenses/<int:id>", methods=["PUT"])
@jwt_required()
def update_expense(id):

    # Get logged-in user id
    current_user = int(get_jwt_identity())

    # Find expense
    expense_item = Expense.query.get(id)

    # Check if expense exists
    if not expense_item:
        return jsonify({
            "message": "Expense not found"
        }), 404

    # Authorization check
    if expense_item.user_id != current_user:
        return jsonify({
            "message": "Unauthorized access"
        }), 403

    data = request.get_json()

    # Update fields
    expense_item.title = data.get(
        "title",
        expense_item.title
    )

    expense_item.amount = data.get(
        "amount",
        expense_item.amount
    )

    expense_item.category = data.get(
        "category",
        expense_item.category
    )

    # Save updates
    db.session.commit()

    return jsonify({
        "message": "Expense updated successfully"
    }), 200