import sqlite3

def select_all_products():
    with sqlite3.connect("tesco's_store.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("tesco's_store.db"):
        cursor = db.cursor()
        sql = """select * from product where ProductID-?""",(id,)
        cursor.execute(sql)
        product = cursor.fetchone()
        return product


if __name__ =="__main__":
    products = select_all_products()
    print(products)
    product = select_product(1)
    print(product)
