from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from playerWindow import Ui_playerWindow
from PyQt6.QtGui import QShowEvent, QCloseEvent




class Logic(QMainWindow, Ui_playerWindow):

    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MP3 Music Player")

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.audioOutput.setVolume(50)

        self.pauseButton.clicked.connect(lambda : self.pause())
        self.playButton.clicked.connect(lambda : self.play())
        self.forwardButton.clicked.connect(lambda : self.forward())
        self.backButton.clicked.connect(lambda : self.reverse())
        
        self.playbackBar.setRange(0, 0)
        self.mediaPlayer.positionChanged.connect(self.updateSlider)
        self.mediaPlayer.durationChanged.connect(self.updateDuration)
        self.playbackBar.sliderMoved.connect(self.setPosition)
        self.filePath = None #Will be set by loadFile function




    def loadFile(self, filePath : str) -> None:
        """Loads the MP3 file a user inputs on the second window"""
        self.filePath = filePath


    def showEvent(self, event : QShowEvent) -> None:
        """Overrides the show window event so audio is loaded and plays as soon as the window opens"""
        super().showEvent(event)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
        self.setWindowTitle(f"Now Playing:, {self.filePath}")
        self.play()

    def closeEvent(self, event : QCloseEvent) -> None:
        """Overrides the close window event so the audio stops when the user closes the music player window"""
        super().closeEvent(event)
        self.stop()


    def play(self) -> None:
        """Plays MP3 file and disables the play buttons"""
        self.mediaPlayer.play()
        self.pauseButton.setEnabled(True)
        self.playButton.setDisabled(False)


    def pause(self) -> None:
        """Pauses MP3 file and disables the pause button"""
        self.mediaPlayer.pause()
        self.pauseButton.setDisabled(True)
        self.playButton.setEnabled(True)


    def reverse(self) -> None:
        pass


    def forward(self) -> None:
        pass

    def updateSlider(self, position : int) -> None:
        """Syncs the slider's position to the current playback position"""
        self.playbackBar.setValue(position)

    def updateDuration(self, duration : int) -> None:
        """Changes the slider's range to match the duration of the song"""
        self.playbackBar.setRange(0, duration)

    def setPosition(self, position : int) -> None:
        """Syncs the playback position with the slider"""
        self.mediaPlayer.setPosition(position)
    

        
