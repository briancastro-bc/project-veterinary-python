from src.database import db

class User(db.Model):
    __tablename__: str = 'users'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    pets = db.relationship('Pet', backref='user', lazy=True)

    def __init__(self, email=None, password=None, name=None, last_name=None) -> None:
        import uuid
        self.uid = uuid.uuid4()
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name