import sys
import sqlite3

from prescription_management import*
from customer_menu import*

#menu for managing customer
class prescription_menu():
    def __init__(self):
        self.running = None
        self.active_detail = prescription_manage()
        self.active_replacement = customer_menu()

    def run_menu(self,choice):
        if choice == 1:
            pharmacist_id= "suesannah9635"
            customer_id = input("please enter the customer NHS number: ")
            Customer_id = self.get_customer_id()
            if customer_id in Customer_id:
                QuantityOfMed = input("please enter the quantity of medication requested: ")
            elif customer_id not in Customer_id:
                self.active_replacement.run_secondary_menu(customer_id)
                QuantityOfMed = input("please enter the quantity of medication requested: ")
            values = (pharmacist_id,customer_id,QuantityOfMed)
            self.active_detail.insert_prescription_data(values)
        elif choice == 2:
            id = input("please enter the id of the product you wish to change: ")
            choice = self.get_answers()
            prescription_code = self.get_prescription_code(id)
            print(prescription_code)
            pharmacist_id = self.get_pharmacist_id(id)
            print(pharmacist_id)
            Customer_id = self.get_customer_id(id)
            print(Customer_id)
            QuantityOfMed = self.get_prescription_quantity(id)
            print(QuantityOfMed)
            if choice == 1:
                pharmacist_id = input("please enter the new pharmacist_id of the the prescription: ")
                value = (pharmacist_id,id)
                self.active_detail.update_prescription_Pharmacist(value)
            elif choice == 2:
                pharmacist_id = input("please enter the new pharmacist_id of the the prescription: ")
                customer_id = input("please enter the new customer_id of the prescription: ")
                value = (pharmacist_id,Customer_id,id)
                self.active_detail.update_prescription_Pharmacustom(value)
            elif choice == 3:
                customer_id = input("please enter the new customer_id of the prescription: ")
                value = (Customer_id,id)
                self.active_detail.update_prescription_customer(value)
            elif choice == 4:
                customer_id = input("please enter the new customer_id of the prescription: ")
                QuantityOfMed = input("please enter the new QuantityOfMed of the the prescription: ")
                value = (Customer_id,QuantityOfMed,id)
                self.active_detail.update_prescription_quatitycustomer(value)
            elif choice == 5:
                QuantityOfMed = input("please enter the new QuantityOfMed of the the prescription: ")
                value = (QuantityOfMed,id)
                self.active_detail.update_prescription_quantity(value)
            elif choice == 6:
                pharmacist_id = input("please enter the new pharmacist_id of the the prescription: ")
                customer_id = input("please enter the new customer_id of the prescription: ")
                QuantityOfMed = input("please enter the new QuantityOfMed of the the prescription: ")
                value = (pharmacist_id,Customer_id,QuantityOfMed,id)
                self.active_detail.update_prescription_data(value)
        elif choice == 3:
            prescription = self.active_detail.prescription_data()
            print(prescription)
        elif choice == 4:
            done = False
            while not done:
                print("would you like to search by pharmacist id or by customer id: ",end = "")
                choices = input()
                choices = choices.lower()
                if choices in ["pharmacist id"]:
                    print("please enter the pharmacist id you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_prescription_data(id)
                    print(rename)
                    done = True
                elif choices in ["customer id"]:
                    print("please enter the customer id you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_prescription_data(name)
                    print(rename)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_prescription_data(choice)
            

    def get_customer_id(self):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ClientNHSNumber from Customer ")
            CustomerID = cursor.fetchall()
            return CustomerID
        
                          
    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.pharmacist id")
        print("2.pharmacist id and client id")
        print("3.client id")
        print("4.client id and QuantityOfMed")        
        print("5.QuantityOfMed")
        print("6.update all")
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
