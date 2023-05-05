import mysql.connector
import pandas as pd
import math

class database:
    def __init__(self):
        self.cnx = mysql.connector.connect(
        host="45.77.80.71",
        user="sistemas",
        password="Sm~18jn57",
        database="emaran")
        #database = "inventario")
        self.cursor = self.cnx.cursor()

    def gettable(self, table):
        sql = "SELECT * FROM "+table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getdf(self, table):
        sql = "SELECT * FROM "+table
        self.cursor.execute(sql)
        return pd.read_sql(sql, con=self.cnx)
    def showTables(self, table):
        resutl = self.gettable(table)
        for row in resutl:
            print(row)
        return True


db = database()
db.showTables("plaza_vea_ejercito")
print("++++++++++++++++++++")
