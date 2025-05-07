from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from startWindow import Ui_startWindow
from selectionLogic import *






class Start(QMainWindow, Ui_startWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Welcome to the Music Player")
        self.selection_window = SelectionLogic()
        self.startButton.clicked.connect(lambda : self.openWindow())

    def openWindow(self) -> None:
        """Opens the selection window after pressing start button"""
        self.selection_window.show()        
