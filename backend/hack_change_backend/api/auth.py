import traceback

from fastapi import APIRouter, Depends, Header, Request
from tortoise.transactions import in_transaction

from hack_change_backend.api.deps import get_user
from hack_change_backend.core.config import PLATFORM_KEYS
from hack_change_backend.core.exceptions import (
    EmailAlreadyExists,
    InvalidCredentials,
    TokenGenerationError,
    TransactionError,
    UserNotFound,
    InvalidPlatformCredentials,
)
from hack_change_backend.core.logger import logger
from hack_change_backend.core.secutity import (
    AuthenticationTokenProvider,
    PasswordHasherProvider,
)
from hack_change_backend.models import (
    UserOrm,
    RegistrationKeyOrm,
    PositionOrm,
    DepartamentOrm,
    TeamOrm,
)
from hack_change_backend.schemas import AuthUserOutDto, SignInUserDto, SignUpUserDto

auth = APIRouter()


@auth.post(
    "/sign-up",
    summary="Регистрация пользователя",
    description="Создает нового пользователя и возвращает токен аутентификации.",
    responses={
        200: {"description": "Пользователь успешно зарегистрирован."},
        400: {"description": "Email уже существует или некорректные данные."},
        401: {"description": "Неверный ключ для регистрации на платформу (123)"},
        500: {
            "description": "Ошибка на сервере при создании пользователя или генерации токена."
        },
    },
)
async def sign_up(request: Request, data: SignUpUserDto) -> AuthUserOutDto:
    """
    Регистрация нового пользователя.

    Параметры
    ----------
    request : Request
        Запрос FastAPI.
    data : SignUpUserDto
        Данные для регистрации пользователя, включая email и пароль.

    Возвращаемое значение
    ---------------------
    AuthUserOutDto
        Токен аутентификации для зарегистрированного пользователя.

    Исключения
    ----------
    EmailAlreadyExists
        Выбрасывается, если пользователь с данным email уже существует.
    InvalidCredentials
        Выбрасывается, если ключ для регистрации на платформе не верный.
    TransactionError
        Выбрасывается, если произошла ошибка при выполнении транзакции.
    TokenGenerationError
        Выбрасывается, если произошла ошибка при генерации токена.
    """
    scope = await RegistrationKeyOrm.get_or_none(key=data.platform_key)
    if scope is None:
        raise InvalidPlatformCredentials
    if await UserOrm.exists(email=data.email):
        raise EmailAlreadyExists

    try:
        async with in_transaction() as transaction:
            user = await UserOrm.create(
                email=data.email,
                password=await PasswordHasherProvider.get_password_hash(
                    password=data.password
                ),
                using_db=transaction,
            )
            position = await scope.position.get()
            user.position = position
            if scope.team:
                team = await scope.team.get()
                await team.members.add(user)
            if scope.departament:
                departament = await scope.departament.get()
                await departament.members.add(user)
            await user.save()
            logger.info(f"User {user.id} created")
        await scope.delete()
    except Exception as e:
        logger.error(f"Error during sign-up: {e}, Traceback: {traceback.format_exc()}")
        raise TransactionError

    try:
        token = await AuthenticationTokenProvider.encode({"user_id": user.id})
    except Exception as e:
        logger.error(
            f"Error generating token: {e}, Traceback: {traceback.format_exc()}"
        )
        raise TokenGenerationError

    return AuthUserOutDto(token=token)


@auth.post(
    "/sign-in",
    summary="Аутентификация пользователя",
    description="Аутентифицирует пользователя по email и паролю и возвращает токен.",
    responses={
        200: {"description": "Пользователь успешно аутентифицирован."},
        400: {"description": "Некорректные данные."},
        401: {"description": "Неверный email или пароль."},
        404: {"description": "Пользователь не найден."},
        500: {"description": "Ошибка на сервере при генерации токена."},
    },
)
async def sign_in(request: Request, data: SignInUserDto) -> AuthUserOutDto:
    """
    Аутентификация пользователя.

    Параметры
    ----------
    request : Request
        Запрос FastAPI.
    data : SignInUserDto
        Данные для входа пользователя, включая email и пароль.

    Возвращаемое значение
    ---------------------
    AuthUserOutDto
        Токен аутентификации для аутентифицированного пользователя.

    Исключения
    ----------
    UserNotFound
        Выбрасывается, если пользователь с данным email не найден.
    InvalidCredentials
        Выбрасывается, если пароль неверный.
    TokenGenerationError
        Выбрасывается, если произошла ошибка при генерации токена.
    """
    user = await UserOrm.get_or_none(email=data.email)
    if user is None:
        raise UserNotFound

    if not await PasswordHasherProvider.verify_password(
        plain_password=data.password, hashed_password=user.password
    ):
        raise InvalidCredentials

    try:
        token = await AuthenticationTokenProvider.encode({"user_id": user.id})
        logger.info(f"User {user.id} sign-in token: {token}")
    except Exception as e:
        logger.error(
            f"Error generating token: {e}, Traceback: {traceback.format_exc()}"
        )
        raise TokenGenerationError

    return AuthUserOutDto(token=token)


@auth.get(
    "/user",
    summary="Получение данных пользователя",
    description="Возвращает информацию о пользователе на основе токена авторизации.",
    responses={
        200: {"description": "Успешное получение информации о пользователе."},
        401: {"description": "Отсутствует или недействительный токен авторизации."},
        404: {"description": "Пользователь не найден."},
    },
)
async def get_user_info(user: UserOrm = Depends(get_user)):
    """
    Получение данных о пользователе.

    Параметры
    ----------
    user : UserOrm
        Пользователь, полученный из токена.

    Возвращаемое значение
    ---------------------


    Исключения
    ----------
    UserNotFound
        Выбрасывается, если пользователь не найден.
    """
    departament = None
    departaments = await DepartamentOrm.all()
    for i in departaments:
        for mem in await i.members.all():
            if mem.id == user.id:
                departament = i
                break
    team = None
    teams = await TeamOrm.all()
    for i in teams:
        for mem in await i.members.all():
            if mem.id == user.id:
                team = i
                break

    return {
        "user": user,
        "departament": departament,
        "team": team,
    }
