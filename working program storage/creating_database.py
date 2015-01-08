import sqlite3

def create_table(db_name,table_name,sql):
    #open an existing database or create a new one
    with sqlite3.connect(db_name)as db:
        #create a cursor
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            responce = input("the table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if responce == "y":
                keep_table = False
                print("the {0} table will be recreated - all excisting data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("the existing table will be kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit() # most important line

def main():
    db_name = "tesco's_store.db"
    sql = """create table product
    (ProductID interger,
    name text,
    Price real,
    Primary Key(ProductID))"""
    table_name = "Product"
    create_table(db_name,table_name,sql)

if __name__ == "__main__":
    main()
