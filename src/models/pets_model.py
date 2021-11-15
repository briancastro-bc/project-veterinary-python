from src.database import db

class Pet(db.Model):
    __tablename__: str = 'pets'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    breed = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.String(36), db.ForeignKey('users.uid'), nullable=False)
    appointments = db.relationship('Appointment', backref='pets', lazy=True)

    def __init__(self, name=None, breed=None, age=None, owner=None) -> None:
        import uuid
        self.uid = uuid.uuid4()
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner