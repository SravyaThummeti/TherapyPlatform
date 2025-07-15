from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.utils.validators import is_valid_email
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate email domain
    if not is_valid_email(data.get('email', '')):
        return jsonify(msg='Email must end with @tempohealthgroup.com'), 400

    # Prevent duplicate
    if User.query.filter_by(email=data['email']).first():
        return jsonify(msg='Email already exists'), 400

    # Create user
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        role=data['role']
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify(msg='Registration successful'), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.check_password(data.get('password', '')):
        return jsonify(msg='Invalid credentials'), 401

    # Create JWT including role
    access_token = create_access_token(
        identity={'id': user.id, 'role': user.role}
    )
    return jsonify(access_token=access_token), 200