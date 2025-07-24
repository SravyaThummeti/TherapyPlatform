from marshmallow import Schema, fields, validate

class ReferringProviderSchema(Schema):
    id    = fields.Int(dump_only=True)
    name  = fields.Str(required=True, validate=validate.Length(max=100))
    phone = fields.Str(validate=validate.Length(max=20))
    email = fields.Email()

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
