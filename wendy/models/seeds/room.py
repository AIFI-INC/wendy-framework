import asyncio
from faker import Faker
faker = Faker()
import sys, os
sys.path.insert(0, os.path.abspath(os.curdir))
from wendy.models import *
from config import init_db

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
            # TODO: fill your attributes here
        )
    ]))
    loop.close()

