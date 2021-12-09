from fastapi import FastAPI, APIRouter
import wendy.controllers as controllers
from wendy.controllers import ResponseModel

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
