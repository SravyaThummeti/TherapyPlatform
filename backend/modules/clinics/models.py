from ...core.database import db
from datetime import datetime

class Clinic(db.Model):
    __tablename__ = 'clinics'

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    address    = db.Column(db.String(200), nullable=False)
    fax        = db.Column(db.String(20))
    npi        = db.Column(db.String(20), unique=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
                     db.DateTime,
                     default=datetime.utcnow,
                     onupdate=datetime.utcnow,
                     nullable=False
                  )
