from marshmallow import Schema, fields

class PatientSchema(Schema):
    id         = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name  = fields.Str(required=True)
    dob        = fields.Date(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
