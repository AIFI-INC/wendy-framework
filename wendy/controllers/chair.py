from typing import List
from fastapi import APIRouter, Response, status
from wendy.models import Chair
from wendy.repositories import create_chair, update_chair_by_id, get_chair_by_id, delete_chair_by_id
from wendy.utilities import MSG_200_OK, MSG_500_ERROR, messages
from config import init_db, close_db
from tortoise.transactions import in_transaction
from pydantic import BaseModel
from config import *
LOG = getLogger(__file__)
router = APIRouter()


class ChairAPI(BaseModel):

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    message: str


@router.get("/chairs", status_code=status.HTTP_200_OK)
async def list(response: Response):
    return None


@router.post("/chair", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def create(chair: ChairAPI, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await create_chair(
            # TODO: add your attributes
        )
    except Exception as e:
        LOG.error(e)  # log internal errors for further investigation
        output.message = MSG_500_ERROR  # hide internal errors from outsiders
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.delete("/chair/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await delete_chair_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.put("/chair/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def update(chair: ChairAPI, id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await update_chair_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.get("/chair/{id}", status_code=status.HTTP_200_OK)
async def get(id: int, response: Response):
    chair = None
    try:
        await init_db()
        chair = await get_chair_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return address
