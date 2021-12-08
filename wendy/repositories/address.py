from tortoise.query_utils import Q
from wendy.models.core import Address
from tortoise.filters import *
from tortoise.transactions import atomic
import datetime

__all__ = [
    'get_address_by_id',
    'create_address',
    'delete_address_by_id',
    'update_address_by_id',
]


async def get_address_by_id(id: int):
    return await Address.filter(Q(id=id))


@atomic()
async def create_address(**kwargs):
    return await Address.create(**kwargs)


@atomic()
async def delete_address_by_id(id: int):
    # FindAll
    records = await get_address_by_id(id)
    for record in records:
        if record.deleted_at is None:
            record.deleted_at = datetime.datetime.utcnow()
            await record.save()


@atomic()
async def update_address_by_id(id: int, **kwargs):
    # FindAll
    records = await get_address_by_id(id)
    # then update
    for record in records:
        if record.deleted_at is None:
            record.update_from_dict(data=dict(kwargs))
            await record.save()
