import random
import time

import jwt
from passlib.context import CryptContext

from hack_change_backend.core.config import (ACCESS_TOKEN_EXPIRE_MINUTES,
                                             ALGORITHM, SECRET_KEY)
from hack_change_backend.core.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    @staticmethod
    async def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    async def get_password_hash(password):
        return pwd_context.hash(password)


class AuthenticationToken:

    @staticmethod
    async def encode(payload: dict) -> str:
        payload["exp"] = int(time.time() + ACCESS_TOKEN_EXPIRE_MINUTES)
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM,
        )

    @staticmethod
    async def decode(jwt_token: str) -> dict:
        try:
            return jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception as e:
            logger.warning(
                "Decode jwt token error",
                extra={
                    "error": str(e),
                },
            )
            raise  # TODO


class RandomGenerator:

    @staticmethod
    async def generate_verify_code(length: int = 4) -> str:
        return "".join([random.choice("0123456789") for _ in range(length)])


PasswordHasherProvider = Hasher()
AuthenticationTokenProvider = AuthenticationToken()
RandomGeneratorProvider = RandomGenerator()
