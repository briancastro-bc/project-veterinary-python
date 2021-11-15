from src.database import db

class Services(db.Model):
    __tablename__: str = 'services'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, name=None, image=None, description=None, value=None) -> None:
        self.name = name
        self.image = image
        self.description = description
        self.value = value