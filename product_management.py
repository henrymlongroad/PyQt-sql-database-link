import sys
import sqlite3


class product_manage():
    def __init__(self):
        self.accessed = None

    def insert_product_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into Product (ProductName,ProductWeight,ProductCode,Price) values (?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def update_product_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Product set ProductName=?,ProductWeight=?,ProductCode=?,Price=? where ProductID=?"
            cursor.execute(sql,data)
            db.commit()

    def product_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ProductID, ProductName, ProductCode from Product ")
            Product = cursor.fetchall()
            return Product

    def display_product_data(self,name):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Product where ProductName=?",(name,))
            Product = cursor.fetchone()
            return Product

    def display_product_data(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product

    def delete_product_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("delete from Product where ProductID=?",(data,))
            db.commit()




