from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import ReferringProviderSchema
from .services import create_provider, list_providers

referrals_bp = Blueprint('referrals', __name__)
schema       = ReferringProviderSchema()
many_schema  = ReferringProviderSchema(many=True)

@referrals_bp.route('', methods=['POST'])
@jwt_required()
def add_provider():
    payload = request.get_json()
    errors  = schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    p = create_provider(payload)
    return schema.jsonify(p), 201

@referrals_bp.route('', methods=['GET'])
@jwt_required()
def get_providers():
    all_ = list_providers()
    return many_schema.jsonify(all_), 200
