import sys
import sqlite3


class prescription_manage():
    def __init__(self):
        self.accessed = None

    def insert_prescription_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into Prescription (PharmacistID,CustomerID,QuantityOfMed) values (?,?,?)"
            cursor.execute(sql,values)
            db.commit()


    def update_prescription_Pharmacist(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set PharmacistID=? where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()


    def update_prescription_Pharmacustom(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set PharmacistID=?, CustomerID=?where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()

    def update_prescription_customer(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set CustomerID=? where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()

    def update_prescription_quatitycustomer(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set CustomerID=?, QuantityOfMed=? where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()

    def update_prescription_quantity(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set QuantityOfMed=? where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()

    def update_prescription_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update Prescription set PharmacistID=?, CustomerID=?, QuantityOfMed=? where PrescriptionCode=?"
            cursor.execute(sql,data)
            db.commit()

    def prescription_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select PharmacistID,CustomerID,QuantityOfMed from Prescription ")
            prescription = cursor.fetchall()
            return prescription

    def display_prescription_data(self,name):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Prescription where CustomerID=?",(name,))
            prescription = cursor.fetchone()
            return prescription

    def display_prescription_data(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Prescription where PharmacistID=?",(id,))
            prescription = cursor.fetchone()
            return prescription

    def delete_prescription_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("delete from Prescription where PrescriptionCode=?",(data,))
            db.commit()





