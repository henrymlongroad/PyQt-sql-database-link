from PyQt4.QtCore import*
from PyQt4.QtGui import*

import sys

from sql_connection import*
from display_window import*


class Window(QMainWindow):
    """a basic window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("databases")
        

        #set actions
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.find_product = QAction("find product",self)
        self.show_products = QAction("show products",self)
        self.create_prescription = QAction("create_prescription",self)
        self.show_prescription = QAction("show_prescription",self)
        self.add_Product = QAction("add_product",self)
        self.remove_product = QAction("Remove_product",self)
        
        
        #add menu
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        #add database to the menu bar
        self.database_menu = self.menu.addMenu("Database")
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)
        
        #add products to the menu bar
        self.product_menu = self.menu.addMenu("Products")
        self.product_menu.addAction(self.find_product)
        self.product_menu.addAction(self.show_products)
        

        self.prescription_menu = self.menu.addMenu("Prescription")
        self.prescription_menu.addAction(self.create_prescription)
        self.prescription_menu.addAction(self.show_prescription)
        
        
        #add to toolbar        
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        # apply to main window
        self.addToolBar(self.database_toolbar)
        self.setMenuBar(self.menu)

        #connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.find_product.triggered.connect(self.display_product)
        self.show_products.triggered.connect(self.display_products)

        
    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SqlConnection(path)
        ok = self.connection.open_database()
        print(ok)
        

    def close_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SqlConnection(path)
        ok = self.connection.close_Database()


    def find_products_by_number(self, values):
        pass


    def display_product(self):
        if not hasattr(self,"display_window"):
            self.display_widget = display_window()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_product_by_number
        self.display_widget.display_results_layout()
        

    def display_products(self):
        print("it_works")
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    application.exec_()
