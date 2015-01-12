from PyQt4.QtCore import*
from PyQt4.QtGui import*

import sys
import sqlite3


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
        choice1 = int(input())
    except ValueError:
        print()
        choice1 = run_main_menu()
    if choice1 == 0:
        return choice1
    elif choice1 in range(1,6):
        choice = run_sub_menu(choice1)
    else:
        run_main_menu()
    return choice
def run_sub_menu(choice):
    if choice == 1:
        print("1. insert data into {0}".format("customer"))
        print("2. update data in {0}".format("customer"))
        print("3. display data from {0}".format("customer"))
        print("4. find item in {0}".format("customer"))
        print("5. delete item in {0}".format("customer"))
        print("choice : ", end = "")
    try:
        choice1 = int(input())
    except ValueError:
        print()
        choice1 = run_sub_menu()
    return choice1


def run_main():
    close = False
    while not close:
        choice = validate_choice()
        if choice == 0:
            close = True
        elif choice == 1:
            FirstName = input("please enter your first name: ") 
            LastName = input("please enter your last name: ")
            print("do you wish to give your address: ", end = "")
            answer = input()
            answer = answer.lower()
            if answer in ["no","n"]:
                values = (FirstName,LastName,"NA","NA","NA","NA","NA")
            elif answer in ["yes","y"]:
                streetname = input("please enter your street name: ") 
                town = input("please enter your town name: ")
                postcode = input("please enter your Postcode: ")
                phone_number = input("please enter your Phone number: ")
                email = input("please enter your email: ")
                values = (FirstName,LastName,streetname,town,postcode,phone_number,email)
            insert_customer_data(values)
        elif choice == 2:
            customer_data()
            choice = input("which id do you want to update: ")
            FirstName = input("please enter your first name: ") 
            LastName = input("please enter your last name: ") 
            data = (FirstName,LastName,choice)
            update_customer_data(data)
        elif choice == 3:
            customer = customer_data()
            print(customer)
        elif choice == 4:
            print("would you like to search by ID or by firstname: ",end = "")
            choices = input()
            if choices in ["ID","Id","id"]:
                print("please enter the ID you wish to view": ,end = "")
                id = input()
                rename = display_customer_data(id)
                print(rename)
            elif choices in ["Firstname","firstname"]:
                print("please enter the Name you wish to view: ",end = "")
                name = input()
                rename = display_customer_data(name)
                print(rename)
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            delete_customer_data(choice) 
        elif choice == 0:
            close = True
        else:
            print("Hey Listen")
    
def validate_choice():
    choicechecked = False
    choice = run_main_menu()
    while not choicechecked:
        if choice in range(0,6):
            choicechecked = True
        else:
            print()
            choice = run_main_menu()
    return choice

def insert_customer_data(values):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "insert into customer (FirstName, LastName,Street,Town,Postcode,TelephoneNum, EmailAddress) values (?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def update_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "update customer set FirstName=?, LastName=? where customerID=?"
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





run_main()

