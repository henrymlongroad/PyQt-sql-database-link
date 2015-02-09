import sys
import sqlite3

class customer_manage():
    def __init__(self):
        self.accessed = None
        
    def insert_customer_data(self,values):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "insert into customer (ClientNHSNumber,FirstName,LastName,HouseNumber,Street,Town,Postcode,TelephoneNum, EmailAddress) values (?,?,?,?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def update_customer_first(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_lastfirst(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_telelastfirst(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?, TelephoneNum=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_emailtelelastfirst(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?, TelephoneNum=?, Emailaddress=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housefirst(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?,TelephoneNum=?, Emailaddress=?, HouseNumber=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()
    
    def update_customer_housestreetpostfirst(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?,TelephoneNum=?, Emailaddress=?, HouseNumber=?,Street=?,Postcode=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_Last(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_TeleLast(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=?, TelephoneNum=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_EmailTeleLast(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=?,TelephoneNum=?, Emailaddress=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_HouseEmailTeleLast(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=?,TelephoneNum=?, Emailaddress=?, HouseNumber=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housestreetpostLast(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=?,TelephoneNum=?, Emailaddress=?, HouseNumber=?, Street=?, postcode=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housetownstreetpostLast(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set LastName=?,TelephoneNum=?, Emailaddress=?, HouseNumber=?, Street=?, postcode=?, town=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_customer_Tele(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set TelephoneNum=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_EmailTele(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set TelephoneNum=?, Emailaddress=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_customer_HouseEmailTele(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set TelephoneNum=?, Emailaddress=?, HouseNumber=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housestreetposttele(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set TelephoneNum=?, Emailaddress=?, HouseNumber=?, Street=?, postcode=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housetownstreetposttele(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set TelephoneNum=?, Emailaddress=?, HouseNumber=?, Street=?, postcode=?, town=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_Email(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set Emailaddress=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_customer_HouseEmail(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set Emailaddress=?, HouseNumber=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housestreetpost(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set Emailaddress=?, HouseNumber=?, Street=?, postcode=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housetownstreetpost(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set  Emailaddress=?, HouseNumber=?, Street=?, postcode=?, town=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_House(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set HouseNumber=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housestreetpost(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set HouseNumber=?, Street=?, postcode=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def update_customer_housetownstreetpost(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set HouseNumber=?, Street=?, postcode=?, town=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()
            
    def update_customer_data(self,data):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            sql = "update customer set FirstName=?, LastName=?,HouseNumber=?,Street=?,Postcode=?,Town=?,Emailaddress=?,TelephoneNum=? where customerID=?"
            cursor.execute(sql,data)
            db.commit()

    def customer_data(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select customerID, FirstName, LastName, ClientNHSNumber from customer ")
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
