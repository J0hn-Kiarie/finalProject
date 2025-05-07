import os
from PyQt6.QtWidgets import *
from selectionWindow import Ui_selectionWindow
from playerLogic import Logic


class SelectionLogic(QWidget, Ui_selectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Select an MP3 file")
        self.musicLogic = Logic()
        self.selectButton.clicked.connect(lambda : self.saveFile())

    def saveFile(self) -> None:
        """Saves the MP3 file for use in third window, checks if the file exists, then opens the third window"""
        self.fileName = self.entryLineEdit.text()
        if self.fileName.lower().endswith(".mp3") and os.path.exists(self.fileName.lower()):
            self.musicLogic.loadFile(self.fileName)
            self.musicLogic.show()
        else:
            self.entryLineEdit.setText("Enter an mp3 file name please")
        
        

