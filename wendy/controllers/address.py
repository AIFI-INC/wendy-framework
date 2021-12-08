from fastapi import APIRouter
from wendy.models import Address
from config import init_db, close_db
from tortoise.transactions import in_transaction

router = APIRouter()


@router.get("/addresses")
async def home():
    await init_db()
    async with in_transaction(connection_name="default"):
        addresses = await Address.all()
    await close_db()
    return addresses
