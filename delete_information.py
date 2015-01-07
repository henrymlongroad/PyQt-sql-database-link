import sqlite3

def delete_customer_data(data):
    with sqlite3.connect("pharmacy_database.db") as db:
        cursor = db.cursor()
        sql = "delete from customer where customerID=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = (1,)
    delete_customer_data(data)
    
