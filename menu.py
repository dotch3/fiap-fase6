from datetime import date, datetime
from random import randint
from uuid import uuid4

from AVL import AVLTree
from DataManager.manager_db import Connect
from model.person import ChildModel, UserModel
from Utils.env import DB_FILE_PATH
from Utils.menu_utils import (child_options, make_fake_children,
                              make_fake_user, menu_children, menu_options,
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
                id = input("ID:")
                first_name = input("Nome: ")
                last_name = input("Sobrenome: ")
                birthday = input("Aniversario (dd/mm/aaaa): ")
                age = self.calc_age(birthday)
                num_cpf = input("CPF: ")
                num_rg = input("RG: ")
                type_user =   (
                        input(
                            "Categoria:\n <0>Funcionario\n <1>Voluntario\n <2> Doador\n <3> Atendido\n <4>Visitante\n"
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
                print("search by id <DATABASE>")
                usr_id=input("Enter the user id to find:")
                
                my_usr=UserModel.find_user_database(usr_id=usr_id)
                if my_usr:
                    print(f"\nFound {my_usr}\n")
                else:
                    print(f"\nNot found user with id: {usr_id}")
            elif option == 3:
                print("search by id <MEMORY>")
                usr_id=input("Enter the user id to find:")
                my_usr=UserModel.find_user(usr_id=usr_id)
                if my_usr:
                    print(f"\nFound {my_usr}\n")
                else:
                    print(f"\nNot found user with id: {usr_id}")
            elif option == 4:
                print("search AVL()")
                Tree = AVLTree()
                dict_data=UserModel.get_users()
                root= None
                key="id"
                dict_len=len(dict_data)

                if dict_len > 1:
                    for item in dict_data:
                        root=Tree.insert(root,int(item[key]))
                Tree.preOrder(root)
                print("\nALV end")
            elif option == 5:
                print("Get All")
                users=UserModel.get_users()
                for i in users:
                    print(f"{i['id']} {i['first_name']} {i['last_name']}\n")
                    
            elif option == 6:
                print("Create using Fake")
                qty=input("How many users I will create? ")
                print(f"to create: {qty}")
                for i in range(int(qty)):
                    print(f"user {i}")
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
                    my_user.create_user()    
                # print(my_user.get_users())
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
        return choice

    def has_children(self, parent_id):
        arr_child = []
        print(menu_children)
        child_option = input("Enter your choice: ").strip()

        # print()
        if child_option.isnumeric():
             child_option = int(child_option)
             
             
        if child_option == 0:
             print("")
        elif child_option == 1:
            parent_id = parent_id
            print("****************************\n")
            name = input("Nome (child): ")
            age = input("Idade: ")
            student = input("Estudante?:\n \t<0> NAO\n,\t <1> SIM\n")
            employed = input("Empregado?:\n \t<0> NAO\n, \t<1> SIM\n")
            date_last_job = input("Data do ultimo emprego (dd/mm/aaaa): ")

            my_child = ChildModel(
                id=(uuid4().hex),
                parent_id=parent_id,
                name=name,
                age=age,
                student=student,
                employed=employed,
                date_last_job=date_last_job,
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat()
            )

            arr_child.append(my_child)
        else:
            print ("no childs to add")
        return arr_child
        # Send to database
    
if __name__ == "__main__":
    birthday = "14/05/1985"
    r = DesktopMenu()
    age = r.calc_age(birthday)
    print(age)
