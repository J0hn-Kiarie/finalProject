from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from selectionWindow import Ui_selectionWindow
from playerWindow import Ui_playerWindow
from playerLogic import Logic


class SelectionLogic(QWidget, Ui_selectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Select an MP3 file")
        self.musicUi = Ui_playerWindow()
        self.musicLogic = Logic()
        self.musicUi.setupUi(self.musicLogic)
        self.selectButton.clicked.connect(lambda : self.saveFile())

    def saveFile(self) -> None:
        """Saves the MP3 file for use in third window, then opens the third window"""
        self.fileName = self.entryLineEdit.text()
        if self.fileName.lower().endswith(".mp3"):
            self.musicLogic.loadFile(self.fileName)
            self.musicLogic.show()
        else:
            self.entryLineEdit.setText("Enter an mp3 file name please")
        
        

