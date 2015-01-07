from PyQt4.QtSql import*
from PyQt4.QtCore import*

class SqlConnection:
    """this connects to the database"""
    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            close_database()
        
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok = self.db.open()
        return opened_ok

    def find_product_by_number(self):
        cursor = db.cursor()
        cursor.execute("select ProductName from customer ")
        customer = cursor.fetchall()
        
    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self,event):
        self.close_database()

