import os
import sys
import asyncio
from faker import Faker
faker = Faker()
sys.path.insert(0, os.path.abspath(os.curdir))
from config import init_db
from wendy.models import *

__all__ = [
    'AddressFaker',
    'seed_address'
]


class AddressFaker(object):
    async def generate(self, **kwargs):
        await init_db()
        fake = Address(**kwargs)
        await fake.save()
        return fake


def seed_address():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        AddressFaker().generate(
            country_code=84,
            post_code=faker.postcode(),
            city=faker.city(),
            province=faker.state(),
            address_1=faker.street_address(),
            address_2=None
        )
    ]))
    loop.close()
