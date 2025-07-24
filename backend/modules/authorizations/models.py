from ...core.database import db
from datetime import datetime

class Authorization(db.Model):
    __tablename__ = 'authorizations'

    id                 = db.Column(db.Integer, primary_key=True)
    patient_id         = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    therapist_id       = db.Column(db.Integer, db.ForeignKey('therapists.id'), nullable=False)
    insurance_id       = db.Column(db.Integer, db.ForeignKey('insurances.id'), nullable=False)
    referral_id        = db.Column(db.Integer, db.ForeignKey('referral_requests.id'), nullable=True)

    start_date         = db.Column(db.Date, nullable=False)
    end_date           = db.Column(db.Date, nullable=False)
    visits_authorized  = db.Column(db.Integer, nullable=False)

    created_at         = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at         = db.Column(
                            db.DateTime,
                            default=datetime.utcnow,
                            onupdate=datetime.utcnow,
                            nullable=False
                        )
