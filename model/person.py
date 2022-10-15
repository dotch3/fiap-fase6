import sys
sys.path.insert(0, "/Users/dotch3/Documents/Coding/Fiap/fase6")
import time
from array import array
from datetime import date, datetime
from AVL import AVLTree

start_time = time.time()

# include project's root path
from DataManager.manager_db import Connect
from Utils.env import DB_FILE_PATH
from Utils.menu_utils import make_fake_children, make_fake_user


class UserModel:
    table_name = "T_PERSON"
    id_name="id"
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
        if len(self.children)>0:
            return f"user: {self.id}: {self.first_name} - {self.last_name}. children {self.children[0]}"
        else:
            return f"user: {self.id}: {self.first_name} - {self.last_name}"

    def create_user(my_user):
        my_conn = Connect(DB_FILE_PATH)
        print(my_user.first_name)
        
        print("test children")
        child_aux="my children"
        print(type(my_user.children))
        str_op = 'INSERT INTO  T_PERSON (id, first_name, last_name,birthday,age,num_cpf,num_rg,type_user,children,fam_income,phone,cellphone,created_at,updated_at)'
      
        insert_query = str_op + 'VALUES (\"'+ str(my_user.id)+'\",' +'\"'+ str(my_user.first_name)+'\",' +'\"'+ str(my_user.last_name)+'\",' +'\"'+ str(my_user.birthday)+'\",' +'\"'+ str(my_user.age)+'\",' +'\"'+ str(my_user.num_cpf)+'\",' +'\"'+ str(my_user.num_rg)+'\",' +'\"'+ str(my_user.type_user)+'\",' +'\"'+ str(child_aux)+'\",' +'\"'+ str(my_user.fam_income)+'\",' +'\"'+ str(my_user.phone)+'\",' +'\"'+ str(my_user.cellphone)+'\",' +'\"'+ str(my_user.created_at)+'\",' +'\"'+ str(my_user.updated_at)+'\");'
     
            
        print(insert_query)
        my_conn.insert_register(data_query=insert_query)
    
    @staticmethod
    def get_users():
        table_name = "T_PERSON"
        id_name="id"
        my_conn = Connect(DB_FILE_PATH)
        users = my_conn.get_all_data(table=table_name,id_name=id_name)
        return users
    
    @staticmethod    
    def find_user_database(usr_id):
        table_name = "T_PERSON"
        id_name="id"
        my_conn = Connect(DB_FILE_PATH)
        usr= my_conn.get_item(table=table_name,id_item=usr_id,id_name=id_name)
        # print(usr)
        return usr

    @staticmethod
    def find_user(usr_id):
        table_name = "T_PERSON"
        id_name="id"
        found=None
        my_conn = Connect(DB_FILE_PATH)
        dict_usr= my_conn.get_all_data(table=table_name,id_name=id_name)
        # print(dict_usr)
        for item in dict_usr:
            if item["id"]==usr_id:
                found=item
        return found

    @staticmethod
    def sort_avl():
        Tree = AVLTree()
        dict_data=UserModel.get_users()
        root= None
        key="id"
        dict_len=len(dict_data)
        
        if dict_len > 1:
            for item in dict_data:
                root=Tree.insert(root,int(item[key]))
        Tree.preOrder(root)


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
        id:None,
        parent_id: None,
        name: None,
        age: None,
        student: None,
        employed: None,
        date_last_job: None,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.parent_id=parent_id
        self.name = name
        self.age = age
        self.student = student
        self.employed = employed
        self.date_last_job = date_last_job
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f" child: {self.name} - {self.age} <> Parent: {self.parent_id}"

    def create_children(
        self,
        id=None,
        parent_id=None,
        name=None,
        age=None,
        student=None,
        employed=None,
        date_last_job=None,
        created_at=str(datetime.now()),
        updated_at=str(datetime.now()),
    ):

        return ChildModel(
            id=id,
            parent_id=parent_id,
            name=name,
            age=age,
            student=student,
            employed=employed,
            date_last_job=date_last_job,
            created_at=created_at,
            updated_at=updated_at,
        )

# print(make_fake_user())

if __name__ == "__main__":
    import time
    start_time = time.time()
    print("\n*****_____STATS____*****\n")


    # for f in range (0,5):
        
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
    # print(str(my_user))
    
    my_user.create_user()    
    print("\nCREATE USER: --- %s seconds ---" % (time.time() - start_time))
    
    #  
    print(my_user.get_users())
    print(f"\nGET ALL USERS:--- %s seconds ---" % (time.time() - start_time))
    
    #
    print(f"found database {my_user.find_user_database(223)}")
    print("\nFIND_IN DATABASE:--- %s seconds ---\n" % (time.time() - start_time))
    
    #
    print(f"found memmory {my_user.find_user(usr_id=223)}")
    print("\nFIND_IN_MEMORY:--- %s seconds ---\n" % (time.time() - start_time))
    
     #
    print(f"AVL() {my_user.sort_avl()}")
    print("\nSORT DATA AVL:--- %s seconds ---\n" % (time.time() - start_time))
    


    print("FINAL STATS:--- %s seconds ---" % (time.time() - start_time))