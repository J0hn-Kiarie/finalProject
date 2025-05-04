import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *
from selectionLogic import *
from playerWindow import Ui_playerWindow




class Logic(QMainWindow, Ui_playerWindow):

    mediaPlayer = QMediaPlayer()
    audioOutput = QAudioOutput()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MP4 Music Player")
        self.pauseButton.clicked.connect(lambda : self.pause())
        self.playButton.clicked.connect(lambda : self.play())
        self.forwardButton.clicked.connect(lambda : self.forward())
        self.backButton.clicked.connect(lambda : self.reverse())


    def play(self):
        Logic.mediaPlayer.play()

    def pause(self):
        Logic.mediaPlayer.pause()

    def reverse(self):
        pass

    def forward(self):
        pass