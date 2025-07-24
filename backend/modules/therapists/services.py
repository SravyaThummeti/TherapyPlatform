from ...core.database import db
from .models import Therapist

def create_therapist(data):
    t = Therapist(**data)
    db.session.add(t)
    db.session.commit()
    return t

def list_therapists():
    return Therapist.query.all()
