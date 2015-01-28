import sys
import sqlite3


class orders_manage():
    def __init__(self):
        self.accessed = None

    def insert_order_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into Orders (OrderDate,OrderSize) values (?,?)"
            cursor.execute(sql,values)
            db.commit()

    def update_order_date(self,data):
        print(data)
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Orders set OrderDate=? where OrderNum=?"
            cursor.execute(sql,data)
            db.commit()

    def update_order_size(self,data):
        print(data)
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Orders set OrderSize=? where OrderNum=?"
            cursor.execute(sql,data)
            db.commit()

    def update_order_sizedate(self,data):
        print(data)
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Orders set OrderDate=?, OrderSize=? where OrderNum=?"
            cursor.execute(sql,data)
            db.commit()

    def order_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select OrderNum, OrderDate, OrderSize from Orders")
            Product = cursor.fetchall()
            return Product

    def display_order_data(self,date):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Orders where OrderDate=?",(date,))
            Product = cursor.fetchone()
            return Product

    def display_order_data(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Orders where OrderNum=?",(id,))
            Product = cursor.fetchone()
            return Product

    def delete_order_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("delete from Orders where OrderNum=?",(data,))
            db.commit()





