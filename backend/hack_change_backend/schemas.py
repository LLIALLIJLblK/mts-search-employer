from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SignUpUserDto(BaseModel):
    email: EmailStr
    password: str
    platform_key: str


class SignInUserDto(BaseModel):
    email: EmailStr
    password: str


class AuthUserOutDto(BaseModel):
    token: str


class DataModelDto(BaseModel):
    id: int
    title: str


class UpdateUserDto(BaseModel):
    first_name: Optional[str] = Field(
        None, max_length=255, description="Имя пользователя"
    )
    last_name: Optional[str] = Field(
        None, max_length=255, description="Фамилия пользователя"
    )
    father_name: Optional[str] = Field(
        None, max_length=255, description="Отчество пользователя"
    )
    phone_number: Optional[str] = Field(
        None, max_length=255, description="Номер телефона"
    )
    sex: Optional[bool] = Field(
        None, description="Пол (True - мужской, False - женский)"
    )
    birthday: Optional[datetime] = Field(None, description="Дата рождения")
    date_of_start_work: Optional[datetime] = Field(
        None, description="Дата начала работы"
    )
    about_user: Optional[str] = Field(
        None, max_length=255, description="Информация о пользователе"
    )
    social_link: Optional[str] = Field(
        None, max_length=255, description="Ссылка на соцсети"
    )
    skills_ids: Optional[list[int]] = Field(None, description="Список ID навыков")


class CreateDirectionDto(BaseModel):
    title: str
    director_id: int
    is_direction: bool


class CreateTeamDto(BaseModel):
    title: str
    director_id: int
    departament_id: int


class AdminUpdatePositionTeamDto(BaseModel):
    team_id: int
    position_id: int


class AdminCreatePlatformKeyDto(BaseModel):
    key: str
    team_id: int | None
    position_id: int
    departament_id: int | None


class UserCreateEducationDto(BaseModel):
    start_year: int
    end_year: int
    specialization_id: int
    institute_id: int
    education_type_id: int
