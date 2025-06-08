# my_window.py
from PySide6.QtWidgets import QWidget, QGridLayout

class My_window_creator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Clicker")
        self.setFixedSize(640, 480)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.row = 0
        self.col = 0

    def add_widget(self, widget, row=None, col=None, rowspan=1, colspan=1):
        if row is None or col is None:
            self.layout.addWidget(widget, self.row, self.col, rowspan, colspan)
            self.row += 1
        else:
            self.layout.addWidget(widget, row, col, rowspan, colspan)
