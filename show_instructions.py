from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class InstructionsWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(InstructionsWindow, self).__init__(*args, **kwargs)

        self.setGeometry(50, 50, 800, 625)
        self.setFixedSize(800, 625)

        self.setWindowTitle('How To Use')

        self.browser = QWebEngineView()

        self.browser.load(QUrl.fromLocalFile("\\instructions.html"))
        self.setCentralWidget(self.browser)

def show_instructions_window():
    instructions_window = InstructionsWindow()
    instructions_window.show()
    return instructions_window
