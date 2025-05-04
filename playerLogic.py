import os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from playerWindow import Ui_playerWindow
from PyQt6.QtGui import QShowEvent




class Logic(QMainWindow, Ui_playerWindow):

    mediaPlayer = QMediaPlayer()
    audioOutput = QAudioOutput()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MP3 Music Player")


        self.pauseButton.clicked.connect(lambda : self.pause())
        self.playButton.clicked.connect(lambda : self.play())
        self.forwardButton.clicked.connect(lambda : self.forward())
        self.backButton.clicked.connect(lambda : self.reverse())
    
        self.audioOutput.setVolume(50)
        self.filePath = None #Will be set by loadFile function


    def loadFile(self, filePath : str) -> None:
        """Loads the MP3 file a user inputs on the second window"""
        self.filePath = filePath
        if not os.path.exists(self.filePath):
            print("file doesn't exist")

    def showEvent(self, event : QShowEvent) -> None:
        super().showEvent(event) #overrides the show window event so audio is loaded as soon as the window opens
        Logic.mediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
        Logic.mediaPlayer.setAudioOutput(Logic.audioOutput)
        self.setWindowTitle(f"Now Playing:, {self.filePath}")
        self.play()


    def play(self) -> None:
        """Plays MP3 file"""
        Logic.mediaPlayer.play()

    def pause(self) -> None:
        """Pauses MP3 file"""
        Logic.mediaPlayer.pause()

    def reverse(self) -> None:
        pass

    def forward(self) -> None:
        pass