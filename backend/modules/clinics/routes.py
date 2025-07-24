from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import ClinicSchema
from .services import create_clinic, list_clinics

clinics_bp = Blueprint('clinics', __name__)
schema     = ClinicSchema()
many_schema= ClinicSchema(many=True)

@clinics_bp.route('', methods=['POST'])
@jwt_required()
def add_clinic():
    payload = request.get_json()
    errors  = schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    c = create_clinic(payload)
    return schema.jsonify(c), 201

@clinics_bp.route('', methods=['GET'])
@jwt_required()
def get_clinics():
    all_ = list_clinics()
    return many_schema.jsonify(all_), 200
