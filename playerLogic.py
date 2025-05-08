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


    #function by ChatGPT
    def showEvent(self, event : QShowEvent) -> None:
        """Overrides the show window event so audio is loaded and plays as soon as the window opens"""
        super().showEvent(event)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
        self.setWindowTitle(f"Now Playing: {self.filePath}")
        self.play()

    def closeEvent(self, event : QCloseEvent) -> None:
        """Overrides the close window event so the audio stops when the user closes the music player window"""
        super().closeEvent(event)
        self.pause()


    def msToSeconds(self, ms : int) -> int:
        """Takes the time of the file in milliseconds and returns the time in seconds"""
        seconds = ms // 1000
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes:02}:{remaining_seconds:02}"

    def play(self) -> None:
        """Plays MP3 file and disables the play button"""
        self.mediaPlayer.play()
        self.pauseButton.setEnabled(True)
        self.playButton.setDisabled(True)


    def pause(self) -> None:
        """Pauses MP3 file and disables the pause button"""
        self.mediaPlayer.pause()
        self.pauseButton.setDisabled(True)
        self.playButton.setEnabled(True)


    def reverse(self) -> None:
        newPosition = max(0, self.mediaPlayer.position() - self.mediaPlayer.duration())
        self.mediaPlayer.setPosition(newPosition)
        


    def forward(self) -> None:
        newPosition = min(self.mediaPlayer.duration(), self.mediaPlayer.position() + 5000)
        self.mediaPlayer.setPosition(newPosition)
        


    def updateSlider(self, position : int) -> None:
        """Syncs the time and slider's position to the current playback position"""
        self.playbackBar.setValue(position)
        self.currentPlayback.setText(self.msToSeconds(self.mediaPlayer.position()))

    def updateDuration(self, duration : int) -> None:
        """Changes the time and slider's range to match the duration of the song"""
        self.playbackBar.setRange(0, duration)
        self.totalLength.setText(self.msToSeconds(self.mediaPlayer.duration()))

    def setPosition(self, position : int) -> None:
        """Syncs the playback position with the slider"""
        self.mediaPlayer.setPosition(position)
    

        
