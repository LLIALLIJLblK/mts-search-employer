from fastapi import FastAPI, Query, HTTPException, APIRouter
from typing import Optional, List
from datetime import datetime
from tortoise.expressions import Q
from tortoise.contrib.pydantic import pydantic_model_creator

from hack_change_backend.models import UserOrm

filter_controller = APIRouter()

# Pydantic модель для вывода данных пользователя
UserOut = pydantic_model_creator(UserOrm, name="UserOut", exclude=("password",))
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserOut(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    father_name: Optional[str]
    email: str
    phone_number: Optional[str]
    sex: Optional[bool]
    birthday: Optional[datetime]
    date_of_start_work: Optional[datetime]
    about_user: Optional[str]
    social_link: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True


@filter_controller.get("/users/search", response_model=List[UserOut])
async def search_users(
    name: Optional[str] = Query(
        None, description="Подстрока имени, фамилии или отчества"
    ),
    institute_ids: Optional[List[int]] = Query(
        None, description="ID учебных заведений"
    ),
    birth_year: Optional[int] = Query(None, description="Год рождения"),
    birth_date: Optional[str] = Query(
        None, description="Полная дата рождения (YYYY-MM-DD)"
    ),
    age_category: Optional[str] = Query(
        None, description="Категория возраста (например, 0-15, 15-30, X-Y)"
    ),
    work_experience: Optional[str] = Query(
        None, description="Стаж работы в годах (например, 0-5, 10-15, X-Y)"
    ),
    email: Optional[str] = Query(None, description="Подстрока почты"),
    phone_number: Optional[str] = Query(None, description="Подстрока номера телефона"),
    specialization_id: Optional[int] = Query(None, description="ID специализации"),
    project_ids: Optional[List[int]] = Query(None, description="ID проектов"),
    skill_ids: Optional[List[int]] = Query(None, description="ID навыков"),
    about: Optional[str] = Query(None, description="Подстрока в поле 'about'"),
    social: Optional[str] = Query(None, description="Подстрока ссылки соцсети"),
    sex: Optional[bool] = Query(
        None, description="Пол (True для мужчины, False для женщины)"
    ),
):
    filters = Q()

    # Фильтры
    if name:
        filters &= (
            Q(first_name__icontains=name)
            | Q(last_name__icontains=name)
            | Q(father_name__icontains=name)
        )
    if institute_ids:
        filters &= Q(education__institute_id__in=institute_ids)
    if birth_year:
        filters &= Q(birthday__year=birth_year)
    if birth_date:
        try:
            date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            filters &= Q(birthday=date)
        except ValueError:
            raise HTTPException(
                status_code=400, detail="Неверный формат даты. Используйте YYYY-MM-DD."
            )
    if age_category:
        try:
            if "-" in age_category:
                min_age, max_age = map(int, age_category.split("-"))
                current_year = datetime.now().year
                start_date = datetime(current_year - max_age, 1, 1)
                end_date = datetime(current_year - min_age, 12, 31)
                filters &= (
                    Q(birthday__lte=end_date)
                    & Q(birthday__gte=start_date)
                    & ~Q(birthday=None)
                )
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Неверный формат категории возраста. Используйте X-Y.",
            )

    if work_experience:
        try:
            if "-" in work_experience:
                min_exp, max_exp = map(int, work_experience.split("-"))
                current_year = datetime.now().year
                filters &= Q(
                    date_of_start_work__year__gte=current_year - max_exp,
                    date_of_start_work__year__lte=current_year - min_exp,
                )
        except ValueError:
            raise HTTPException(
                status_code=400, detail="Неверный формат стажа работы. Используйте X-Y."
            )
    if email:
        filters &= Q(email__icontains=email)
    if phone_number:
        filters &= Q(phone_number__icontains=phone_number)
    if specialization_id:
        filters &= Q(education__specialization_id=specialization_id)
    if project_ids:
        filters &= Q(projects__id__in=project_ids)
    if skill_ids:
        filters &= Q(skills__id__in=skill_ids)
    if about:
        filters &= Q(about_user__icontains=about)
    if social:
        filters &= Q(social_link__icontains=social)
    if sex is not None:
        filters &= Q(sex=sex)

    # Выполняем запрос и сериализуем результаты
    # Выполняем запрос
    queryset = await UserOrm.filter(filters).distinct()
    users = [UserOut.from_orm(user) for user in queryset]
    return users
