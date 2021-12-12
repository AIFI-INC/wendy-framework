from tortoise.query_utils import Q
from wendy.models.core import Building
from tortoise.filters import *
from tortoise.transactions import atomic
import datetime

__all__ = [
    'get_building_by_id',
    'create_building',
    'delete_building_by_id',
    'update_building_by_id',
]


async def get_building_by_id(id: int):
    return await Building.filter(Q(id=id))


@atomic()
async def create_building(**kwargs):
    return await Building.create(**kwargs)


@atomic()
async def delete_building_by_id(id: int):
    # FindAll
    records = await get_building_by_id(id)
    for record in records:
        if record.deleted_at is None:
            record.deleted_at = datetime.datetime.utcnow()
            await record.save()


@atomic()
async def update_building_by_id(id: int, **kwargs):
    # FindAll
    records = await get_building_by_id(id)
    # then update
    for record in records:
        if record.deleted_at is None:
            record.update_from_dict(data=dict(kwargs))
            await record.save()
