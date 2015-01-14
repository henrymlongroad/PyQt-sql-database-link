import sys
import sqlite3

from customer_management import*

#menu for managing customer
class customer_menu():
    def __init__(self):
        self.running = None
        self.active_detail = customer_manage()

    def run_menu(self,choice):
        if choice == 1:
            done = False
            FirstName = input("please enter your first name: ") 
            LastName = input("please enter your last name: ")
            print("do you wish to give your address: ", end = "")
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    values = (FirstName,LastName,"NA","NA","NA","NA","NA")
                    done = True
                elif answer in ["yes","y"]:
                    streetname = input("please enter your street name: ") 
                    town = input("please enter your town name: ")
                    postcode = input("please enter your Postcode: ")
                    phone_number = input("please enter your Phone number: ")
                    email = input("please enter your email: ")
                    values = (FirstName,LastName,streetname,town,postcode,phone_number,email)
                    done = True
                else:
                    done = False
                    print("please enter a valid answer: ")
            self.active_detail.insert_customer_data(values)
        elif choice == 2:
            self.active_detail.customer_data()
            choice = input("which id do you want to update: ")
            FirstName = input("please enter a first name: ") 
            LastName = input("please enter a last name: ")
            print("do you wish to update their address: ", end = "")
            done = False
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    data = (FirstName,LastName,"NA","NA","NA","NA","NA",choice)
                    done = True
                elif answer in ["yes","y"]:
                    streetname = input("please enter their street name: ") 
                    town = input("please enter their town name: ")
                    postcode = input("please enter their Postcode: ")
                    phone_number = input("please enter their Phone number: ")
                    email = input("please enter their email: ")
                    data = (FirstName,LastName,streetname,town,postcode,phone_number,email,choice)
                    done = True
                else:
                    print("please enter a valid choice: ", end = "")
            self.active_detail.update_customer_data(data)
        elif choice == 3:
            customer = self.active_detail.customer_data()
            print(customer)
        elif choice == 4:
            done = False
            while not done:
                print("would you like to search by ID or by firstname: ",end = "")
                choices = input()
                if choices in ["ID","Id","id"]:
                    print("please enter the ID you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_customer_data(id)
                    done = True
                elif choices in ["Firstname","firstname"]:
                    print("please enter the Name you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_customer_data(name)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_customer_data(choice) 
