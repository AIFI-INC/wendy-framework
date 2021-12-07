import os
import sys
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))
from config import init_db
from wendy.models import *

__all__ = [
    'RoomFaker',
    'seed_room'
]


class RoomFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Room(**kwargs)
        await fake.save()
        return fake


def seed_room():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        RoomFaker().generate(
            name="Fake room",
            floor=4,
            building_id=2
        )
    ]))
    loop.close()
