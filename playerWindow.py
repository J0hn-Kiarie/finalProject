# Form implementation generated from reading ui file 'playerWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_playerWindow(object):
    def setupUi(self, playerWindow):
        playerWindow.setObjectName("playerWindow")
        playerWindow.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(playerWindow.sizePolicy().hasHeightForWidth())
        playerWindow.setSizePolicy(sizePolicy)
        playerWindow.setMinimumSize(QtCore.QSize(400, 200))
        playerWindow.setMaximumSize(QtCore.QSize(400, 200))
        self.playbackBar = QtWidgets.QSlider(parent=playerWindow)
        self.playbackBar.setGeometry(QtCore.QRect(20, 50, 361, 22))
        self.playbackBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.playbackBar.setObjectName("playbackBar")
        self.backButton = QtWidgets.QPushButton(parent=playerWindow)
        self.backButton.setGeometry(QtCore.QRect(30, 90, 93, 28))
        self.backButton.setObjectName("backButton")
        self.playButton = QtWidgets.QPushButton(parent=playerWindow)
        self.playButton.setGeometry(QtCore.QRect(150, 90, 93, 28))
        self.playButton.setObjectName("playButton")
        self.forwardButton = QtWidgets.QPushButton(parent=playerWindow)
        self.forwardButton.setGeometry(QtCore.QRect(270, 90, 93, 28))
        self.forwardButton.setObjectName("forwardButton")
        self.pauseButton = QtWidgets.QPushButton(parent=playerWindow)
        self.pauseButton.setGeometry(QtCore.QRect(150, 140, 93, 28))
        self.pauseButton.setObjectName("pauseButton")
        self.currentPlayback = QtWidgets.QLabel(parent=playerWindow)
        self.currentPlayback.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.currentPlayback.setObjectName("currentPlayback")
        self.totalLength = QtWidgets.QLabel(parent=playerWindow)
        self.totalLength.setGeometry(QtCore.QRect(320, 30, 55, 16))
        self.totalLength.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.totalLength.setObjectName("totalLength")

        self.retranslateUi(playerWindow)
        QtCore.QMetaObject.connectSlotsByName(playerWindow)

    def retranslateUi(self, playerWindow):
        _translate = QtCore.QCoreApplication.translate
        playerWindow.setWindowTitle(_translate("playerWindow", "Form"))
        self.backButton.setText(_translate("playerWindow", "Back"))
        self.playButton.setText(_translate("playerWindow", "Play"))
        self.forwardButton.setText(_translate("playerWindow", "Forward"))
        self.pauseButton.setText(_translate("playerWindow", "Pause"))
        self.currentPlayback.setText(_translate("playerWindow", "TextLabel"))
        self.totalLength.setText(_translate("playerWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playerWindow = QtWidgets.QWidget()
    ui = Ui_playerWindow()
    ui.setupUi(playerWindow)
    playerWindow.show()
    sys.exit(app.exec())
