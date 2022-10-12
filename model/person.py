import json
import sys
from array import array
from datetime import date, datetime
from random import randint

from faker import Faker
from faker.providers import internet, person


class UserModel:
    table_name = "T_PERSON"
    TYPE_USERS = "Funcionario, Voluntario, Doador, Atendido, Visitante"
    #  Uma pessoa pode pertencer a mais de uma categoria, no entanto, os Atendidos não podem ser doadores ou funcionários.

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        birthday: date,
        age: int,
        num_cpf: str,
        num_rg: str,
        type_user: int,
        children: array,
        fam_income: int,
        phone: str,
        cellphone: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.age = age
        self.num_cpf = num_cpf
        self.num_rg = num_rg
        self.type_user = type_user
        self.children = children
        self.fam_income = fam_income
        self.phone = phone
        self.cellphone = cellphone
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"user: {self.id}: {self.first_name} - {self.last_name}. children {self.children}"

    def create_user(
        self,
        id=None,
        first_name=None,
        last_name=None,
        birthday=None,
        age=None,
        num_cpf=None,
        num_rg=None,
        type_user=None,
        children=None,
        fam_income=None,
        phone=None,
        cellphone=None,
        created_at=None,
        updated_at=None,
    ):

        return UserModel(
            id=id,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            age=age,
            num_cpf=num_cpf,
            num_rg=num_rg,
            type_user=type_user,
            children=children,
            fam_income=fam_income,
            phone=phone,
            cellphone=cellphone,
            created_at=created_at,
            updated_at=updated_at,
        )

    @classmethod
    def criar_funcionario(
        cls,
        id=None,
        first_name=None,
        last_name=None,
        birthday=None,
        age=None,
        num_cpf=None,
        num_rg=None,
        type_user=None,
        children=None,
        fam_income=None,
        phone=None,
        cellphone=None,
        created_at=None,
        updated_at=None,
    ):
        """ """
        return UserModel(
            id=id,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            age=age,
            num_cpf=num_cpf,
            num_rg=num_rg,
            type_user=UserModel.TYPE_USERS[0],  # Funcionario
            children=children,
            fam_income=fam_income,
            phone=phone,
            cellphone=cellphone,
            created_at=created_at,
            updated_at=updated_at,
        )


class ChildModel:
    table_name = "T_CHILD"

    def __init__(
        self,
        id: None,
        name: None,
        age: None,
        student: None,
        employed: None,
        date_last_job: None,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.student = student
        self.employed = employed
        self.date_last_job = date_last_job
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f" child: {self.name} - {self.age} "

    def create_children(
        self,
        id=None,
        name=None,
        age=None,
        student=None,
        employed=None,
        date_last_job=None,
        created_at=None,
        updated_at=None,
    ):

        return ChildModel(
            id=id,
            name=name,
            age=age,
            student=student,
            employed=employed,
            date_last_job=date_last_job,
            created_at=created_at,
            updated_at=updated_at,
        )


def make_fake_user():
    fake = Faker("pt_BR")
    child_array = [
        # name, age,student,worker,lastdayJob
        ["joao", "20", "student", None, None],
        ["Maria", "11", "student", None, None],
        ["Dolly", "23", None, "employed", datetime.now()],
    ]
    fake_user_json = {
        "id": fake.random_number(digits=2, fix_len=True),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birthday": fake.date_between_dates(),
        "age": fake.pyint(0, 99, 1),
        "num_cpf": fake.cpf(),
        "num_rg": fake.rg(),
        "type_user": fake.pyint(0, 5, 1),
        "children": make_fake_children(),
        "fam_income": fake.random_number(digits=4, fix_len=True),
        "phone": fake.phone_number(),
        "cellphone": fake.cellphone_number(),
        "created_at": str(datetime.now()),
        "updated_at": str(datetime.now()),
    }

    return fake_user_json


def make_fake_children():
    fake = Faker("pt_BR")
    arr_child = []
    for n in range(randint(0, 4)):  # top 4 children
        fake_children_json = {
            "id": fake.random_number(digits=2, fix_len=True),
            "name": fake.name(),
            "age": fake.pyint(0, 5, 1),
            "student": fake.pybool(),
            "employed": fake.pybool(),
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now()),
        }
        arr_child.append(fake_children_json)
    return arr_child


# print(make_fake_user())

if __name__ == "__main__":
    fake_data = make_fake_user()
    my_user = UserModel(
        id=fake_data["id"],
        first_name=fake_data["first_name"],
        last_name=fake_data["last_name"],
        birthday=fake_data["birthday"],
        age=fake_data["age"],
        num_cpf=fake_data["num_cpf"],
        num_rg=fake_data["num_rg"],
        type_user=fake_data["type_user"],
        children=fake_data["children"],
        fam_income=fake_data["fam_income"],
        phone=fake_data["phone"],
        cellphone=fake_data["cellphone"],
        created_at=fake_data["created_at"],
        updated_at=fake_data["updated_at"],
    )
    print(str(my_user))
