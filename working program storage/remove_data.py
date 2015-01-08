from PyQt4.QtGui import*
from PyQt4.QtCore import*
from PyQt4.QtSql import*

import sys

from edit_database import*

class display_window(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_widget = QWidget()
        self.display_remove_data_layout()
        
        

        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    application.exec_()
