from tortoise import fields
from tortoise.models import Model

structure = None
class Structure(Model):

    class Meta:
        table = "structure"

    id = fields.UUIDField(pk=True)
    structure = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
