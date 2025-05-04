from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from selectionWindow import Ui_selectionWindow
from playerWindow import Ui_playerWindow


class SelectionLogic(QWidget, Ui_selectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Select an MP4 file")
        self.musicWindow = QWidget()
        self.musicUi = Ui_playerWindow()
        self.musicUi.setupUi(self.musicWindow)
        self.selectButton.clicked.connect(lambda : self.openWindow())

    
    def openWindow(self):
        self.musicWindow.show()