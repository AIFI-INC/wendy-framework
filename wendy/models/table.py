from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient, fields
from tortoise.models import Model
from tortoise.signals import post_delete, post_save, pre_delete, pre_save

__all__ = [
    'Table'
]


class Table(Model):
    id = fields.BigIntField(pk=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'tables'
        unique_together = ()

    def __str__(self) -> str:
        return "Table"


@pre_save(Table)
async def table_pre_save(
    sender: "Type[Table]", instance: Table, using_db, update_fields
) -> None:
    print(sender, instance, using_db, update_fields)


@post_save(Table)
async def table_post_save(
    sender: "Type[Table]",
    instance: Table,
    created: bool,
    using_db: "Optional[BaseDBAsyncClient]",
    update_fields: List[str],
) -> None:
    print(sender, instance, using_db, created, update_fields)


@pre_delete(Table)
async def table_pre_delete(
    sender: "Type[Table]", instance: Table, using_db: "Optional[BaseDBAsyncClient]"
) -> None:
    print(sender, instance, using_db)


@post_delete(Table)
async def table_post_delete(
    sender: "Type[Table]", instance: Table, using_db: "Optional[BaseDBAsyncClient]"
) -> None:
    print(sender, instance, using_db)
