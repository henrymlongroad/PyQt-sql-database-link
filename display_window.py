from PyQt4.QtGui import*
from PyQt4.QtCore import*
from PyQt4.QtSql import*

class display_window(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_widget = QWidget()
        self.display_results_Layout()
        

    def display_results_layout(self):
        
        self.results_layout.addWidget(self.results_table)
        
        self.results_widget.set_layout(self.result_layout)
        self.stacked_layout.addWidget(self.results_widget)
    
        
    def show_results(self):
        if not self.model or not isinstance(self.model,"QSqlQueryModel"):
            self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()

    def show_table(self):
        pass
    
