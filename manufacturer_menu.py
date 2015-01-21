import sys
import sqlite3

from manufacturer_management import*

#menu for managing customer
class manufacturer_menu():
    def __init__(self):
        self.running = None
        self.active_detail = manufacturer_manage()

    def run_menu(self,choice):
        if choice == 1:
            manufacturer = input("please enter the name of the manufacturer: ")
            product= input("please enter the name of the product: ")
            manufacturertown = input("please enter the town the manufacturer is located: ")
            manufacturerstreet = input("please enter the street which the manufacturer is based: ")
            manufacturerpostcode = input("please enter the postcode of the manufacturer: ")
            values = (manufacturer,product,manufacturertown,manufacturerstreet,manufacturerpostcode)
            self.active_detail.insert_manufacturer_data(values)
        elif choice == 2:
            id = input("please enter the id of the product you wish to change: ")
            choice = self.get_answers()
            manufacturer = self.get_manufacturer_name(id)
            product = self.get_product(id)
            town = self.get_manufacturer_town(id)
            street= self.get_manufacturer_street(id)
            postcode = self.get_manufacturer_postcode(id)
            if choice == 1:
                manufacturer = input("please enter the name of the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 2:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new weight of the the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 3:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new weight of the the manufacturer: ")
                town = input("please enter the new town of the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 4:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new weight of the the manufacturer: ")
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 5:
                product = input("please enter the new product of the the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 6:
                product = input("please enter the new product of the the manufacturer: ")
                town = input("please enter the new town of the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 7:
                product = input("please enter the new weight of the the manufacturer: ")
                street = input("please enter the new town of the manufacturer: ")
                postcode = input("please enter the new street of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 8:
                product = input("please enter the new weight of the the manufacturer: ")
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 9:
                street = input("please enter the new town of the manufacturer: ")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 10:
                town = input("please enter the new town of the manufacturer: ")
                street = input("please enter the new street of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 11:
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 12:
                street = input("please enter the new street of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 13:
                street = input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 14:
                postcode == input("please enter the new postcode of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            elif choice == 15:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new weight of the the manufacturer: ")
                town = input("please enter the new town of the manufacturer: ")
                street = input("please enter the new street of the manufacturer: ")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (manufacturer,product,town,street,postcode)
            self.active_detail.update_manufacturer_data(value)
        elif choice == 3:
            manufacturer = self.active_detail.manufacturer_data()
            print(manufacturer)
        elif choice == 4:
            done = False
            while not done:
                print("would you like to search by manufacturer or by product: ",end = "")
                choices = input()
                choices = choices.lower()
                if choices in ["manufacturer"]:
                    print("please enter the pharmacist id you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_manufacturer_data(id)
                    print(rename)
                    done = True
                elif choices in ["product"]:
                    print("please enter the customer id you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_manufacturer_data(name)
                    print(rename)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_manufacturer_data(choice)

    def get_Manufacturer_name(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Manufacturer from Manufacturer where Manufacturer=?",(id,))
            manufacturer = cursor.fetchone()
            return manufacturer
        
    def get_Product_info(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select Product from Manufacturer where Manufacturer=?",(id,))
            Product = cursor.fetchone()
            return Product

    def get_manufacturer_town(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ManufacturerTown from Manufacturer where Manufacturer=?",(id,))
            town = cursor.fetchone()
            return town
        
    def get_manufacturer_street(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ManufacturerStreet from Manufacturer where Manufacturer=?",(id,))
            street = cursor.fetchone()
            return street
        
    def get_manufacturer_postcode(self,id):
        with sqlite3.connect("pharmacy_database.db") as db:
            cursor = db.cursor()
            cursor.execute("select ManufacturerPostcode from Manufacturer where Manufacturer=?",(id,))
            postcode = cursor.fetchone()
            return postcode

                          
    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.Manufacturer")
        print("2.Manufacturer and Product")
        print("3.Manufacturer,Product and ManufacturerTown")
        print("4.Manufacturer,Product,ManufacturerTown and ManufacturerStreet")
        print("5.Product")
        print("6.Product,ManufacturerTown")
        print("7.Product,ManufacturerTown and ManufacturerStreet")
        print("8.Product,ManufacturerTown, ManufacturerStreet and ManufacturerPostcode")
        print("9.ManufacturerTown")
        print("10.ManufacturerTown and ManufacturerStreet")
        print("11.ManufacturerTown, ManufacturerStreet and ManufacturerPostcode")
        print("12.ManufacturerStreet")
        print("13.ManufacturerStreet and ManufacturerPostcode")        
        print("14.ManufacturerPostcode")
        print("15.update all")
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice

