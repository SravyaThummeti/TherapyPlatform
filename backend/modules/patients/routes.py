from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import PatientSchema
from .services import create_patient

patients_bp = Blueprint('patients', __name__)
schema      = PatientSchema()

@patients_bp.route('', methods=['POST'])
@jwt_required()
def add_patient():
    payload = request.get_json()
    errors  = schema.validate(payload)
    if errors:
        return jsonify(errors), 400

    patient = create_patient(payload)
    return schema.jsonify(patient), 201
