import sys
import sqlite3

class customer_manage():
    def __init__(self):
        self.accessed = None
        
    def insert_customer_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into customer (FirstName, LastName,Street,Town,Postcode,TelephoneNum, EmailAddress) values (?,?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def update_customer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?,Street=?,Town=?,Postcode=?,TelephoneNum=?,EmailAddress=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def customer_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select customerID, FirstName, LastName from customer ")
            customer = cursor.fetchall()
            return customer

    def display_customer_data(self,FirstName):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from customer where FirstName=?",(FirstName,))
            customer = cursor.fetchone()
            return customer

    def display_customer_data(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from customer where customerID=?",(id,))
            customer = cursor.fetchone()
            return customer

    def delete_customer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("delete from customer where customerID=?",(data,))
        db.commit()
