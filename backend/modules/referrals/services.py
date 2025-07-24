from ...core.database import db
from .models import ReferringProvider

def create_provider(data):
    prov = ReferringProvider(**data)
    db.session.add(prov)
    db.session.commit()
    return prov

def list_providers():
    return ReferringProvider.query.all()
