from fastapi import APIRouter, Query, HTTPException
from typing import List

from hack_change_backend.core.exceptions import (
    CityNotFound,
    PositionNotFound,
    SkillNotFound,
    SpecializationNotFound,
    InstituteNotFound,
    WorkCategoryNotFound,
    EducationTypeNotFound,
)
from hack_change_backend.models import (
    CityOrm,
    PositionOrm,
    SkillOrm,
    SpecializationOrm,
    InstituteOrm,
    WorkCategoryOrm,
    EducationTypeOrm,
    ProjectOrm,
)
from hack_change_backend.schemas import DataModelDto

data_controller = APIRouter()


@data_controller.get(
    "/city",
    response_model=List[DataModelDto],
    summary="Получить все города",
    description="Возвращает список всех городов.",
    responses={200: {"description": "Список городов успешно получен."}},
)
async def get_all_cities() -> List[DataModelDto]:
    """
    Получить все города.

    Возвращает список всех городов.

    Returns
    -------
    List[DataModelDto]
        Список городов, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await CityOrm.all()]


@data_controller.get(
    "/city/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация городов",
    description="Возвращает список городов, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список городов успешно отфильтрован."}},
)
async def get_city_filter(query: str = Query(..., min_length=1)) -> List[DataModelDto]:
    """
    Фильтрация городов по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации городов (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список городов, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await CityOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/city/{city_id}",
    response_model=DataModelDto,
    summary="Получить город по ID",
    description="Возвращает информацию о городе по его ID.",
    responses={
        200: {"description": "Информация о городе успешно получена."},
        404: {"description": "Город не найден."},
    },
)
async def get_city_by_id(city_id: int) -> DataModelDto:
    """
    Получить информацию о городе по его ID.

    Параметры
    ---------
    city_id : int
        Уникальный идентификатор города.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий город.

    Raises
    ------
    CityNotFound
        Если город с данным ID не найден.
    """
    city = await CityOrm.get_or_none(id=city_id)
    if city is None:
        raise CityNotFound
    return DataModelDto(id=city.id, title=city.title)


@data_controller.get(
    "/position",
    response_model=List[DataModelDto],
    summary="Получить все должности",
    description="Возвращает список всех должностей.",
    responses={200: {"description": "Список должностей успешно получен."}},
)
async def get_all_positions() -> List[DataModelDto]:
    """
    Получить все должности.

    Возвращает список всех должностей.

    Returns
    -------
    List[DataModelDto]
        Список должностей, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await PositionOrm.all()]


@data_controller.get(
    "/position/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация должностей",
    description="Возвращает список должностей, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список должностей успешно отфильтрован."}},
)
async def get_position_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация должностей по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации должностей (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список должностей, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await PositionOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/position/{position_id}",
    response_model=DataModelDto,
    summary="Получить должность по ID",
    description="Возвращает информацию о должности по её ID.",
    responses={
        200: {"description": "Информация о должности успешно получена."},
        404: {"description": "Должность не найдена."},
    },
)
async def get_position_by_id(position_id: int) -> DataModelDto:
    """
    Получить информацию о должности по её ID.

    Параметры
    ---------
    position_id : int
        Уникальный идентификатор должности.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий должность.

    Raises
    ------
    PositionNotFound
        Если должность с данным ID не найдена.
    """
    position = await PositionOrm.get_or_none(id=position_id)
    if position is None:
        raise PositionNotFound
    return DataModelDto(id=position.id, title=position.title)


@data_controller.get(
    "/skill",
    response_model=List[DataModelDto],
    summary="Получить все навыки",
    description="Возвращает список всех навыков.",
    responses={200: {"description": "Список навыков успешно получен."}},
)
async def get_all_skills() -> List[DataModelDto]:
    """
    Получить все навыки.

    Возвращает список всех навыков.

    Returns
    -------
    List[DataModelDto]
        Список навыков, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await SkillOrm.all()]


@data_controller.get(
    "/skill/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация навыков",
    description="Возвращает список навыков, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список навыков успешно отфильтрован."}},
)
async def get_skill_filter(query: str = Query(..., min_length=1)) -> List[DataModelDto]:
    """
    Фильтрация навыков по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации навыков (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список навыков, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await SkillOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/skill/{skill_id}",
    response_model=DataModelDto,
    summary="Получить навык по ID",
    description="Возвращает информацию о навыке по его ID.",
    responses={
        200: {"description": "Информация о навыке успешно получена."},
        404: {"description": "Навык не найден."},
    },
)
async def get_skill_by_id(skill_id: int) -> DataModelDto:
    """
    Получить информацию о навыке по его ID.

    Параметры
    ---------
    skill_id : int
        Уникальный идентификатор навыка.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий навык.

    Raises
    ------
    SkillNotFound
        Если навык с данным ID не найден.
    """
    skill = await SkillOrm.get_or_none(id=skill_id)
    if skill is None:
        raise SkillNotFound
    return DataModelDto(id=skill.id, title=skill.title)


@data_controller.get(
    "/specialization",
    response_model=List[DataModelDto],
    summary="Получить все специализации",
    description="Возвращает список всех специализаций.",
    responses={200: {"description": "Список специализаций успешно получен."}},
)
async def get_all_specializations() -> List[DataModelDto]:
    """
    Получить все специализации.

    Возвращает список всех специализаций.

    Returns
    -------
    List[DataModelDto]
        Список специализаций, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await SpecializationOrm.all()]


@data_controller.get(
    "/specialization/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация специализаций",
    description="Возвращает список специализаций, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список специализаций успешно отфильтрован."}},
)
async def get_specialization_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация специализаций по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации специализаций (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список специализаций, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await SpecializationOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/specialization/{specialization_id}",
    response_model=DataModelDto,
    summary="Получить специализацию по ID",
    description="Возвращает информацию о специализации по её ID.",
    responses={
        200: {"description": "Информация о специализации успешно получена."},
        404: {"description": "Специализация не найдена."},
    },
)
async def get_specialization_by_id(specialization_id: int) -> DataModelDto:
    """
    Получить информацию о специализации по её ID.

    Параметры
    ---------
    specialization_id : int
        Уникальный идентификатор специализации.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий специализацию.

    Raises
    ------
    SpecializationNotFound
        Если специализация с данным ID не найдена.
    """
    specialization = await SpecializationOrm.get_or_none(id=specialization_id)
    if specialization is None:
        raise SpecializationNotFound
    return DataModelDto(id=specialization.id, title=specialization.title)


@data_controller.get(
    "/institute",
    response_model=List[DataModelDto],
    summary="Получить все институты",
    description="Возвращает список всех институтов.",
    responses={200: {"description": "Список институтов успешно получен."}},
)
async def get_all_institutes() -> List[DataModelDto]:
    """
    Получить все институты.

    Возвращает список всех институтов.

    Returns
    -------
    List[DataModelDto]
        Список институтов, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await InstituteOrm.all()]


@data_controller.get(
    "/institute/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация институтов",
    description="Возвращает список институтов, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список институтов успешно отфильтрован."}},
)
async def get_institute_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация институтов по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации институтов (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список институтов, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await InstituteOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/institute/{institute_id}",
    response_model=DataModelDto,
    summary="Получить институт по ID",
    description="Возвращает информацию о институте по его ID.",
    responses={
        200: {"description": "Информация о институте успешно получена."},
        404: {"description": "Институт не найден."},
    },
)
async def get_institute_by_id(institute_id: int) -> DataModelDto:
    """
    Получить информацию о институте по его ID.

    Параметры
    ---------
    institute_id : int
        Уникальный идентификатор института.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий институт.

    Raises
    ------
    InstituteNotFound
        Если институт с данным ID не найден.
    """
    institute = await InstituteOrm.get_or_none(id=institute_id)
    if institute is None:
        raise InstituteNotFound
    return DataModelDto(id=institute.id, title=institute.title)


@data_controller.get(
    "/work_category",
    response_model=List[DataModelDto],
    summary="Получить все категории работы",
    description="Возвращает список всех категорий работы.",
    responses={200: {"description": "Список категорий работы успешно получен."}},
)
async def get_all_work_categories() -> List[DataModelDto]:
    """
    Получить все категории работы.

    Возвращает список всех категорий работы.

    Returns
    -------
    List[DataModelDto]
        Список категорий работы, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await WorkCategoryOrm.all()]


@data_controller.get(
    "/work_category/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация категорий работы",
    description="Возвращает список категорий работы, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список категорий работы успешно отфильтрован."}},
)
async def get_work_category_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация категорий работы по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации категорий работы (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список категорий работы, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await WorkCategoryOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/work_category/{work_category_id}",
    response_model=DataModelDto,
    summary="Получить категорию работы по ID",
    description="Возвращает информацию о категории работы по её ID.",
    responses={
        200: {"description": "Информация о категории работы успешно получена."},
        404: {"description": "Категория работы не найдена."},
    },
)
async def get_work_category_by_id(work_category_id: int) -> DataModelDto:
    """
    Получить информацию о категории работы по её ID.

    Параметры
    ---------
    work_category_id : int
        Уникальный идентификатор категории работы.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий категорию работы.

    Raises
    ------
    WorkCategoryNotFound
        Если категория работы с данным ID не найдена.
    """
    work_category = await WorkCategoryOrm.get_or_none(id=work_category_id)
    if work_category is None:
        raise WorkCategoryNotFound
    return DataModelDto(id=work_category.id, title=work_category.title)


@data_controller.get(
    "/education_type",
    response_model=List[DataModelDto],
    summary="Получить все типы образования",
    description="Возвращает список всех типов образования.",
    responses={200: {"description": "Список типов образования успешно получен."}},
)
async def get_all_education_types() -> List[DataModelDto]:
    """
    Получить все типы образования.

    Возвращает список всех типов образования.

    Returns
    -------
    List[DataModelDto]
        Список типов образования, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await EducationTypeOrm.all()]


@data_controller.get(
    "/education_type/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация типов образования",
    description="Возвращает список типов образования, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список типов образования успешно отфильтрован."}},
)
async def get_education_type_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация типов образования по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации типов образования (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список типов образования, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await EducationTypeOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/education_type/{education_type_id}",
    response_model=DataModelDto,
    summary="Получить тип образования по ID",
    description="Возвращает информацию о типе образования по его ID.",
    responses={
        200: {"description": "Информация о типе образования успешно получена."},
        404: {"description": "Тип образования не найден."},
    },
)
async def get_education_type_by_id(education_type_id: int) -> DataModelDto:
    """
    Получить информацию о типе образования по его ID.

    Параметры
    ---------
    education_type_id : int
        Уникальный идентификатор типа образования.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий тип образования.

    Raises
    ------
    EducationTypeNotFound
        Если тип образования с данным ID не найден.
    """
    education_type = await EducationTypeOrm.get_or_none(id=education_type_id)
    if education_type is None:
        raise EducationTypeNotFound
    return DataModelDto(id=education_type.id, title=education_type.title)


@data_controller.get(
    "/projects",
    response_model=List[DataModelDto],
    summary="Получить все проекты",
    description="Возвращает список всех проекты.",
    responses={200: {"description": "Список проекты успешно получен."}},
)
async def get_all_projects() -> List[DataModelDto]:
    """
    Получить все типы проекты.

    Возвращает список всех проектов.

    Returns
    -------
    List[DataModelDto]
        Список проекты, представленный в виде объектов DataModelDto.
    """
    return [DataModelDto(id=i.id, title=i.title) for i in await ProjectOrm.all()]


@data_controller.get(
    "/projects/filter",
    response_model=List[DataModelDto],
    summary="Фильтрация проектов",
    description="Возвращает список проектов, содержащих заданный запрос в названии.",
    responses={200: {"description": "Список проектов успешно отфильтрован."}},
)
async def get_projects_filter(
    query: str = Query(..., min_length=1)
) -> List[DataModelDto]:
    """
    Фильтрация проектов по названию.

    Параметры
    ---------
    query : str
        Запрос для фильтрации проектов (минимальная длина - 1 символ).

    Returns
    -------
    List[DataModelDto]
        Список проектов, содержащих заданный запрос в названии.
    """
    return [
        DataModelDto(id=i.id, title=i.title)
        for i in await ProjectOrm.filter(title__icontains=query).all()
    ]


@data_controller.get(
    "/projects/{projects_type_id}",
    response_model=DataModelDto,
    summary="Получить проект по ID",
    description="Возвращает информацию о проекте по его ID.",
    responses={
        200: {"description": "Информация о проекте успешно получена."},
        404: {"description": "Проект не найден."},
    },
)
async def get_project_by_id(projects_type_id: int) -> DataModelDto:
    """
    Получить информацию о типе образования по его ID.

    Параметры
    ---------
    projects_type_id : int
        Уникальный идентификатор проекта.

    Returns
    -------
    DataModelDto
        Объект DataModelDto, представляющий проект

    Raises
    ------
    EducationTypeNotFound
        Если проект с данным ID не найден.
    """
    education_type = await ProjectOrm.get_or_none(id=projects_type_id)
    if education_type is None:
        raise EducationTypeNotFound
    return DataModelDto(id=education_type.id, title=education_type.title)
