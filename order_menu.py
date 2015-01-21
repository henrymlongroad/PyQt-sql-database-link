import sys
import sqlite3

from orders_management import*

#menu for managing customer
class order_menu():
    def __init__(self):
        self.running = None
        self.active_detail = orders_manage()

    def run_menu(self,choice):
        if choice == 1:
            order_date = input("please enter the order date: ")
            order_size = input("please enter the size of the order: ")
            values = (orderdate,order_size)
            self.active_detail.insert_order_data(values)
        elif choice == 2:
            id = input("please enter the id of the product you wish to change: ")
            choice = self.get_answers()
            orderdate = self.get_order_date(id)
            order_size = self.get_order_size(id)
            if choice == 1:
                orderdate = input("please enter the name of the product: ")
                value = (orderdate,order_size)
            elif choice == 2:
                orderdate = input("please enter the name of the product: ")
                order_size = input("please enter the new weight of the the product: ")
                value = (orderdate,order_size)
            elif choice == 3:
                orderdate = input("please enter the name of the product: ")
                order_size = input("please enter the new weight of the the product: ")
                ProductCode = input("please enter the new ProductCode of the product: ")
                value = (orderdate,order_size,ProductCode)
            self.active_detail.update_order_data(value)
        elif choice == 3:
            order = self.active_detail.order_data()
            print(order)
        elif choice == 4:
            done = False
            while not done:
                print("would you like to search by order_num or by order_date: ",end = "")
                choices = input()
                choices = choices.lower()
                if choices in ["order_num","order num","order number","order_number"]:
                    print("please enter the order number you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_order_data(id)
                    print(rename)
                    done = True
                elif choices in ["order_date","order date"]:
                    print("please enter the customer id you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_order_data(name)
                    print(rename)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_order_data(choice)
    def get_orderdate(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select OrderDate from Orders where OrderNum=?",(id,))
            Product = cursor.fetchone()
    def get_order_size(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select OrderSize from Orders where OrderNum=?",(id,))
            Product = cursor.fetchone()
            return Product
                          
    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.orderdate")
        print("2.order_size")
        print("3.update all")
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
