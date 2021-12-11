from fastapi import FastAPI, APIRouter, staticfiles
import wendy.controllers as controllers
from wendy.controllers import ResponseModel
from config import *

app = FastAPI(
    debug=True,
    title="A Wendy app",
    docs_url='/docs'
)
router = APIRouter(prefix="/v1")
router.include_router(controllers.address.router)
router.include_router(controllers.building.router)
router.include_router(controllers.room.router)
router.include_router(controllers.table.router)
router.include_router(controllers.chair.router)
app.include_router(router)
app.mount('/static', staticfiles.StaticFiles(directory=env.get('STATIC_DIR', 'static')), name='static')
