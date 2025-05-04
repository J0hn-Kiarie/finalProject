from PyQt6 import *
from startMenuLogic import *
from startWindow import *
from playerLogic import *
from selectionLogic import *

def main():
    application = QApplication([])
    window = Start()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()