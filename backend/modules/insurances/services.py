from ...core.database import db
from .models import Insurance

def create_insurance(data):
    ins = Insurance(**data)
    db.session.add(ins)
    db.session.commit()
    return ins

def list_insurances():
    return Insurance.query.all()
