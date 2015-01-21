import sys
import sqlite3

class manufacturer_manage():
    def __init__(self):
        self.accessed = None

    def insert_manufacturer_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into Manufacturer(Manufacturer,Product,ManufacturerTown,ManufacturerStreet,ManufacturerPostcode) values (?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def update_manufacturer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=?,product=?,ManufacturerTown=?,ManufacturerStreet=?,ManufacturerPostcode=?  where Manufacturer=?"
            cursor.execute(sql,data)
            db.commit()

    def manufacturer_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Manufacturer, Product, ManufacturerPostcode from Manufacturer ")
            Product = cursor.fetchall()
            return Product

    def display_manufacturer_data(self,name):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Manufacturer where Manufacturer=?",(name,))
            Product = cursor.fetchone()
            return Product

    def delete_manufacturer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("delete from Manufacturer where Manufacturer=?",(data,))
            db.commit()






