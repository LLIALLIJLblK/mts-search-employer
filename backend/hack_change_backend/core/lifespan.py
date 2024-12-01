from fastapi import FastAPI

from hack_change_backend.core import config
from hack_change_backend.core.database import close_database, init_database
from hack_change_backend.core.logger import logger
from hack_change_backend.data_generator import seed_database
from hack_change_backend.utils import (
    load_city,
    load_education_type,
    load_institute,
    load_position,
    load_skill,
    load_specialization,
    load_work_category,
    load_projects,
)


async def lifespan(app: FastAPI):
    logger.info("Starting app")
    await init_database()

    if config.MODE == "dev":
        logger.info("Loading test data")
        logger.info(f"Loaded {len(await load_city())} cities")
        logger.info(f"Loaded {len(await load_education_type())} education types")
        logger.info(f"Loaded {len( await load_institute())} institutes")
        logger.info(f"Loaded {len(await load_position())} positions")
        logger.info(f"Loaded {len(await load_skill())} skills")
        logger.info(f"Loaded {len(await load_specialization())} specializations")
        logger.info(f"Loaded {len(await load_work_category())} work categories")
        logger.info(f"Loaded {len(await load_projects())} projects")

        await seed_database()
        logger.info("Test data loaded")

    yield
    logger.info("Shutting down app")
    await close_database()
