from marshmallow import Schema, fields

class TherapistSchema(Schema):
    id          = fields.Int(dump_only=True)
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    npi         = fields.Str(required=True)
    clinic_id   = fields.Int(required=True)

    created_at  = fields.DateTime(dump_only=True)
    updated_at  = fields.DateTime(dump_only=True)
