from tortoise.query_utils import Q
from wendy.models.core import Table
from tortoise.filters import *
from tortoise.transactions import atomic
import datetime

__all__ = [
    'get_table_by_id',
    'create_table',
    'delete_table_by_id',
    'update_table_by_id',
]


async def get_table_by_id(id: int):
    return await Table.filter(Q(id=id))


@atomic()
async def create_table(**kwargs):
    return await Table.create(**kwargs)


@atomic()
async def delete_table_by_id(id: int):
    # FindAll
    records = await get_table_by_id(id)
    for record in records:
        if record.deleted_at is None:
            record.deleted_at = datetime.datetime.utcnow()
            await record.save()


@atomic()
async def update_table_by_id(id: int, **kwargs):
    # FindAll
    records = await get_table_by_id(id)
    # then update
    for record in records:
        if record.deleted_at is None:
            record.update_from_dict(data=dict(kwargs))
            await record.save()
