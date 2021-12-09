from typing import List
from fastapi import APIRouter, Response, status
from wendy.models import Building
from wendy.repositories import create_building, update_building_by_id, get_building_by_id, delete_building_by_id
from wendy.utilities import MSG_200_OK, MSG_500_ERROR, messages
from config import init_db, close_db
from tortoise.transactions import in_transaction
from pydantic import BaseModel
import logging
from logging import config
config.fileConfig('config/logging.conf', disable_existing_loggers=False)
LOG = logging.getLogger(__file__)
router = APIRouter()


class BuildingAPI(BaseModel):

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    message: str


@router.get("/buildings", status_code=status.HTTP_200_OK)
async def list(response: Response):
    return None


@router.post("/building", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def create(building: BuildingAPI, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await create_building(
            # TODO: add your attributes
        )
    except Exception as e:
        LOG.error(e)  # log internal errors for further investigation
        output.message = MSG_500_ERROR  # hide internal errors from outsiders
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.delete("/building/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await delete_building_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.put("/building/{id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def update(building: BuildingAPI, id: int, response: Response):
    output = ResponseModel(
        message=MSG_200_OK
    )
    try:
        await init_db()
        await update_building_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        output.message = MSG_500_ERROR
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return output


@router.get("/building/{id}", status_code=status.HTTP_200_OK)
async def get(id: int, response: Response):
    building = None
    try:
        await init_db()
        building = await get_building_by_id(id=id)
    except Exception as e:
        LOG.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return address
