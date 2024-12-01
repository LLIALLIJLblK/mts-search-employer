from tortoise import Tortoise

from hack_change_backend.core.config import TORTOISE_ORM
from hack_change_backend.core.logger import logger


async def init_database():
    logger.info("Initializing database")
    await Tortoise.init(config=TORTOISE_ORM)
    # Generate the schema
    await Tortoise.generate_schemas()


async def close_database():
    logger.info("Close database connections")
    await Tortoise.close_connections()
