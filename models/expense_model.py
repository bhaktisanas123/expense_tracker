from extensions import db 

class Expense(db.Model):
    __tablename__="expenses" 

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    amount=db.Column(db.Float,nullable=False) 
    category=db.Column(db.String(100),nullable=False) 

    user_id=db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    ) 

    def __repr__(self):
        return f"<expense {self.title}" 
    

