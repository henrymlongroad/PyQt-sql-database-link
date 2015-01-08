import sqlite3

def insert_customer_data(values):
    
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "insert into customer (CustomerID, FirstName, LastName) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    customer = (1, "susannah", "Mason")
    insert_customer_data(customer)
