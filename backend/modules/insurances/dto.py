from marshmallow import Schema, fields

class InsuranceSchema(Schema):
    id       = fields.Int(dump_only=True)
    name     = fields.Str(required=True)
    payer_id = fields.Str()

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
