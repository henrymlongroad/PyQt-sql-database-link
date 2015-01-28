from PyQt4.QtCore import*
from PyQt4.QtGui import*


import sys
import sqlite3

from product_menu import*
from customer_menu import*
from prescription_menu import*
from order_menu import*
from manufacturer_menu import*



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
        choice1 = 0
        return choice, choice1
    elif choice in range(1,6):
        choice1 = run_sub_menu(choice)
    else:
        choice, choice1 = run_main_menu()
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
    elif choice == 3:
        print("1. insert data into {0}".format("prescription"))
        print("2. update data in {0}".format("prescription"))
        print("3. display data from {0}".format("prescription"))
        print("4. find item in {0}".format("prescription"))
        print("5. delete item in {0}".format("prescription"))
        print("choice : ", end = "")
    elif choice == 4:
        print("1. insert data into {0}".format("orders"))
        print("2. update data in {0}".format("orders"))
        print("3. display data from {0}".format("orders"))
        print("4. find item in {0}".format("orders"))
        print("5. delete item in {0}".format("orders"))
        print("choice : ", end = "")
    elif choice == 5:
        print("1. insert data into {0}".format("manufacturer"))
        print("2. update data in {0}".format("manufacturer"))
        print("3. display data from {0}".format("manufacturer"))
        print("4. find item in {0}".format("manufacturer"))
        print("5. delete item in {0}".format("manufacturer"))
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
        elif choice == 3:
            connect = prescription_menu()
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
        elif choice == 4:
            connect = order_menu()
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
        elif choice == 5:
            connect = manufacturer_menu()
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

if __name__ == "__main__":
    run_main()

