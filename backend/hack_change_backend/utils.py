from hack_change_backend.data.city import city
from hack_change_backend.data.education_type import education_type
from hack_change_backend.data.institute import institute
from hack_change_backend.data.position import position
from hack_change_backend.data.projects import projects
from hack_change_backend.data.skill import skill
from hack_change_backend.data.specialization import specialization
from hack_change_backend.data.work_category import work_category
from hack_change_backend.models import (
    CityOrm,
    EducationTypeOrm,
    InstituteOrm,
    PositionOrm,
    SkillOrm,
    SpecializationOrm,
    WorkCategoryOrm,
    ProjectOrm,
)


async def load_city():
    created = []
    for i in city:
        if not await CityOrm.exists(title=i):
            await CityOrm.create(title=i)
            created.append(i)
    return created


async def load_education_type():
    created = []
    for i in education_type:
        if not await EducationTypeOrm.exists(title=i):
            await EducationTypeOrm.create(title=i)
            created.append(i)
    return created


async def load_institute():
    created = []
    for i in institute:
        if not await InstituteOrm.exists(title=i):
            await InstituteOrm.create(title=i)
            created.append(i)
    return created


async def load_position():
    created = []
    for i in position:
        if not await PositionOrm.exists(title=i):
            await PositionOrm.create(title=i)
            created.append(i)

    return created


async def load_skill():
    created = []
    for i in skill:
        if not await SkillOrm.exists(title=i):
            await SkillOrm.create(title=i)
            created.append(i)

    return created


async def load_specialization():
    created = []
    for i in specialization:
        if not await SpecializationOrm.exists(title=i):
            await SpecializationOrm.create(title=i)
            created.append(i)

    return created


async def load_work_category():
    created = []
    for i in work_category:
        if not await WorkCategoryOrm.exists(title=i):
            await WorkCategoryOrm.create(title=i)
            created.append(i)

    return created


async def load_projects():
    created = []
    for i in projects:
        if not await ProjectOrm.exists(title=i):
            await ProjectOrm.create(title=i)
            created.append(i)

    return created
