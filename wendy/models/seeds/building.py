import os
import sys
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))
from config import init_db
from wendy.models import *

__all__ = [
    'BuildingFaker',
    'seed_building'
]


class BuildingFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Building(**kwargs)
        await fake.save()
        return fake


def seed_building():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        BuildingFaker().generate(
            name="Fake building",
            address_id=1
        )
    ]))
    loop.close()
