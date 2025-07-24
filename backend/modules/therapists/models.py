from ...core.database import db
from datetime import datetime

class Therapist(db.Model):
    __tablename__ = 'therapists'

    id          = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String(50), nullable=False)
    last_name   = db.Column(db.String(50), nullable=False)
    npi         = db.Column(db.String(20), nullable=False, unique=True)
    clinic_id   = db.Column(db.Integer, db.ForeignKey('clinics.id'), nullable=False)

    created_at  = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at  = db.Column(
                     db.DateTime,
                     default=datetime.utcnow,
                     onupdate=datetime.utcnow,
                     nullable=False
                  )
