import sqlite3

def run_menu():
    
    print("1. insert data into database")
    print("2. update data in database")
    print("3. display data from database")
    print("4. find customer in database")
    print("5. delete item in database")
    print("0. cloce the database")
    print("choice: ",end="")
    try:
        choice = int(input())
    except ValueError:
        print()
        choice = run_menu()
    
    return choice

def validate_choice():
    choicechecked = False
    choice = run_menu()
    while not choicechecked:
        if choice in range(0,6):
            choicechecked = True
        else:
            print()
            choice = run_menu()
    return choice

def insert_customer_data(values):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "insert into customer (CustomerID, FirstName, LastName) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def update_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "update customer set FirstName=?, LastName=? where customerID=?"
        cursor.execute(sql,data)
        db.commit()

def customer_data(id):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select FirstName from customer ")
        customer = cursor.fetchall()
        return customer

def display_customer_data(FirstName):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from customer where FirstName=?",(FirstName,))
        customer = cursor.fetchone()
        return customer

def display_customer_data(value):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from customer where customerID=?",(value,))
        customer = cursor.fetchone()
        return customer

def delete_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "delete from customer where customerID=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    delete_customer_data("1")
    close = False
    while not close:
        choice = validate_choice()
        if choice == 0:
            close = True
        elif choice == 1:
            FirstName = input("please enter your FirstName: ")
            LastName = input("please enter your LastNname: ")
            values = (1,FirstName,LastName)
            insert_customer_data(values)
        elif choice == 3:
            customer_data()
        elif choice == 5:
           delete_customer_data("1") 
        elif choice == 0:
            close = True
        else:
            print("Hey Listen")
