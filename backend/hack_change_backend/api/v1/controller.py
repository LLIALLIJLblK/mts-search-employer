import json
import os
import uuid

from fastapi import APIRouter, Request, UploadFile, Depends, HTTPException, File, Form
from pydantic import ValidationError
from tortoise.transactions import in_transaction

from hack_change_backend.api.deps import get_user, get_admin
from hack_change_backend.data.education_type import education_type
from hack_change_backend.data.institute import institute
from hack_change_backend.models import (
    UserOrm,
    SkillOrm,
    DepartamentOrm,
    TeamOrm,
    SpecializationOrm,
    InstituteOrm,
    EducationTypeOrm,
    UserEducationOrm,
    ProjectOrm,
)
from hack_change_backend.schemas import (
    UpdateUserDto,
    CreateDirectionDto,
    CreateTeamDto,
    UserCreateEducationDto,
)

controller = APIRouter()

# @controller.put("/user")
# Путь для сохранения файлов
AVATAR_DIR = "hack_change_backend/static/avatars"

# Проверяем, существует ли папка
os.makedirs(AVATAR_DIR, exist_ok=True)


@controller.put("/user", response_model=dict)
async def update_user(
    update_data: str = Form(...),  # Получаем данные в виде строки
    avatar: UploadFile = File(None),  # Для загрузки файла
    user=Depends(get_user),  # Авторизация и получение текущего пользователя
):
    # Парсинг строки JSON
    try:
        parsed_data = json.loads(update_data)
        update_data_obj = UpdateUserDto(**parsed_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Некорректный JSON формат")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
        # Обработка аватара
    if avatar:
        avatar_filename = f"{user.id}_{avatar.filename}"
        avatar_path = os.path.join(AVATAR_DIR, str(uuid.uuid4()) + avatar_filename)

        with open(avatar_path, "wb") as f:
            f.write(await avatar.read())

        user.avatar = avatar_path.removeprefix("hack_change_backend/")

        # Обновление остальных данных
    async with in_transaction():
        for field, value in update_data_obj.dict(exclude_unset=True).items():
            if field == "skills_ids":
                skills = await SkillOrm.filter(id__in=value)
                await user.skills.clear()
                await user.skills.add(*skills)
            else:
                setattr(user, field, value)
        await user.save()

    return {
        "message": "Пользователь успешно обновлен",
        "avatar_url": user.avatar,
    }


@controller.post("/user/education")
async def create_education(data: UserCreateEducationDto, user=Depends(get_user)):
    spec = await SpecializationOrm.get_or_none(id=data.specialization_id)
    if spec is None:
        raise

    institute = await InstituteOrm.get_or_none(id=data.institute_id)
    if institute is None:
        raise

    education_type = await EducationTypeOrm.get_or_none(id=data.education_type_id)
    if education_type is None:
        raise

    entity = await UserEducationOrm.create(
        start_year=data.start_year,
        end_year=data.end_year,
        specialization=spec,
        institute=institute,
        education_type=education_type,
    )
    await user.education.add(entity)
    return True


@controller.delete("/user/education")
async def delete_education(education_id: int, user=Depends(get_user)):
    education = await UserEducationOrm.get_or_none(id=education_id)
    if education is None:
        raise

    await user.education.delete()
    return True


@controller.post("/user/project")
async def add_project_to_user(project_id: int, user=Depends(get_user)):
    project = await ProjectOrm.get_or_none(id=project_id)
    if project is None:
        raise

    for project in await user.projects.all():
        if project.id == project_id:
            raise
    else:
        await user.projects.add(project)
    return True


@controller.delete("/user/project")
async def delete_project_from_user(project_id: int, user=Depends(get_user)):
    project = await ProjectOrm.get_or_none(id=project_id)
    if project is None:
        raise

    await user.projects.remove(project)
    return True
