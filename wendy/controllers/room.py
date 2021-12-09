from typing import List
from fastapi import APIRouter, Response, status
from wendy.models import Room
from wendy.repositories import create_room, update_room_by_id, get_room_by_id, delete_room_by_id
from wendy.utilities import MSG_200_OK, MSG_500_ERROR, messages
from config import init_db, close_db
from tortoise.transactions import in_transaction
from pydantic import BaseModel
import logging
from logging import config
config.fileConfig('config/logging.conf', disable_existing_loggers=False)
LOG = logging.getLogger(__file__)
router = APIRouter()


class RoomAPI(BaseModel):

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    message: str


@router.get("/rooms", status_code=status.HTTP_200_OK)
async def list(response: Response):
    return None


@router.post("/room", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def create(room: RoomAPI, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await create_room(
            # TODO: add your attributes
        )
    except Exception as e:
        LOG.error(e)  # log internal errors for further investigation
        output.message = MSG_500_ERROR  # hide internal errors from outsiders
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.delete("/room/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await delete_room_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.put("/room/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def update(room: RoomAPI, id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await update_room_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.get("/room/{id}", status_code=status.HTTP_200_OK)
async def get(id: int, response: Response):
    room = None
    try:
        await init_db()
        room = await get_room_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return address
