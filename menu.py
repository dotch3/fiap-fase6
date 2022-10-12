from datetime import date, datetime
from uuid import uuid4

from DataManager.manager_db import Connect
from model.person import ChildModel, UserModel
from Utils.env import DB_FILE_PATH
from Utils.menu_utils import (child_options, menu_children, menu_options,
                              menu_txt)

tb_name = "T_PERSON"
id_name = "id"


class DesktopMenu:
    def __init__(self, role=None):
        self.role = role

    def loadData():
        """
        connexion with database"""
        conn = Connect(DB_FILE_PATH)
        return conn.get_all_data(table=tb_name, id_name=id_name)

    def get_all(self):
        """
        Get all data
        """
        conn = Connect(DB_FILE_PATH)
        users = conn.get_all_data(table=tb_name, id_name=id_name)
        for u in users:
            print(u)

    def execute(self):
        # people = PeopleAvlTree()
        # person = UserModel()
        role = "parent"
        stop = False

        while not stop:

            # print(f"logged as {self.session._repository._users}")

            print(
                "\n*******************************************************************************************"
            )
            print(f"\t\t\tMENU")

            print(
                "*******************************************************************************************"
            )
            # Menu
            option = self.show_menu(role)
            # option = input(f"Escolha uma das seguintes opções ").strip()

            if option.isnumeric():
                option = int(option)

            if option == 0:
                stop = True
            elif option == 1:
                # Add person
                print("Insira os dados")
                id = (uuid4().hex,)
                # first_name = input("Nome: ")
                # last_name = input("Sobrenome: ")
                # birthday = input("Aniversario (dd/mm/aaaa): ")
                # age = self.calc_age(birthday)
                # num_cpf = input("CPF: ")
                # num_rg = input("RG: ")
                type_user =   (
                        input(
                            "Categoria: <0> Funcionario, <1>Voluntario, <2> Doador, <3> Atendido, <4>Visitante"
                        )
                    )
                
                children = self.has_children( id)
                fam_income = (input("Ingresso Familiar $R: "))
                phone = (input("Tel.Fixo: "))
                cellphone = (input("Tel.Celular: "))
                created_at = datetime.now().isoformat()
                updated_at = datetime.now().isoformat()

                # if children:
                #     child_array = self.has_children(self, id)
                # update the table with the values # Create the parent first then ask if has children
                try:
                    my_user = UserModel(
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
                    my_user.create_user()

                except Exception as e:
                    print("error:", e)

            elif option == 2:
                print("search by id")
            elif option == 3:
                print("search AVL()")

            else:
                print("Invalid Option ")

    def calc_age(self, date_time_str):

        print(date_time_str)
        print(type(date_time_str))
        birthday = datetime.strptime(date_time_str, "%d/%m/%Y")
        today = date.today()
        age = (
            today.year
            - birthday.year
            - ((today.month, today.day) < (birthday.month, birthday.day))
        )

        return age

    def show_menu(self, role):
        """
        Function to show the menu options
        """
        choice = None
        if role == "parent":
            print(menu_txt)
            choice = input("Enter your choice: ")
            print()

            if choice not in menu_options:
                print("")
        if role == "child":
            print(menu_children)
            choice = input("Enter your choice: ")
            print()

            if choice not in child_options:
                print("")

        return choice

    def has_children(self, parent_id):
        # print(
        #     "\n*******************************************************************************************"
        # )
        # print(f"\t\t\tMENU CHILD")

        # print(
        #     "*******************************************************************************************"
        # )
        role = "child"
        arr_child = []
        self.show_menu(role)
        child_option = input(f"Child: Escolha uma das seguintes opções ").strip()
        print()

        if child_option not in child_options:
            print("")
        elif child_option == 1:
            parent_id = parent_id
            name = input("Nome: ")
            age = input("Idade: ")
            student = input("Estudante?: <0> NAO, <1> SIM")
            employed = input("Empregado?: <0> NAO, <1> SIM")
            date_last_job = input("Data do ultimo emprego (dd/mm/aaaa): ")

            my_child = ChildModel(
                parentId=parent_id,
                name=name,
                age=age,
                student=student,
                employed=employed,
                date_last_job=date_last_job,
            )

            arr_child.append(my_child)
        return arr_child
        # Send to database


if __name__ == "__main__":
    birthday = "14/05/1985"
    r = DesktopMenu()
    age = r.calc_age(birthday)
    print(age)
