from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from startWindow import Ui_startWindow
from selectionWindow import Ui_selectionWindow
from selectionLogic import *






class Start(QMainWindow, Ui_startWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Welcome to the Music Player")
        self.selection_window = SelectionLogic()
        self.startButton.clicked.connect(lambda : self.openWindow())

    def openWindow(self):
        self.selection_window.show()        
