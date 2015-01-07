import sqlite3

def display_customer_data():
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select FirstName from customer")
        customer = cursor.fetchall()
        return customer

def customer_data(id):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from customer where customerID=?",(id,))
        customer = cursor.fetchone()
        return customer

if __name__ == "__main__":
    customer = display_customer_data()
    print(customer)
    customer = customer_data(1)
    print(customer)
