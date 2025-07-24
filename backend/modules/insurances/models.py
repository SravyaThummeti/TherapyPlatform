from ...core.database import db
from datetime import datetime

class Insurance(db.Model):
    __tablename__ = 'insurances'

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    payer_id   = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
                     db.DateTime,
                     default=datetime.utcnow,
                     onupdate=datetime.utcnow,
                     nullable=False
                  )
