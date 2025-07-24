from flask import Blueprint, request, jsonify
from ...core.extensions import jwt_required
from .dto import InsuranceSchema
from .services import create_insurance, list_insurances

insurances_bp = Blueprint('insurances', __name__)
schema        = InsuranceSchema()
many_schema   = InsuranceSchema(many=True)

@insurances_bp.route('', methods=['POST'])
@jwt_required()
def add_insurance():
    payload = request.get_json()
    errors  = schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    ins = create_insurance(payload)
    return schema.jsonify(ins), 201

@insurances_bp.route('', methods=['GET'])
@jwt_required()
def get_insurances():
    all_ = list_insurances()
    return many_schema.jsonify(all_), 200
