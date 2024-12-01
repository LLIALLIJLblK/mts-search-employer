from fastapi import APIRouter, Depends

from hack_change_backend.api.deps import get_admin
from hack_change_backend.data.position import position
from hack_change_backend.models import (
    DepartamentOrm,
    UserOrm,
    TeamOrm,
    PositionOrm,
    RegistrationKeyOrm,
)
from hack_change_backend.schemas import (
    CreateTeamDto,
    CreateDirectionDto,
    AdminUpdatePositionTeamDto,
    AdminCreatePlatformKeyDto,
)

admin = APIRouter()


@admin.post("/departament")
async def create_departament(
    data: CreateDirectionDto, admin: UserOrm = Depends(get_admin)
):
    director = UserOrm.get_or_none(id=data.director_id)
    if director is None:
        raise

    departament = await DepartamentOrm.create(
        title=data.title, director=director, is_direction=data.is_direction
    )
    return departament


@admin.post("/team")
async def create_team(data: CreateTeamDto, admin: UserOrm = Depends(get_admin)):
    departament = await DepartamentOrm.get_or_none(id=data.departament_id)
    if departament is None:
        raise

    director = UserOrm.get_or_none(id=data.director_id)
    if director is None:
        raise

    team = await TeamOrm.create(
        title=data.title, departament=departament, director=director
    )
    return team


@admin.put("/user")
async def update_user_position_and_team(
    data: AdminUpdatePositionTeamDto,
    user_id: int,
    admin_user: UserOrm = Depends(get_admin),
):
    entity = await UserOrm.get_or_none(id=user_id)
    if entity is None:
        raise

    user_position = await PositionOrm.get_or_none(id=data.position_id)
    if user_position is None:
        raise

    user_team = await TeamOrm.get_or_none(id=data.team_id)
    if user_team is None:
        raise
    print(user_position.title, user_team.title)
    us_pos = await entity.position.get()
    if us_pos.id == user_position.id:
        print("ok")
    else:
        entity.position = user_position

    for member in await user_team.members.all():
        if member.id == entity.id:
            print("ok")
            break
    else:
        await user_team.members.add(entity)

    await entity.save()
    return entity


@admin.post("/platform-key")
async def create_platform_key(
    data: AdminCreatePlatformKeyDto, admin: UserOrm = Depends(get_admin)
):
    if await RegistrationKeyOrm.exists(key=data.key):
        raise
    if data.departament_id:
        key = await RegistrationKeyOrm.create(
            key=data.key,
            position=await PositionOrm.get(id=data.position_id),
            departament=await DepartamentOrm.get(id=data.departament_id),
        )
    else:
        key = await RegistrationKeyOrm.create(
            key=data.key,
            position=await PositionOrm.get(id=data.position_id),
            team=await TeamOrm.get(id=data.team_id),
        )
    return key.key
