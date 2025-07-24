from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, cors
from ..modules.auth.routes import bp as auth_bp
from ..modules.authorizations.routes import authorizations_bp
from ..modules.patients.routes import patients_bp
from ..modules.therapists.routes  import therapists_bp
from ..modules.referrals.routes   import referrals_bp
from ..modules.insurances.routes  import insurances_bp
from ..modules.clinics.routes     import clinics_bp

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
    app.register_blueprint(patients_bp, url_prefix='/api/patients')
    app.register_blueprint(therapists_bp, url_prefix='/api/therapists')
    app.register_blueprint(insurances_bp, url_prefix='/api/insurances')
    app.register_blueprint(clinics_bp, url_prefix='/api/clinics')
    app.register_blueprint(referrals_bp, url_prefix='/api/referrals')
    app.register_blueprint(authorizations_bp, url_prefix='/api/authorizations')
    
    return app