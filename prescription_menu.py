import sys
import sqlite3

from prescription_management import*

#menu for managing customer
class product_menu():
    def __init__(self):
        self.running = None
        self.active_detail = prescription_manage()

    def run_menu(self,choice):
        if choice == 1:
            pharmacist_id= "suesannah9635"
            customer_id = input("please enter the customer NHS number: ")
            QuantityOfMed = input("please enter the quantity of medication requested: ")
            values = (prescription_code,pharmacist_id,customer_id,QuantityOfMed)
            self.active_detail.insert_prescription_data(values)
        elif choice == 2:
            id = input("please enter the id of the product you wish to change: ")
            choice = self.get_answers()
            prescription_code = get_prescription_code()
            pharmacist_id = get_pharmacist_id()
            Customer_id = get_Customer_id()
            QuantityOfMed = get_QuantityOfMed()
            if choice == 1:
                prescription_code = input("please enter the name of the product: ")
                value = (prescription_code,pharmacist_id,Customer_id,QuantityOfMed)
            elif choice == 2:
                prescription_code = input("please enter the name of the product: ")
                pharmacist_id = input("please enter the new weight of the the product: ")
                value = (prescription_code,pharmacist_id,Customer_id,QuantityOfMed)
            elif choice == 3:
                prescription_code = input("please enter the name of the product: ")
                pharmacist_id = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                value = (prescription_code,pharmacist_id,Customer_id,QuantityOfMed)
            elif choice == 4:
                pharmacist_id = input("please enter the new weight of the the product: ")
                value = (prescription_code,pharmacist_id,Customer_id,QuantityOfMed)
            elif choice == 5:
                pharmacist_id = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
            elif choice == 6:
                pharmacist_id = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                QuantityOfMed = input("please enter the new QuantityOfMed of the the product")
            elif choice == 7:
                productCode = input("please enter the new ProductCode of the product: ")
            elif choice == 8:
                productCode = input("please enter the new ProductCode of the product: ")
                QuantityOfMed = input("please enter the new QuantityOfMed of the the product")
            elif choice == 9:
                QuantityOfMed = input("please enter the new QuantityOfMed of the the product")  
            elif choice == 10:
                prescription_code = input("please enter the name of the product: ")
                pharmacist_id = input("please enter the new weight of the the product: ")
                productCode = input("please enter the new ProductCode of the product: ")
                QuantityOfMed = input("please enter the new QuantityOfMed of the the product")
        elif choice == 3:
            pprescription = self.active_detail.prescription_data()
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
                elif choices in ["customer id"]
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
    def get_prescription_code():
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ProductName from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product

    def get_pharmacist_id():
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ProductWeight from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product
        
    def get_customer_id():
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Productcode from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product
        
    def get_prescription_quantity():
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select QuantityOfMed from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product

                          
    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.prescription code")
        print("2.prescription code and pharmacist id")
        print("3.prescription code, pharmacist id and client id ")
        print("4.pharmacist id")
        print("5.pharmacist id and client id")
        print("6.pharmacist id and client id and QuantityOfMed")
        print("7.client id")
        print("8.client id and QuantityOfMed")        
        print("9.QuantityOfMed")
        print("10.update all")
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
