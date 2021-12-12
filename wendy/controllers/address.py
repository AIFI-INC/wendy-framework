from typing import List
from fastapi import APIRouter, Response, status
from starlette.types import Message
from wendy.models import Address
from wendy.repositories import create_address, update_address_by_id, get_address_by_id, delete_address_by_id
from wendy.utilities import MSG_200_OK, MSG_500_ERROR, messages
from config import init_db, close_db
from tortoise.transactions import in_transaction
from pydantic import BaseModel
from config import *
LOG = getLogger(__file__)
router = APIRouter()


class AddressAPI(BaseModel):
    longtitude: float
    latitude: float
    country_code: str
    post_code: str
    city: str
    province: str
    address_1: str
    address_2: str

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    message: str


@router.get("/addresses", status_code=status.HTTP_200_OK)
async def list(response: Response):
    addresses = []
    try:
        await init_db()
        addresses = await Address.all()
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return addresses


@router.post("/address", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def create(address: AddressAPI, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await create_address(
            longtitude=address.longtitude,
            latitude=address.latitude,
            country_code=address.country_code,
            post_code=address.post_code,
            city=address.city,
            province=address.province,
            address_1=address.address_1,
            address_2=address.address_2
        )
    except Exception as e:
        LOG.error(e)  # log internal errors for further investigation
        output.message = MSG_500_ERROR  # hide internal errors from outsiders
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.delete("/address/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await delete_address_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.put("/address/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def update(address: AddressAPI, id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await update_address_by_id(id=id,
                                   longtitude=address.longtitude,
                                   latitude=address.latitude,
                                   country_code=address.country_code,
                                   post_code=address.post_code,
                                   city=address.city,
                                   province=address.province,
                                   address_1=address.address_1,
                                   address_2=address.address_2)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.get("/address/{id}", status_code=status.HTTP_200_OK)
async def get(id: int, response: Response):
    address = None
    try:
        await init_db()
        address = await get_address_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return address
