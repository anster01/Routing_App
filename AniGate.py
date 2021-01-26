import sys

from PyQt5 import QtWidgets
from user_interface import Window

if __name__ == "__main__":
    #start the application
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_) #exit when the window is closed
