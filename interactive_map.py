from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class InteractiveMap(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(InteractiveMap, self).__init__(*args, **kwargs)

        self.setGeometry(50, 50, 800, 625)
        self.setFixedSize(800, 625)

        self.browser = QWebEngineView()
        self.display_map()
        
    def display_map(self):
        self.setWindowTitle('Interactive Map')
        self.browser.load(QUrl.fromLocalFile("\\graph_route.html"))
        self.setCentralWidget(self.browser)

class InteractiveCrimeMap(InteractiveMap):
    def __init__(self, *args, **kwargs):
        super(InteractiveCrimeMap, self).__init__(*args, **kwargs)

    def display_map(self):
        self.setWindowTitle('Interactive Crime Map')
        self.browser.load(QUrl.fromLocalFile("\\avoid_crime_route.html"))
        self.setCentralWidget(self.browser)

