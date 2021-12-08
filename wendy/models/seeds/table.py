import os
import sys
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))
from config import init_db
from wendy.models import *

__all__ = [
    'TableFaker',
    'seed_table'
]


class TableFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Table(**kwargs)
        await fake.save()
        return fake


def seed_table():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        TableFaker().generate(
            # TODO: fill your attributes here
        )
    ]))
    loop.close()
