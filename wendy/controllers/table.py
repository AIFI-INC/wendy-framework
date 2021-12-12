from typing import List
from fastapi import APIRouter, Response, status
from wendy.models import Table
from wendy.repositories import create_table, update_table_by_id, get_table_by_id, delete_table_by_id
from wendy.utilities import MSG_200_OK, MSG_500_ERROR, messages
from config import init_db, close_db
from tortoise.transactions import in_transaction
from pydantic import BaseModel
from config import *
LOG = getLogger(__file__)
router = APIRouter()


class TableAPI(BaseModel):

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    message: str


@router.get("/tables", status_code=status.HTTP_200_OK)
async def list(response: Response):
    return None


@router.post("/table", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def create(table: TableAPI, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await create_table(
            # TODO: add your attributes
        )
    except Exception as e:
        LOG.error(e)  # log internal errors for further investigation
        output.message = MSG_500_ERROR  # hide internal errors from outsiders
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.delete("/table/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await delete_table_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.put("/table/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def update(table: TableAPI, id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await update_table_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.get("/table/{id}", status_code=status.HTTP_200_OK)
async def get(id: int, response: Response):
    table = None
    try:
        await init_db()
        table = await get_table_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return address
