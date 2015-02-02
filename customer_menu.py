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
            NHSNumber = input("please enter the patients NHSnumber: ")
            FirstName = input("please enter the clients first name: ") 
            LastName = input("please enter the clients last name: ")
            HouseNumber= input("please enter the clients house number")
            streetname = input("please enter the clients street name: ") 
            town = input("please enter the clients town name: ")
            postcode = input("please enter the clients Postcode: ")
            print("does the client wish to give their phone number and email address: ", end = "")
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    values = (NHSNumber,FirstName,LastName,streetname,town,postcode,"NA","NA")
                    done = True
                elif answer in ["yes","y"]:
                    phone_number = input("please enter the clients Phone number: ")
                    email = input("please enter the clients email: ")
                    values = (NHSNumber,FirstName,LastName,streetname,town,postcode,phone_number,email)
                    done = True
                else:
                    done = False
                    print("please enter a valid answer: ")
            self.active_detail.insert_customer_data(values)
        elif choice == 2:
            self.active_detail.customer_data()
            choice = input("which id do you want to update: ")
            if choice == 1:
                FirstName = input("please enter a first name: ")
                data = (FirstName,choice)
            elif choice == 2:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                data = (FirstName,LastName,choice)
            elif choice == 3:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (FirstName,LastName,TelephoneNumber,choice)
            elif choice == 4:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,choice)
            elif choice == 5:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,HouseNumber,choice)
            elif choice == 6:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,choice)
            elif choice == 7:
                LastName = input("please enter a last name: ")
                data = (LastName,choice)
            elif choice == 8:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (LastName,TelephoneNumber,choice)
            elif choice == 9:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (LastName,TelephoneNumber,EmailAddress,choice)
            elif choice == 10:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,choice)
            elif choice == 11:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,choice)
            elif choice == 12:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,town,choice)
            elif choice == 13:
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (email,choice)
            elif choice == 14:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (phone_number,email,choice)
            elif choice == 15:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (HouseNumber,phone_number,email,choice)
            elif choice == 16:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (,choice)
            elif choice == 17:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (phone_number,EmailAddress,HouseNumber,streetname,postcode,Town,choice)
            elif choice == 18:
                EmailAddress = input("please enter their new email address: ")
                data = (EmailAddress,choice)
            elif choice == 19:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (EmailAddress,HouseNumber,choice)
            elif choice == 20:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (EmailAddress,HouseNumber,streetname,postcode,choice)
            elif choice == 21:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (EmailAddress,HouseNumber,streetname,postcode,town,choice)
            elif choice == 22:
                HouseNumber = input("please enter their new house number: ")
                data = (HouseNumber,choice)
            elif choice == 23:
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (HouseNumber,streetname,postcode,choice)
            elif choice == 24:
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (HouseNumber,streetname,postcode,town,choice)
            elif choice == 25:
                FirstName = input("please enter their newfirst name: ") 
                LastName = input("please enter their new last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (FirstName,LastName,HouseNumber,streetname,postcode,EmailAddress,phone_number,town,choice)
            print("do you wish to update their address: ", end = "")
            done = False
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    data = (FirstName,LastName,"NA","NA","NA","NA",choice)
                    done = True
                elif answer in ["yes","y"]:
                    streetname = input("please enter their street name: ") 
                    town = input("please enter their town name: ")
                    postcode = input("please enter their Postcode: ")
                    phone_number = input("please enter their Phone number: ")
                    data = (FirstName,LastName,streetname,town,postcode,phone_number,choice)
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
                    print(rename)
                    done = True
                elif choices in ["Firstname","firstname"]:
                    print("please enter the Name you wish to view: ",end = "")
                    name = input()
                    rename = self.active_detail.display_customer_data(name)
                    print(rename)
                    done = True
                else:
                    print("please enter a valid choice")
                    done = False
        elif choice == 5:
            choice = input("which id do you want to delete: ")
            self.active_detail.delete_customer_data(choice)
            
    def run_secondary_menu(self,NHSNumber):
            done = False
            NHSNumber = input("please enter the patients NHSnumber: ")
            FirstName = input("please enter the clients first name: ") 
            LastName = input("please enter the clients last name: ")
            HouseNumber = input("please enter the clients house number")
            streetname = input("please enter the clients street name: ") 
            town = input("please enter the clients town name: ")
            postcode = input("please enter the clients Postcode: ")
            print("does the client wish to give their phone number and email address: ", end = "")
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    values = (NHSNumber,FirstName,LastName,streetname,town,postcode,"NA","NA")
                    done = True
                elif answer in ["yes","y"]:
                    phone_number = input("please enter the clients Phone number: ")
                    email = input("please enter the clients email: ")
                    values = (NHSNumber,FirstName,LastName,streetname,town,postcode,phone_number,email)
                    done = True
                else:
                    done = False
                    print("please enter a valid answer: ")
            self.active_detail.insert_customer_data(values)

    def get_answers(self):
        print("what do you want to update?")
        print()
        print("1.First_Name")
        print("2.First_Name and Last_name")
        print("3.First_Name, Last_name and Phone_Number")
        print("4.First_Name, Last_name, Phone_Number and email_address")
        print("5.First_Name, Last_name, Phone_Number, email_address and HouseNumber")
        print("6.First_Name, Last_name, Phone_Number, email_address, HouseNumber, Street and Postcode")       
        print("7.Last_name")
        print("8.Last_name and Phone_Number")
        print("9.Last_name, Phone_Number and email_address")
        print("10.Last_name, Phone_Number, email_address and HouseNumber")#
        print("11.Last_name, Phone_Number, email_address, HouseNumber, Street and Postcode")
        print("12.Last_name, Phone_Number, email_address, HouseNumber, Town, Street and Postcode")
        print("13.Phone_Number")
        print("14.Phone_Number and email_address")
        print("15.Phone_Number, email_address, HouseNumber, Street and Postcode")
        print("16.Phone_Number, email_address, HouseNumber, Town, Street and Postcode")
        print("17.email_address")
        print("18.email_address, HouseNumber, Street and Postcode")
        print("19.email_address, HouseNumber, Town, Street and Postcode")
        print("20.HouseNumber")
        print("21.HouseNumber, Street and Postcode")
        print("22.HouseNumber, Town, Street and Postcode")
        print("23.update all")
        print()
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
            
