from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    status_code = 500
    message = ""
    code: int = 0

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail={"detail": self.message, "code": self.code},
        )

    @classmethod
    def get_dict(cls):
        return {"detail": cls.message}


# Additional Errors


class EmailAlreadyExists(BaseHTTPException):  # Usage: raise EmailAlreadyExists
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Email already exists"
    code = 1002


class InvalidCredentials(BaseHTTPException):  # Usage: raise InvalidCredentials
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid email or password"
    code = 1003


class UserNotFound(BaseHTTPException):  # Usage: raise UserNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "User not found"
    code = 1004


class TokenGenerationError(BaseHTTPException):  # Usage: raise TokenGenerationError
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Error generating authentication token"
    code = 1005


class InvalidRequestData(BaseHTTPException):  # Usage: raise InvalidRequestData
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Invalid request data"
    code = 1006


class PasswordHashingError(BaseHTTPException):  # Usage: raise PasswordHashingError
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Error hashing the password"
    code = 1007


class TransactionError(BaseHTTPException):  # Usage: raise TransactionError
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Transaction error"
    code = 1008


class CityNotFound(BaseHTTPException):  # Usage: raise CityNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "City not found"
    code = 1009


class PositionNotFound(BaseHTTPException):  # Usage: raise PositionNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Position not found"
    code = 1010


class SkillNotFound(BaseHTTPException):  # Usage: raise SkillNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Skill not found"
    code = 1011


class SpecializationNotFound(BaseHTTPException):  # Usage: raise SpecializationNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Specialization not found"
    code = 1012


class InstituteNotFound(BaseHTTPException):  # Usage: raise InstituteNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Institute not found"
    code = 1013


class WorkCategoryNotFound(BaseHTTPException):  # Usage: raise WorkCategoryNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Work Category not found"
    code = 1014


class EducationTypeNotFound(BaseHTTPException):  # Usage: raise EducationTypeNotFound
    status_code = status.HTTP_404_NOT_FOUND
    message = "Education Type Category not found"
    code = 1015


class InvalidPlatformCredentials(BaseHTTPException):  # Usage: raise InvalidCredentials
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid platform key"
    code = 1016


# Ошибки
class TokenMissingError(BaseHTTPException):  # Usage: raise TokenMissingError
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Отсутствует заголовок авторизации"
    code = 2001


class TokenDecodeError(BaseHTTPException):  # Usage: raise TokenDecodeError
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Ошибка декодирования токена"
    code = 2002


class AdminPrivilegesRequired(
    BaseHTTPException
):  # Usage: raise AdminPrivilegesRequired
    status_code = status.HTTP_403_FORBIDDEN
    message = "Необходимы привилегии администратора"
    code = 2003
