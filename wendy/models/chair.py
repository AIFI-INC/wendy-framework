from tortoise.models import Model
from tortoise import fields

__all__ = [
    'Chair'
]


class Chair(Model):
    id = fields.BigIntField(pk=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'chairs'
        unique_together = ()

    def __str__(self) -> str:
        return "Chair"
