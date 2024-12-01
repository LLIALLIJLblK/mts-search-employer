from datetime import datetime

from tortoise import fields

from hack_change_backend.core.abstract import AbstractModel


class CityOrm(AbstractModel):
    """Города - например: Москва, Мурманск"""

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_city"


class PositionOrm(AbstractModel):
    """Позиции (кем работает) - например: Администратор CAM систем, Юрист по таможенному праву"""

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_position"


class SkillOrm(AbstractModel):
    """Навыки - например: Ремонт мототехники, Веб-дизайн"""

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_skill"


class SpecializationOrm(AbstractModel):
    """
    Специализации (та, которую дают после вуза)
    например: Операторское искусство (по видам),
    Комплексное обеспечение информационной безопасности автоматизированных систем
    """

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_specialization"


class InstituteOrm(AbstractModel):
    """
    Институты (где учились)
    например: МГТУ им. Баумана,
    Московский государственный университет имени М.В. Ломоносова
    """

    title: str = fields.CharField(max_length=600)

    class Meta:
        table_name = "hc_institute"


class WorkCategoryOrm(AbstractModel):
    """
    Категории работы
    например: Бытовые услуги, Системное администрирование
    """

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_work_category"


class EducationTypeOrm(AbstractModel):
    """
    Типы образования
    например: Среднее, Магистр
    """

    title: str = fields.CharField(max_length=255)

    class Meta:
        table_name = "hc_education_type"


class UserEducationOrm(AbstractModel):
    start_year: int = fields.IntField()
    end_year: int = fields.IntField()
    specialization: SpecializationOrm = fields.ForeignKeyField("hack.SpecializationOrm")
    institute: InstituteOrm = fields.ForeignKeyField("hack.InstituteOrm")
    education_type: EducationTypeOrm = fields.ForeignKeyField("hack.EducationTypeOrm")

    class Meta:
        table_name = "hc_user_education"


class DepartamentOrm(AbstractModel):
    title: str = fields.CharField(max_length=255)
    director: "UserOrm" = fields.ForeignKeyField(
        "hack.UserOrm",
        related_name="director",
    )
    is_direction: bool = fields.BooleanField(default=False)
    members: list["UserOrm"] = fields.ManyToManyField("hack.UserOrm")


class TeamOrm(AbstractModel):
    title: str = fields.CharField(max_length=255)
    director: "UserOrm" = fields.ForeignKeyField(
        "hack.UserOrm", related_name="team_leader"
    )
    departament: DepartamentOrm = fields.ForeignKeyField("hack.DepartamentOrm")
    members: list["UserOrm"] = fields.ManyToManyField("hack.UserOrm")


class ProjectOrm(AbstractModel):
    title: str = fields.CharField(max_length=255)


class UserOrm(AbstractModel):
    """
    Пользователи
    """

    first_name: str = fields.CharField(max_length=255, null=True)
    last_name: str = fields.CharField(max_length=255, null=True)
    father_name: str = fields.CharField(max_length=255, null=True)

    avatar: str = fields.CharField(max_length=255, null=True)
    phone_number: str = fields.CharField(max_length=255, null=True)
    sex: bool = fields.BooleanField(default=None, null=True)
    birthday: datetime = fields.DatetimeField(null=True)
    date_of_start_work: datetime = fields.DatetimeField(null=True)
    about_user: str = fields.CharField(max_length=255, null=True)
    social_link: str = fields.CharField(max_length=255, null=True)

    is_direction: bool = fields.BooleanField(default=False, null=True)

    email: str = fields.CharField(max_length=255)
    password: str = fields.CharField(max_length=255)
    is_admin: bool = fields.BooleanField(default=False)

    education: list[UserEducationOrm] = fields.ManyToManyField("hack.UserEducationOrm")
    skills: list[SkillOrm] = fields.ManyToManyField("hack.SkillOrm")
    position: PositionOrm = fields.ForeignKeyField("hack.PositionOrm", null=True)
    projects: list[ProjectOrm] = fields.ManyToManyField("hack.ProjectOrm")

    class Meta:
        table_name = "hc_user"


class RegistrationKeyOrm(AbstractModel):
    key: str = fields.CharField(max_length=255)
    position: PositionOrm = fields.ForeignKeyField("hack.PositionOrm")
    team: TeamOrm = fields.ForeignKeyField("hack.TeamOrm", null=True)
    departament: DepartamentOrm = fields.ForeignKeyField(
        "hack.DepartamentOrm", null=True
    )
