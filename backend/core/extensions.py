from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS


from .database import db

# Instantiate extensions
# db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors    = CORS()
__all__ = ['db', 'migrate', 'jwt', 'cors', 'jwt_required']