from marshmallow import Schema, fields, validate

class AuthorizationSchema(Schema):
    id                = fields.Int(dump_only=True)
    patient_id        = fields.Int(required=True)
    therapist_id      = fields.Int(required=True)
    insurance_id      = fields.Int(required=True)
    referral_id       = fields.Int(allow_none=True)

    start_date        = fields.Date(required=True)
    end_date          = fields.Date(required=True)
    visits_authorized = fields.Int(
                            required=True,
                            validate=validate.Range(min=1)
                        )
