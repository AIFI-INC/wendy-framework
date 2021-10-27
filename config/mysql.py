from tortoise import Tortoise
from os import environ as env

TORTOISE_ORM = {
    "connections": {
        "default": env.get('MYSQL_URL', "mysql://root@127.0.0.1:3306/wendy")
    },
    "apps": {
        "models": {
            "models": ["wendy.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(
        db_url=env.get('MYSQL_URL', "mysql://root@127.0.0.1:3306/wendy"),
        modules={'models': ['wendy.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def close_db():
    """
    Remember to close all connections before leaving
    """
    await Tortoise.close_connections()
