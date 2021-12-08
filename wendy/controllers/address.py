from fastapi import APIRouter

router = APIRouter()


@router.get("/addresses")
async def home():
    return {"message": "welcome"}
