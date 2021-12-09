from tortoise.query_utils import Q
from wendy.models.chair import Chair
from tortoise.filters import *
from tortoise.transactions import atomic
import datetime

__all__ = [
    'get_chair_by_id',
    'create_chair',
    'delete_chair_by_id',
    'update_chair_by_id',
]


async def get_chair_by_id(id: int):
    return await Chair.filter(Q(id=id))


@atomic()
async def create_chair(**kwargs):
    return await Chair.create(**kwargs)


@atomic()
async def delete_chair_by_id(id: int):
    # FindAll
    records = await get_chair_by_id(id)
    for record in records:
        if record.deleted_at is None:
            record.deleted_at = datetime.datetime.utcnow()
            await record.save()


@atomic()
async def update_chair_by_id(id: int, **kwargs):
    # FindAll
    records = await get_chair_by_id(id)
    # then update
    for record in records:
        if record.deleted_at is None:
            record.update_from_dict(data=dict(kwargs))
            await record.save()
