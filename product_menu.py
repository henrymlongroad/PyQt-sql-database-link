import sys
import sqlite3

from product_management import*

#menu for managing customer
class product_menu():
    def __init__(self):
        self.running = None
        self.active_detail = product_manage()

    def run_menu(self,choice):
        if choice == 1:
            product_name = input("please enter the name of the product: ")
            product_weight = input("please enter the products weight: ")
            product_code = input("please enter the product code: ")
            price = input("please enter the products price: ")
            values = (product_name,product_weight,product_code,price)
            self.active_detail.insert_product_data(values)
        elif choice == 2:
            choice1 = input("please enter the id of the product you wish to change: ")
            choice = self.get_answers()
            if choice == 1:
                product_name = input("please enter the name of the product: ")
                value = (product_name,choice1)
                self.active_detail.update_product_name(value)
            elif choice == 2:
                product_name = input("please enter the name of the product: ")
                product_weight = input("please enter the new weight of the the product: ")
                value = (product_name,product_weight,choice1)
                self.active_detail.update_product_weightname(value)
            elif choice == 3:
                product_name = input("please enter the name of the product: ")
                product_weight = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                value = (product_name,product_weight,product_code,choice1)
                self.active_detail.update_product_codeweightname(value)
            elif choice == 4:
                product_weight = input("please enter the new weight of the the product: ")
                value = (product_weight,choice1)
                self.active_detail.update_product_weight(value)
            elif choice == 5:
                product_weight = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                value = (product_weight,product_code,choice1)
                self.active_detail.update_product_codeweight(value)
            elif choice == 6:
                product_weight = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                price = input("please enter the new price of the the product")
                value = (product_weight,product_code,price,choice1)
                self.active_detail.update_product_pricecodeweight(value)
            elif choice == 7:
                productCode = input("please enter the new ProductCode of the product: ")
                value = (product_code,choice1)
                self.active_detail.update_product_code(value)
            elif choice == 8:
                productCode = input("please enter the new ProductCode of the product: ")
                price = input("please enter the new price of the the product")
                value = (product_code,price,choice1)
                self.active_detail.update_product_pricecode(value)
            elif choice == 9:
                price = input("please enter the new price of the the product")
                value = (price,choice1)
                self.active_detail.update_product_price(value)
            elif choice == 10:
                product_name = input("please enter the name of the product: ")
                product_weight = input("please enter the new weight of the the product: ")
                productCode = input("please enter the new ProductCode of the product: ")
                price = input("please enter the new price of the the product")
                value = (product_name,product_weight,product_code,price,choice1)
                self.active_detail.update_product_data(value)
        elif choice == 3:
            product = self.active_detail.product_data()
            print(product)
        elif choice == 4:
            done = False
            while not done:
                print("would you like to search by ID or by productname: ",end = "")
                choices = input()
                choices = choices.lower()
                if choices in ["id"]:
                    print("please enter the ID you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_product_data(id)
                    print(rename)
                    done = True
                elif choices in ["productname"]:
                    print("please enter the Name you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_product_data(name)
                    print(rename)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_product_data(choice)

    def get_product_name(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ProductName from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product

    def get_product_weight(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ProductWeight from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product
        
    def get_product_code(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Productcode from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product
        
    def get_product_price(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Price from Product where ProductID=?",(id,))
            Product = cursor.fetchone()
            return Product
        db.commit()
                          
    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.product name")
        print("2.product name and product weight")
        print("3.product name, product weight and product code ")
        print("4.product weight")
        print("5.product weight and product code")
        print("6.product weight, product code and price")
        print("7.product code")
        print("8.product code and price")        
        print("9.price")
        print("10.update all")
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
        
                          
                        
