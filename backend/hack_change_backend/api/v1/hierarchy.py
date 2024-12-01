from fastapi import APIRouter

from hack_change_backend.models import DepartamentOrm, TeamOrm

hierarchy = APIRouter()


@hierarchy.get("/")
async def get_organization_structure():
    # Получаем все дирекции
    directions = await DepartamentOrm.filter(is_direction=True).prefetch_related(
        "members",
        "director",
    )

    organization_structure = []

    for direction in directions:
        # Для каждой дирекции собираем информацию о департаментах
        departments = await DepartamentOrm.filter(is_direction=False).prefetch_related(
            "members",
            "director",
        )

        departments_list = []
        for department in departments:
            # Для каждого департамента собираем информацию о командах
            teams = await TeamOrm.filter(departament=department).prefetch_related(
                "members",
                "director",
            )

            teams_list = []
            for team in teams:
                # Для каждой команды собираем данные
                teams_list.append(
                    {
                        "title": team.title,
                        "director": {
                            "first_name": team.director.first_name,
                            "last_name": team.director.last_name,
                            "avatar": team.director.avatar,
                        },
                        "members": [
                            {
                                "first_name": member.first_name,
                                "last_name": member.last_name,
                                "avatar": member.avatar,
                            }
                            for member in team.members
                        ],
                    }
                )

            # Добавляем департамент в список департаментов дирекции
            departments_list.append(
                {
                    "title": department.title,
                    "director": {
                        "first_name": department.director.first_name,
                        "last_name": department.director.last_name,
                        "avatar": department.director.avatar,
                    },
                    "teams": teams_list,
                }
            )
        members = []
        for member in await direction.members.all():
            members.append(
                {
                    "id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "avatar": member.avatar,
                }
            )
        # Добавляем дирекцию в общий список
        organization_structure.append(
            {
                "title": direction.title,
                "director": {
                    "id": direction.director.id,
                    "first_name": direction.director.first_name,
                    "last_name": direction.director.last_name,
                    "avatar": direction.director.avatar,
                },
                "members": members,
                "departments": departments_list,
            }
        )

    return organization_structure
