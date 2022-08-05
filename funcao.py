import imp
import os
import sys
import sqlite3
from sqlite3 import Error
from PySide2.QtWidgets import QTableWidgetItem


class AppFunctions():
    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg

    #cria conexão com base de dados
    def create_connection(db_file):
        conn = None
        try:
            conn =sqlite3.connect(db_file)
        except Error as e:
            print(e)
            
        return conn

    #cria tabela
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main(dbFolder):
        create_user_table = """CREATE TABLE IF NOT EXISTS Users(
                                                USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                USER_NAME TEXT,
                                                USER_EMAIL TEXT,
                                                USER_TEL TEXT); """
        conn = AppFunctions.create_connection(dbFolder)

        if conn is not None:
            AppFunctions.create_table(conn, create_user_table)
        else:
            print('Erro ao criar a tabela de dados!!')

    #pegar todos os usuarios
    def get_users(dbfolder):


        try:
            conn = AppFunctions.create_connection(dbfolder)

            get_all_users = """SELECT * FROM Users;"""
            c = conn.cursor()
            c.execute(get_all_users)
            return c
        except Error as e:
            print(e)

    def insert_users(self, dbfolder):
        conn = AppFunctions.create_connection(dbfolder)

        usuario = self.ui.usuario.text()
        email = self.ui.email.text()
        telefone = self.ui.telefone.text()

        insert_user = f"""INSERT INTO Users(USER_NAME, USER_EMAIL, USER_TEL) 
                                            VALUES('{usuario}', '{email}', '{telefone}');"""

        if not conn.cursor().execute(insert_user):
            print("Erro ao inserir dados!")
        else:
            conn.commit()
            self.ui.usuario.setText("")
            self.ui.email.setText("")
            self.ui.telefone.setText("")
            AppFunctions.displayUsers(self, AppFunctions.get_users(dbfolder))

    
    def displayUsers(self,rows):

            for row in rows:
                rowPos = self.ui.tableWidget.rowCount()

                if rowPos + 1 > row[0]:
                    continue

                itemCount = 0
                self.ui.tableWidget.setRowCount(rowPos + 1)
                qTableWidgetItem = QTableWidgetItem()
                self.ui.tableWidget.setVerticalHeaderItem(rowPos, qTableWidgetItem)

                for item in row:
                    self.qtablewidgetitem = QTableWidgetItem()
                    self.ui.tableWidget.setItem(rowPos, itemCount, self.qtablewidgetitem)
                    self.qtablewidgetitem = self.ui.tableWidget.item(rowPos, itemCount)
                    self.qtablewidgetitem.setText(str(item))

                    itemCount += 1
                rowPos += 1

