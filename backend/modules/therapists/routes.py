from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import TherapistSchema
from .services import create_therapist, list_therapists

therapists_bp = Blueprint('therapists', __name__)
schema        = TherapistSchema()
many_schema   = TherapistSchema(many=True)

@therapists_bp.route('', methods=['POST'])
@jwt_required()
def add_therapist():
    payload = request.get_json()
    errors  = schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    t = create_therapist(payload)
    return schema.jsonify(t), 201

@therapists_bp.route('', methods=['GET'])
@jwt_required()
def get_therapists():
    all_ = list_therapists()
    return many_schema.jsonify(all_), 200
