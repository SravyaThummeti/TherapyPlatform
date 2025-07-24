from ...core.database import db
from .models import Authorization

def create_authorization(data):
    auth = Authorization(**data)
    db.session.add(auth)
    db.session.commit()
    return auth
