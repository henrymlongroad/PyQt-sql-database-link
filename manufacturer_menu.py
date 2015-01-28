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
            if choice == 1:
                manufacturer = input("please enter the name of the manufacturer: ")
                value = (manufacturer,id)
                self.active_detail.update_manufacturer_name(value)
            elif choice == 2:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new name of the  product: ")
                value = (manufacturer,product,id)
                self.active_detail.update_manufacturer_productname(value)
            elif choice == 3:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new name of the product: ")
                town = input("please enter the new town of the manufacturer: ")
                value = (manufacturer,product,town,id)
                self.active_detail.update_manufacturer_townproductname(value)
            elif choice == 4:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new name of the product: ")
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                value = (manufacturer,product,town,street,id)
                self.active_detail.update_manufacturer_streettownproductname(value)
            elif choice == 5:
                product = input("please enter the new name of the product: ")
                value = (product,id)
                self.active_detail.update_manufacturer_product(value)
            elif choice == 6:
                product = input("please enter the new name of the product: ")
                town = input("please enter the new town of the manufacturer: ")
                value = (product,town,id)
                self.active_detail.update_manufacturer_townproduct(value)
            elif choice == 7:
                product = input("please enter the new name of the product: ")
                town = input("please enter the new town of the manufacturer: ")
                street = input("please enter the new street of the the manufacturer")
                value = (product,town,street,id)
                self.active_detail.update_manufacturer_streettownproduct(value)
            elif choice == 8:
                product = input("please enter the new name of the product: ")
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (product,town,street,postcode,id)
                self.active_detail.update_manufacturer_postcodestreettownproduct(value)
            elif choice == 9:
                town = input("please enter the new town of the manufacturer: ")
                value = (town,id)
                self.active_detail.update_manufacturer_town(value)
            elif choice == 10:
                town = input("please enter the new town of the manufacturer: ")
                street = input("please enter the new street of the the manufacturer")
                value = (town,street,postcode,id)
                self.active_detail.update_manufacturer_streettown(value)
            elif choice == 11:
                town = input("please enter the new town of the manufacturer: ")
                street= input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (town,street,postcode,id)
                self.active_detail.update_manufacturer_postcodestreettown(value)
            elif choice == 12:
                street = input("please enter the new street of the the manufacturer")
                value = (street,postcode,id)
                self.active_detail.update_manufacturer_street(value)
            elif choice == 13:
                street = input("please enter the new street of the the manufacturer")
                postcode = input("please enter the new postcode of the the manufacturer")
                value = (street,postcode,id)
                self.active_detail.update_manufacturer_postcodestreet(value)
            elif choice == 14:
                postcode == input("please enter the new postcode of the the manufacturer")
                value = (postcode,id)
                self.active_detail.update_manufacturer_postcode(value)
            elif choice == 15:
                manufacturer = input("please enter the name of the manufacturer: ")
                product = input("please enter the new name of the product: ")
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
                    print("please enter the manufacturer you wish to view: " ,end = "")
                    id = input()
                    rename = self.active_detail.display_manufacturer_data(id)
                    print(rename)
                    done = True
                elif choices in ["product"]:
                    print("please enter the product you wish to view: ",end = "")
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

