from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import AuthorizationSchema
from .services import create_authorization

authorizations_bp = Blueprint('authorizations', __name__)
schema = AuthorizationSchema()

@authorizations_bp.route('', methods=['POST'])
@jwt_required()
def add_authorization():
    payload = request.get_json()
    errors = schema.validate(payload)
    if errors:
        return jsonify(errors), 400

    auth = create_authorization(payload)
    return schema.jsonify(auth), 201
