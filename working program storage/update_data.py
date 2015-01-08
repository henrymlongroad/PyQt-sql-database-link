import sqlite3

def update_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "update customer set FirstName=?, LastName=? where customerID=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("Peter", "Millard",1)
    update_customer_data(data)
