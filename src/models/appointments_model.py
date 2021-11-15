from src.database import db
import datetime

class Appointment(db.Model):
    __tablename__: str = 'appointments'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    service = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    pet = db.Column(db.String(36), db.ForeignKey('pets.uid'), nullable=False)
    to_day = db.Column(db.DATETIME, nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.utcnow())
    
    def __init__(self, service=None, pet=None, to_day=None) -> None:
        import uuid
        self.uid = uuid.uuid4()
        self.service = service
        self.pet = pet
        self.to_day = to_day