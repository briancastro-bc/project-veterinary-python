from src.database import db

class Pet(db.Model):
    __tablename__: str = 'Pets'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    breed = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.String(36), db.ForeignKey('user.uid'), nullable=False)

    def __init__(self, uid=None, name=None, breed=None, age=None, owner=None) -> None:
        self.uid = uid
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner