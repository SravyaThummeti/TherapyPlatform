from ...core.database import db
from datetime import datetime

class ReferringProvider(db.Model):
    __tablename__ = 'referring_providers'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    phone       = db.Column(db.String(20))
    email       = db.Column(db.String(120))
    created_at  = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at  = db.Column(
                     db.DateTime,
                     default=datetime.utcnow,
                     onupdate=datetime.utcnow,
                     nullable=False
                  )

class ReferralRequest(db.Model):
    __tablename__ = 'referral_requests'

    id                    = db.Column(db.Integer, primary_key=True)
    patient_id            = db.Column(db.Integer,
                                      db.ForeignKey('patients.id'),
                                      nullable=False)
    discipline            = db.Column(db.String(50), nullable=False)
    notes                 = db.Column(db.Text, nullable=False)
    referring_provider_id = db.Column(db.Integer,
                                      db.ForeignKey('referring_providers.id'),
                                      nullable=False)
    physician_name        = db.Column(db.String(100), nullable=False)
    physician_signature   = db.Column(db.String(200))
    physician_signed_at   = db.Column(db.Date)
    requested_at          = db.Column(db.Date, nullable=False)

    created_at            = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at            = db.Column(
                             db.DateTime,
                             default=datetime.utcnow,
                             onupdate=datetime.utcnow,
                             nullable=False
                          )
