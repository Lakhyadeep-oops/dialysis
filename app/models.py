from app import db 

class Staff(db.Model):
    sid=db.Column(db.Integer, primary_key=True  )
    name=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(225),nullable=False)

class Patient(db.Model):
    pid=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(225),nullable=False)

class DialysisRecord(db.Model):
    pid = db.Column(
        db.Integer,
        db.ForeignKey("patient.pid"),
        primary_key=True
    )

    date = db.Column(db.Date, primary_key=True)

    pre_weight = db.Column(db.Float)
    post_weight = db.Column(db.Float)

    pre_bp = db.Column(db.String(20))
    post_bp = db.Column(db.String(20))

    uf = db.Column(db.Float)

    remarks = db.Column(db.Text)
    medications = db.Column(db.Text)