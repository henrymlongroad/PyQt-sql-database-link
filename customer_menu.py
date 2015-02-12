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
            while not done:
                true = False
                NHSNumber = input("please enter the patients NHSnumber: ")
                true = self.run_NHS_validate(NHSNumber)
                if true == True:
                    done = True
                else:
                    done = False
                    print("that is not a valid NHS number")
            FirstName = input("please enter the clients first name: ") 
            LastName = input("please enter the clients last name: ")
            HouseNumber= input("please enter the clients house number: ")
            Street = input("please enter the clients street name: ") 
            town = input("please enter the clients town name: ")
            postcode = input("please enter the clients Postcode: ")
            print("does the client wish to give their phone number and email address: ", end = "")
            done = False
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    values = (NHSNumber,FirstName,LastName,HouseNumber,Street,town,postcode,"NA","NA")
                    done = True
                elif answer in ["yes","y"]:
                    phone_number = input("please enter the clients Phone number: ")
                    email = input("please enter the clients email: ")
                    values = (NHSNumber,FirstName,LastName,HouseNumber,Street,town,postcode,phone_number,email)
                    done = True
                else:
                    done = False
                    print("please enter a valid answer: ")
            self.active_detail.insert_customer_data(values)
        elif choice == 2:
            choice2 = input("what id do you want to update: ")
            print("pass 1-1")
            choice1 = self.get_answers()
            print("pass 1-2")
            if choice1 == 1:
                FirstName = input("please enter a first name: ")
                data = (FirstName,choice2)
                self.active_detail.update_customer_first(data)
            elif choice1 == 2:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                data = (FirstName,LastName,choice2)
                self.active_detail.update_customer_lastfirst(data)
            elif choice1 == 3:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (FirstName,LastName,TelephoneNumber,choice2)
                self.active_detail.update_customer_telelastfirst(data)
            elif choice1 == 4:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,choice2)
                self.active_detail.update_customer_emailtelelastfirst(data)
            elif choice1 == 5:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,HouseNumber,choice2)
                self.active_detail.update_customer_housefirst(data)
            elif choice1 == 6:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (FirstName,LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,choice2)
                self.active_detail.update_customer_housestreetpostfirst(data)
            elif choice1 == 7:
                LastName = input("please enter a last name: ")
                data = (LastName,choice2)
                self.active_detail.update_customer_Last(data)
            elif choice1 == 8:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (LastName,TelephoneNumber,choice2)
                self.active_detail.update_customer_TeleLast(data)
            elif choice1 == 9:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (LastName,TelephoneNumber,EmailAddress,choice2)
                self.active_detail.update_customer_EmailTeleLast(data)
            elif choice1 == 10:
                FirstName = input("please enter a first name: ") 
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,choice2)
                self.active_detail.update_customer_HouseEmailTeleLast(data)
            elif choice1 == 11:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,choice2)
                self.active_detail.update_customer_housestreetpostLast(data)
            elif choice1 == 12:
                LastName = input("please enter a last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (LastName,TelephoneNumber,EmailAddress,HouseNumber,Street,postcode,town,choice2)
                self.active_detail.update_customer_housetownstreetpostLast(data)
            elif choice1 == 13:
                TelephoneNumber = input("please enter their new telephone number: ")
                data = (email,choice2)
                self.active_detail.update_customer_Tele(data)
            elif choice1 == 14:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                data = (phone_number,email,choice2)
                self.active_detail.update_customer_EmailTele(data)
            elif choice1 == 15:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (phone_number,email,HouseNumber,choice2)
                self.active_detail.update_customer_HouseEmailTele(data)
            elif choice1 == 16:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (phone_number,email,HouseNumber,Street,postcode,choice2)
                self.active_detail.update_customer_housestreetposttele(data)
            elif choice1 == 17:
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (phone_number,EmailAddress,HouseNumber,Street,postcode,Town,choice2)
                self.active_detail.update_customer_housetownstreetposttele(data)
            elif choice1 == 18:
                EmailAddress = input("please enter their new email address: ")
                data = (EmailAddress,choice2)
                self.active_detail.update_customer_Email(data)
            elif choice1 == 19:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                data = (EmailAddress,HouseNumber,choice2)
                self.active_detail.update_customer_HouseEmail(data)
            elif choice1 == 20:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (EmailAddress,HouseNumber,Street,postcode,choice2)
                self.active_detail.update_customer_housestreetpost(data)
            elif choice1 == 21:
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (EmailAddress,HouseNumber,Street,postcode,town,choice2)
                self.active_detail.update_customer_housetownstreetpost(data)
            elif choice1 == 22:
                HouseNumber = input("please enter their new house number: ")
                data = (HouseNumber,choice2)
                self.active_detail.update_customer_House(data)
            elif choice1 == 23:
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                postcode = input("please enter their new postcode: ")
                data = (HouseNumber,Street,postcode,choice2)
                self.active_detail.update_customer_housestreetpost(data)
            elif choice1 == 24:
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (HouseNumber,Street,postcode,town,choice2)
                self.active_detail.update_customer_housetownstreetpost(data)
            elif choice1 == 25:
                FirstName = input("please enter their newfirst name: ") 
                LastName = input("please enter their new last name: ")
                TelephoneNumber = input("please enter their new telephone number: ")
                EmailAddress = input("please enter their new email address: ")
                HouseNumber = input("please enter their new house number: ")
                Street = input("please enter their new street name: ")
                Town = input("please enter their new town name: ")
                postcode = input("please enter their new postcode: ")
                data = (FirstName,LastName,HouseNumber,Street,postcode,town,EmailAddress,phone_number,choice2)
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
            HouseNumber= input("please enter the clients house number: ")
            Street = input("please enter the clients street name: ") 
            town = input("please enter the clients town name: ")
            postcode = input("please enter the clients Postcode: ")
            print("does the client wish to give their phone number and email address: ", end = "")
            while not done:
                answer = input()
                answer = answer.lower()
                if answer in ["no","n"]:
                    values = (NHSNumber,FirstName,LastName,HouseNumber,Street,town,postcode,"NA","NA")
                    done = True
                elif answer in ["yes","y"]:
                    phone_number = input("please enter the clients Phone number: ")
                    email = input("please enter the clients email: ")
                    values = (NHSNumber,FirstName,LastName,HouseNumber,Street,town,postcode,phone_number,email)
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
        print("15.Phone_Number, email_address and HouseNumber")
        print("16.Phone_Number, email_address, HouseNumber, Street and Postcode")
        print("17.Phone_Number, email_address, HouseNumber, Town, Street and Postcode")
        print("18.email_address")
        print("19.email_address and HouseNumber")
        print("20.email_address, HouseNumber, Street and Postcode")
        print("21.email_address, HouseNumber, Town, Street and Postcode")
        print("22.HouseNumber")
        print("23.HouseNumber, Street and Postcode")
        print("24.HouseNumber, Town, Street and Postcode")
        print("25.update all")
        print()
        print("what is your choice: ",end = "")
        try:
            choice = int(input())
        except ValueError:
           print()
           self.get_answers()
        return choice
            
    def run_NHS_validate(self,NHSNumber):
        count = 1
        for each in NHSNumber:
            each1 = ord(each)
            if each1 in range(48,57):
                if count in range(1,4) or count in range(5,8) or count in range(9,13):
                    valid1 = True
                elif count == 4:
                    valid2 = False
                elif count == 8:
                    valid3 = False
            elif each1 == 32:
                if count in range(1,4) or count in range(5,8) or count in range(9,13):
                    valid1 = False
                elif count == 4:
                    valid2 = True
                elif count == 8:
                    valid3 = True  
            count+=1 
        if valid1 == True and valid2 == True and valid3 == True:
            true = True
        else:
            true = False
        return true
