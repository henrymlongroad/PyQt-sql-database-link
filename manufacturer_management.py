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

    def update_manufacturer_name(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_productname(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=?,product=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_townproductname(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=?,product=?,ManufacturerTown=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_streettownproductname(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=?,product=?,ManufacturerTown=?,ManufacturerStreet=?,ManufacturerPostcode=?  where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_manufacturer_product(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set product=? where ManufacturerIDr=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_townproduct(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set product=?,ManufacturerTown=?  where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_manufacturer_streettownproduct(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set product=?,ManufacturerTown=?,ManufacturerStreet=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_postcodestreettownproduct(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set product=?,ManufacturerTown=?,ManufacturerStreet=?,ManufacturerPostcode=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_manufacturer_town(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerTown=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_streettown(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerTown=?,ManufacturerStreet=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_postcodestreettown(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerTown=?,ManufacturerStreet=?,ManufacturerPostcode=?  where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_street(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerStreet=? where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_manufacturer_postcodestreet(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerStreet=?,ManufacturerPostcode=?  where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_manufacturer_postcode(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set ManufacturerPostcode=?  where ManufacturerID=?"
            cursor.execute(sql,data)
            db.commit()
        
    def update_manufacturer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Manufacturer set manufacturer=?,product=?,ManufacturerTown=?,ManufacturerStreet=?,ManufacturerPostcode=?  where ManufacturerID=?"
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






