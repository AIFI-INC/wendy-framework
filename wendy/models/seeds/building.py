import asyncio
from faker import Faker
faker = Faker()
import sys, os
sys.path.insert(0, os.path.abspath(os.curdir))
from wendy.models import *
from config import init_db

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
            # TODO: fill your attributes here
        )
    ]))
    loop.close()

