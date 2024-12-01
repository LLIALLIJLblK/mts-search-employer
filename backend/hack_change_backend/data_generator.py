import asyncio
import random

from hack_change_backend.models import (
    DepartamentOrm,
    TeamOrm,
    UserOrm,
    UserEducationOrm,
    EducationTypeOrm,
    InstituteOrm,
    SpecializationOrm,
    PositionOrm,
)


async def get_or_create_user(first_name, last_name, email, **kwargs):
    """Создает пользователя, если его нет в БД."""
    user = await UserOrm.get_or_none(email=email)
    if user is None:
        user = await UserOrm.create(
            first_name=first_name, last_name=last_name, email=email, **kwargs
        )
        print(f"Создан пользователь: {first_name} {last_name} ({email})")
    else:
        print(f"Пользователь уже существует: {first_name} {last_name} ({email})")
    if user.position is None:
        user_position = await PositionOrm.get(id=random.randint(1, 50))
        user.position = user_position
        await user.save()
    return user


async def get_or_create_department(title, is_direction, director, **kwargs):
    """Создает департамент, если его нет в БД."""
    department = await DepartamentOrm.get_or_none(
        title=title, is_direction=is_direction
    )
    if department is None:
        department = await DepartamentOrm.create(
            title=title, is_direction=is_direction, director=director, **kwargs
        )
        print(f"Создан департамент: {title}")
    else:
        print(f"Департамент уже существует: {title}")
    return department


async def get_or_create_team(title, director, departament, **kwargs):
    """Создает команду, если ее нет в БД."""
    team = await TeamOrm.get_or_none(title=title, departament=departament)
    if team is None:
        team = await TeamOrm.create(
            title=title, director=director, departament=departament, **kwargs
        )
        print(f"Создана команда: {title}")
    else:
        print(f"Команда уже существует: {title}")
    return team


async def get_random_record(model, id_range):
    """Возвращает случайную запись из указанного диапазона ID."""
    record_id = random.randint(*id_range)
    return await model.get_or_none(id=record_id)


async def assign_user_education(user):
    """Добавляет случайное образование пользователю."""
    if await user.education.all().count() > 0:
        print(
            f"Образование уже добавлено для пользователя {user.first_name} {user.last_name}"
        )
        return

    education_type = await get_random_record(EducationTypeOrm, (1, 10))
    institute = await get_random_record(InstituteOrm, (1, 10))
    specialization = await get_random_record(SpecializationOrm, (1, 10))

    if education_type and institute and specialization:
        await UserEducationOrm.create(
            user=user,
            start_year=random.randint(2000, 2015),
            end_year=random.randint(2016, 2023),
            education_type=education_type,
            institute=institute,
            specialization=specialization,
        )
        print(
            f"Добавлено образование для пользователя {user.first_name} {user.last_name}"
        )
    else:
        print(
            f"Не удалось добавить образование для пользователя {user.first_name} {user.last_name}"
        )


async def assign_user_position(user):
    """Добавляет случайную позицию пользователю."""
    if user.position is not None:
        print(
            f"Позиция уже установлена для пользователя {user.first_name} {user.last_name}"
        )
        return

    position = await get_random_record(PositionOrm, (1, 100))
    if position:
        user.position = position
        await user.save()
        print(f"Добавлена позиция для пользователя {user.first_name} {user.last_name}")
    else:
        print(
            f"Не удалось добавить позицию для пользователя {user.first_name} {user.last_name}"
        )


async def seed_database():
    # Создаем пользователей
    director_user = await get_or_create_user(
        first_name="Иван",
        last_name="Иванов",
        email="director@example.com",
        avatar="https://example.com/avatar_director.jpg",
        password="password",
        is_admin=True,
    )

    users = [director_user]

    # Генерация пользователей
    for i in range(1, 21):  # 20 пользователей
        user = await get_or_create_user(
            first_name=f"Имя{i}",
            last_name=f"Фамилия{i}",
            email=f"user{i}@example.com",
            avatar=f"https://example.com/avatar_user{i}.jpg",
            password="password",
        )
        users.append(user)

    # Привязываем образование и позиции
    for user in users:
        await assign_user_education(user)
        await assign_user_position(user)

    # Создаем дирекцию (is_direction=True)
    direction = await get_or_create_department(
        title="Главная Дирекция",
        is_direction=True,
        director=director_user,
    )

    # Генерация департаментов
    departments = []
    for i in range(1, 6):  # 5 департаментов
        department = await get_or_create_department(
            title=f"Департамент {i}",
            is_direction=False,
            director=random.choice(users),  # Случайный пользователь - директор
        )
        departments.append(department)
        department_director = await department.director
        if department_director not in await direction.members.all():
            await direction.members.add(department_director)
            print(
                f"Пользователь {department_director.first_name} добавлен в дирекцию {direction.title}"
            )

    # Генерация команд и их участников
    for department in departments:
        for i in range(1, random.randint(3, 6)):  # От 3 до 5 команд на департамент
            team = await get_or_create_team(
                title=f"Команда {department.title} {i}",
                director=random.choice(users),  # Случайный пользователь - лидер команды
                departament=department,
            )

            # Привязываем участников к команде
            team_members = random.sample(
                users, random.randint(3, 7)
            )  # От 3 до 7 участников
            for member in team_members:
                if member not in await team.members.all():
                    await team.members.add(member)
                    print(
                        f"Пользователь {member.first_name} добавлен в команду {team.title}"
                    )

    print("Данные успешно добавлены в базу данных!")


# if __name__ == "__main__":
#     asyncio.run(seed_database())
