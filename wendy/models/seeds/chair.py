import os
import sys
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))
from config import init_db
from wendy.models import *

__all__ = [
    'ChairFaker',
    'seed_chair'
]


class ChairFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Chair(**kwargs)
        await fake.save()
        return fake


def seed_chair():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        ChairFaker().generate(
            position="Leader",
            room_id=1
        ),
        ChairFaker().generate(
            position="Dev",
            room_id=1
        )
    ]))
    loop.close()
