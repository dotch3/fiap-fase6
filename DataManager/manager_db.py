import json
import re
import sqlite3
import sys

# include project's root path
sys.path.insert(0, "/Users/dotch3/Documents/Coding/Fiap/fase6")
from Utils.env import DB_FILE_PATH


class Connect(object):

    # db_file_path = '../Database/db_cerv.sqlite'

    def __init__(self, db_file_path) -> None:
        self.db_file_path = DB_FILE_PATH

    def create_connexion(self, db_file_path):
        try:
            self.conn = sqlite3.connect(db_file_path)

            # test connexion
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT SQLITE_VERSION()")
            self.data = self.cursor.fetchone()
            # imprimindo a versão do SQLite
            print(f"SQLite version: {self.data}")

            return self.conn
        except sqlite3.Error as e:
            print(f"Erro ao conectar o banco: {e}")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_connexion(self):
        if self.conn:
            self.conn.close()
            print("connexion fechada.")

    # Function to make the test connection using parameters
    def run_query_test(self, data_query):
        conn = self.create_connexion(self.db_file_path)
        cursor = conn.cursor()
        try:
            cursor.execute(data_query)
            for linha in cursor.fetchall():
                print(linha)

            self.close_connexion()
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")

    # Function to make the test connection using parameters
    def run_query__return_json(self, data_query):
        conn = self.create_connexion(self.db_file_path)
        conn.row_factory = (
            sqlite3.Row
        )  # This enables column access by name: row['column_name']
        cursor = conn.cursor()
        try:
            cursor.execute(data_query)
            rows = cursor.fetchall()
            print(json.dumps([dict(ix) for ix in rows]))  # CREATE JSON

            self.close_connexion()
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")

    def get_all_data(self, table=None, id_name=None):
        print(f'get_all_data for table: "{table}" ')
        # remove the "TC"form table name
        if id_name:
            sql = f"SELECT * FROM {table} ORDER BY {id_name};"
        else:
            sql = f"SELECT * FROM {table};"
        # print(sql)
        # In order to jsonify the dictionary, is needed to call it inside the app_context

        conn = self.create_connexion(self.db_file_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql)

        ITEMS = cursor.fetchall()

        dict_items = json.dumps([dict(ix) for ix in ITEMS])
        # print(dict_items)
        dict_items = json.loads(dict_items)

        # print(dict_items)
        # qtd = len(dict_items)

        # print("End of get_data_service ")
        return dict_items

    def get_item(self, table=None, id_item=None, id_name=None):
        print(f'get_id for table: "{table}" ')
        if id_name:
            sql = (
                f"SELECT * FROM {table}  WHERE {id_name}={id_item}  ORDER BY {id_name};"
            )
        else:
            sql = f"SELECT * FROM {table}  WHERE {id_name}={id_item};"
        print(sql)
        # In order to jsonify the dictionary, is needed to call it inside the app_context

        conn = self.create_connexion(self.db_file_path)
        try:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(sql)
            # row = row.fetchone()
            # print(row)
            ITEMS = cursor.fetchall()
            dict_items = json.dumps([dict(ix) for ix in ITEMS])
            # print(dict_items)
            dict_items = json.loads(dict_items)
           
            return dict_items
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")

    def delete_item(self, table, id_item=None, id_name=None):
        print("Manager:delete_item")
        try:
            sql = f"SELECT * FROM {table}  WHERE {id_name}={id_item};"
            print(sql)
            conn = self.create_connexion(self.db_file_path)
            cursor = conn.cursor()
            row = cursor.execute(sql).fetchone()

            print(row)
            if row:
                sql = f"DELETE FROM {table}  WHERE {id_name}={id_item};"
                cursor.execute(sql)
                # gravando no bd
                self.commit_db()
                print("Registro %d excluído com sucesso." % id_item)
                return True
            else:
                print("Não existe o record com o código informado.")
                return False
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")
            return False

    def get_latest_id(self, tb_name=None, id_name=None):
        print(f'get_latest_id for table: "{tb_name}" ')
        conn = self.create_connexion(self.db_file_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = f"SELECT {id_name} FROM {tb_name} WHERE {id_name}=(SELECT MAX({id_name}) FROM {tb_name});"
        res = False
        print(sql)
        try:
            cursor.execute(sql)
            # tmp_res = cursor.rowcount
            tmp_res = cursor.fetchone()
            print(tmp_res, type(tmp_res))
            if tmp_res != None:
                res = cursor.fetchone()
                print(res)
            self.close_connexion()
            return res
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")

    def udate_item(self, table=None, data_query=None):
        print(f'get_latest_id for table: "{table}" ')
        conn = self.create_connexion(self.db_file_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # TODO
        sql = f"""UPDTATE INTO {table} values (?,?),"""
        cursor.execute(data_query)
        print(sql)
        try:
            cursor.execute(sql)
            res = cursor.fetchone()[0]
            self.close_connexion()
            return res
        except sqlite3.Error as e:
            print(f"Error encontrado: {e}")

    # insert_one_register
    def insert_register(self, data_query=None):
        print(f"insert_register")
        conn = self.create_connexion(self.db_file_path)
        cursor = conn.cursor()

        try:
            cursor.execute(data_query)
            self.commit_db()
            print("Um registro inserido com sucesso.")
            self.close_connexion()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False


if __name__ == "__main__":
    # validating the connexion using the query and db_path as parameters
    # db_file_path = os.path.abspath(os.getcwd()) + '/Database/db_test.sqlite'
    # db_file_path = DB_FILE_PATH

    query_test = """SELECT name FROM sqlite_schema
                            WHERE type='table'
                            ORDER BY name;"""

    my_conn = Connect(DB_FILE_PATH)
    my_conn.run_query_test(query_test)
