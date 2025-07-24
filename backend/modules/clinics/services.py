from ...core.database import db
from .models import Clinic

def create_clinic(data):
    c = Clinic(**data)
    db.session.add(c)
    db.session.commit()
    return c

def list_clinics():
    return Clinic.query.all()
