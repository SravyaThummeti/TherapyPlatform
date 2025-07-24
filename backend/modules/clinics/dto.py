from marshmallow import Schema, fields

class ClinicSchema(Schema):
    id      = fields.Int(dump_only=True)
    name    = fields.Str(required=True)
    address = fields.Str(required=True)
    fax     = fields.Str()
    npi     = fields.Str(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
