from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.staticfiles import StaticFiles

from hack_change_backend.api.auth import auth
from hack_change_backend.api.data_controller import data_controller
from hack_change_backend.api.v1.admin import admin
from hack_change_backend.api.v1.controller import controller
from hack_change_backend.api.v1.filter import filter_controller
from hack_change_backend.api.v1.hierarchy import hierarchy
from hack_change_backend.core import config
from hack_change_backend.core.lifespan import lifespan
from hack_change_backend.core.middlevare import TimeMiddleware
from hack_change_backend.core.logger import logger

app = FastAPI(
    title=config.APP_TITLE,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
    lifespan=lifespan,
)

app.add_middleware(TimeMiddleware)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)

app.mount("/static", StaticFiles(directory="hack_change_backend/static"), name="static")

app.include_router(auth, tags=["auth"], prefix="/auth")
app.include_router(data_controller, tags=["dictionary"], prefix="/dictionary")
app.include_router(controller, tags=["controller"])
app.include_router(hierarchy, tags=["hierarchy"], prefix="/hierarchy")
app.include_router(admin, tags=["admin"], prefix="/admin")
app.include_router(filter_controller, tags=["filters"], prefix="/filters")
logger.debug("Setup prometheus instrumentator")
Instrumentator().instrument(app).expose(app)
