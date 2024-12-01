import traceback

from fastapi import Header, Depends

from hack_change_backend.core.exceptions import (
    TokenMissingError,
    TokenDecodeError,
    UserNotFound,
    AdminPrivilegesRequired,
)
from hack_change_backend.core.logger import logger
from hack_change_backend.core.secutity import AuthenticationTokenProvider
from hack_change_backend.models import UserOrm


# Функции авторизации
async def get_auth_header(x_auth: str = Header(...)):
    """
    Получение заголовка авторизации.

    Параметры
    ----------
    x_auth : str
        Заголовок авторизации.

    Возвращаемое значение
    ---------------------
    str
        Токен авторизации.

    Исключения
    ----------
    TokenMissingError
        Выбрасывается, если заголовок авторизации отсутствует.
    """
    if x_auth is None:
        raise TokenMissingError

    return x_auth


async def get_user(token: str = Depends(get_auth_header)):
    """
    Получение пользователя по токену.

    Параметры
    ----------
    token : str
        Токен авторизации.

    Возвращаемое значение
    ---------------------
    UserOrm
        Пользователь, связанный с данным токеном.

    Исключения
    ----------
    TokenDecodeError
        Выбрасывается, если произошла ошибка при декодировании токена.
    UserNotFound
        Выбрасывается, если пользователь не найден.
    """
    try:
        payload = await AuthenticationTokenProvider.decode(jwt_token=token)
    except Exception as e:
        logger.error(f"Error decode token: {e}, Traceback: {traceback.format_exc()}")
        raise TokenDecodeError
    user_id = payload.get("user_id")
    if user_id is None:
        raise UserNotFound
    user = await UserOrm.get_or_none(id=user_id)
    if user is None:
        raise UserNotFound

    return user


async def get_admin(user: UserOrm = Depends(get_user)):
    """
    Проверка привилегий администратора.

    Параметры
    ----------
    user : UserOrm
        Пользователь, полученный из токена.

    Возвращаемое значение
    ---------------------
    UserOrm
        Пользователь с правами администратора.

    Исключения
    ----------
    AdminPrivilegesRequired
        Выбрасывается, если у пользователя отсутствуют права администратора.
    """
    if user.is_admin:
        return user
    raise AdminPrivilegesRequired
