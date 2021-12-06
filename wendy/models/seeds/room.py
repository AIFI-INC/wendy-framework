import os
import sys
from config import init_db
from wendy.models import *
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))

__all__ = [
    'RoomFaker'
]


class RoomFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Room(**kwargs)
        await fake.save()
        return fake


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    RoomFaker().generate(
        # TODO: fill your attributes here
    )
]))
loop.close()
