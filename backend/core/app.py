from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, cors
from ..modules.auth.routes import bp as auth_bp
from ..modules.authorizations.routes import authorizations_bp
from ..modules.patients.routes import patients_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(authorizations_bp, url_prefix='/api/authorizations')
    app.register_blueprint(patients_bp, url_prefix='/api/patients')
    
    return app