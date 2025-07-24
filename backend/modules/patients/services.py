from ...core.database import db
from .models import Patient

def create_patient(data):
    p = Patient(**data)
    db.session.add(p)
    db.session.commit()
    return p
