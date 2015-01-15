from PyQt4.QtCore import*
from PyQt4.QtGui import*

import sys
import sqlite3

from product_menu import*
from customer_menu import*

def run_main_menu():
    print("which area of the database do you wish to access")
    print()
    print("1. customer")
    print("2. products")
    print("3. prescription data")
    print("4. Orders")
    print("5. manufacturers")
    print("0. close the database")
    print("choice : ", end = "")
    try:
        choice = int(input())
    except ValueError:
        print()
        choice, choice1 = run_main_menu()
    if choice == 0:
        return choice
    elif choice in range(1,6):
        choice1 = run_sub_menu(choice)
    else:
        run_main_menu()
    return choice, choice1
def run_sub_menu(choice):
    if choice == 1:
        print("1. insert data into {0}".format("customer"))
        print("2. update data in {0}".format("customer"))
        print("3. display data from {0}".format("customer"))
        print("4. find item in {0}".format("customer"))
        print("5. delete item in {0}".format("customer"))
        print("choice : ", end = "")
    elif choice == 2:
        print("1. insert data into {0}".format("product"))
        print("2. update data in {0}".format("product"))
        print("3. display data from {0}".format("product"))
        print("4. find item in {0}".format("product"))
        print("5. delete item in {0}".format("product"))
        print("choice : ", end = "")
    try:
        choice1 = int(input())
    except ValueError:
        print()
        choice1 = run_sub_menu(choice)
    return choice1


def run_main():
    close = False
    while not close:
        connect = None
        choice, choice1 = validate_choice()
        if choice == 0:
            close = True
        elif choice == 1:
            connect = customer_menu()
            if choice1 == 1:
                connect.run_menu(choice1)
            elif choice1 == 2:
                connect.run_menu(choice1)
            elif choice1 == 3:
                connect.run_menu(choice1)
            elif choice1 == 4:
                connect.run_menu(choice1)
            elif choice1 == 5:
                connect.run_menu(choice1)
        elif choice == 2:
            connect = product_menu()
            if choice1 == 1:
                connect.run_menu(choice1)
            elif choice1 == 2:
                connect.run_menu(choice1)
            elif choice1 == 3:
                connect.run_menu(choice1)
            elif choice1 == 4:
                connect.run_menu(choice1)
            elif choice1 == 5:
                connect.run_menu(choice1)
        else:
            print("Hey Listen")
    
def validate_choice():
    choicechecked = False
    choice, choice1 = run_main_menu()
    while not choicechecked:
        if choice in range(0,6):
            choicechecked = True
        else:
            print()
            choice, choice1  = run_main_menu()
    return choice, choice1 

def insert_customer_data(values):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "insert into customer (FirstName, LastName,Street,Town,Postcode,TelephoneNum, EmailAddress) values (?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def update_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "update customer set FirstName=?, L
        astName=?,street=?,town=?,postcode=?,TelephoneNum=?,EmailAddress=? where customerID=?"
        cursor.execute(sql,data)
        db.commit()

def customer_data():
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select customerID, FirstName, LastName from customer ")
        customer = cursor.fetchall()
        return customer

def display_customer_data(FirstName):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from customer where FirstName=?",(FirstName,))
        customer = cursor.fetchone()
        return customer

def display_customer_data(id):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from customer where customerID=?",(id,))
        customer = cursor.fetchone()
        return customer

def delete_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("delete from customer where customerID=?",(data,))
    db.commit()





if __name__ == "__main__":
    run_main()

