import imp
from array import array
from datetime import date, datetime
from random import randint

from faker import Faker
from faker.providers import internet, person

# Menu for testing the services
menu_txt = """
(1) - Add Person
(2) - Search person by id <DATABASE>
(3) - Search person by id <MEMORY>
(4) - Search by ALV 
(5) - Get All
(6) - Create Test Users using Fake
<0> - Exit"""
menu_options = [str(i) for i in range(0, 6)]


menu_children = """
Deseja cadastrar dados dos filhos?\n
(1) - Add Child
<2> - None Child
"""
child_options = [str(i) for i in range(0, 2)]


menu_categoria="""
<0> Funcionario
<1>Voluntario
<2> Doador
<3> Atendido
<4>Visitante
"""


def make_fake_user():
    fake = Faker("pt_BR")
    child_array = [
        # name, age,student,worker,lastdayJob
        ["joao", "20", "student", None, None],
        ["Maria", "11", "student", None, None],
        ["Dolly", "23", None, "employed", datetime.now()],
    ]
    fake_data = {
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


    return fake_data


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
    # children=''.join(str(e)for e in fake_children_json)
    return arr_child

