from app import db 

class Staff(db.Model):
    sid=db.Column(db.Integer, primary_key=True  )
    name=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(225),nullable=False)


