from datetime import datetime

from tortoise import Model, fields


class AbstractModel(Model):
    id: int = fields.IntField(pk=True)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)
    is_deleted: bool = fields.BooleanField(default=False)

    class Meta:
        abstract = True
