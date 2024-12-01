import logging
from logging.config import dictConfig

from hack_change_backend.core.config import MODE


# Конфигурация логгера
def configure_logging():
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
            },
            "color": {
                "()": "colorlog.ColoredFormatter",
                "format": "%(log_color)s[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "color",
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "app.log",
                "encoding": "utf8",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file"],
        },
    }

    dictConfig(log_config)


# Настройка логгера
configure_logging()
logger = logging.getLogger("backend")

if MODE == "dev":
    logger.setLevel(logging.DEBUG)
