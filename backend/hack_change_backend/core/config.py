from typing import Literal

MODE: Literal["dev", "prod"] = "dev"  # менять мод на prod для прода
# при dev моде - некоторые функции отключены, включено заполнение бд данными


# App
APP_TITLE = "HackChange"  # Меняет название приложение - отображение в Swagger
APP_VERSION = "0.0.1"  # меняет версию приложения - отображение в Swagger
APP_DESCRIPTION = "Backend service for HackChange hackathon"  # меняет описание приложение - отображение в Swagger

# DataBase
DATABASE_MODULES = {
    "models": [
        "hack_change_backend.models",
    ]
}

DATABASE_URL = "sqlite://database.db"  # меняет строку подключения к бд, можно заменить бд на postgresql / mysql поменяв эту строку
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "hack": {
            "models": DATABASE_MODULES["models"],
            "default_connection": "default",
        },
        "aerich": {  # Не забудьте добавить эту секцию для Aerich
            "models": ["aerich.models"],
            "default_connection": "default",
        },
    },
}

# Auth
SECRET_KEY = "123"  #! change in production # Секретный ключ для генерации JWT токена - поменять на проде на что-то более серьезное
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30  # Minutes
PLATFORM_KEYS = ["123"]  # Ключи для регистрации
