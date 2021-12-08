from fastapi import FastAPI, APIRouter
import wendy.controllers as controllers

app = FastAPI(
    debug=True,
    title="A Wendy app",
    docs_url='/docs'
)
router = APIRouter(prefix="/v1")
router.include_router(controllers.address.router)
app.include_router(router)
