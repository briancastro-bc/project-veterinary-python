from src.database import db

class User(db.Model):
    __tablename__: str = 'Users'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    name = db.Column(db.string(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    pets = db.relationship('Pet', backref='user', lazy=True)

    def __init__(self, uid=None, email=None, password=None, name=None, last_name=None) -> None:
        self.uid = uid
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name