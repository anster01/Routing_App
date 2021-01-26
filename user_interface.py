import sys

from PyQt5 import QtCore, QtWidgets
from autocomplete_address import autocomplete_address
from show_instructions import show_instructions_window
from network_functions import Network_Functions

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.my_network = Network_Functions()
        
        self.setGeometry(50,50,500,300)
        self.setFixedSize(500, 300)
        self.setWindowTitle("AniGate")

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QtWidgets.QGridLayout(central_widget)

        self.strList_start = []
        self.strList_end = []
        self.avoid_crime_bool = False
        
        self.help_btn = QtWidgets.QPushButton('Help', self)
        self.help_btn.clicked.connect(self.show_instructions)
        self.help_btn.resize(self.help_btn.minimumSizeHint())
        grid_layout.addWidget(self.help_btn, 0, 2)

        grid_layout.addWidget(QtWidgets.QLabel("Start Location", self), 1, 0)
        
        self.start_entry = QtWidgets.QLineEdit(self)
        self.start_entry.textChanged.connect(self.autocomplete_entry)
        self.completer_start_entry = QtWidgets.QCompleter(self.strList_start, self)
        self.completer_start_entry.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer_start_entry.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.start_entry.setCompleter(self.completer_start_entry)
        grid_layout.addWidget(self.start_entry, 1, 1)

        self.start_clear = QtWidgets.QPushButton("Clear", self)
        self.start_clear.clicked.connect(self.clear_start_entry)
        self.start_clear.resize(self.start_clear.minimumSizeHint())
        grid_layout.addWidget(self.start_clear, 1, 2)

        self.swap_btn = QtWidgets.QPushButton("Swap", self)
        self.swap_btn.clicked.connect(self.swap_entry)
        self.swap_btn.resize(self.swap_btn.minimumSizeHint())
        grid_layout.addWidget(self.swap_btn, 2, 0)

        grid_layout.addWidget(QtWidgets.QLabel("End Location", self), 3, 0)
        
        self.end_entry = QtWidgets.QLineEdit(self)
        self.end_entry.textChanged.connect(self.autocomplete_entry)
        self.completer_end_entry = QtWidgets.QCompleter(self.strList_end, self)
        self.completer_end_entry.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer_end_entry.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.end_entry.setCompleter(self.completer_end_entry)
        grid_layout.addWidget(self.end_entry, 3, 1)

        self.end_clear = QtWidgets.QPushButton("Clear", self)
        self.end_clear.clicked.connect(self.clear_end_entry)
        self.end_clear.resize(self.end_clear.minimumSizeHint())
        grid_layout.addWidget(self.end_clear, 3, 2)

        self.chk_box = QtWidgets.QCheckBox('Avoid High Crime', self)
        self.chk_box.stateChanged.connect(self.avoid_high_crime)
        grid_layout.addWidget(self.chk_box, 4, 0)

        self.calc_btn = QtWidgets.QPushButton("Calculate", self)
        self.calc_btn.clicked.connect(self.start_calculation)
        self.calc_btn.resize(self.calc_btn.minimumSizeHint())
        self.calc_btn.setEnabled(False)
        grid_layout.addWidget(self.calc_btn, 4, 1)
        
        quit_btn = QtWidgets.QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close_application)
        quit_btn.resize(quit_btn.minimumSizeHint())
        grid_layout.addWidget(quit_btn, 4, 2)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.resize(self.progress_bar.minimumSizeHint())
        grid_layout.addWidget(self.progress_bar, 5, 1)
        
        self.show()

    def show_instructions(self):
        self.window = show_instructions_window()

    def clear_start_entry(self):
        self.start_entry.setText('')
        self.completer_start_entry = QtWidgets.QCompleter([], self)
        self.start_entry.setCompleter(self.completer_start_entry)

    def clear_end_entry(self):
        self.end_entry.setText('')
        self.completer_end_entry = QtWidgets.QCompleter([], self)
        self.end_entry.setCompleter(self.completer_end_entry)

    def close_application(self):
        sys.exit()

    def swap_entry(self):
        start, end = self.start_entry.text(), self.end_entry.text()
        self.start_entry.setText(end)
        self.end_entry.setText(start)

    def avoid_high_crime(self, state):
        if state == QtCore.Qt.Checked:
            self.avoid_crime_bool = True
        else:
            self.avoid_crime_bool = False

    def autocomplete_entry(self):
        if self.start_entry.text() and self.end_entry.text() and self.start_entry.text().strip() != '' and self.end_entry.text().strip() != '':
            self.calc_btn.setEnabled(True)
        else:
            self.calc_btn.setEnabled(False)

        if self.start_entry.text()[-1:] == ' ' and self.start_entry.text().strip() != '':
            self.strList_start = autocomplete_address(self.start_entry.text())
            self.completer_start_entry = QtWidgets.QCompleter(self.strList_start, self)
            self.completer_start_entry.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.completer_start_entry.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
            self.start_entry.setCompleter(self.completer_start_entry)

        if self.end_entry.text()[-1:] == ' ' and self.end_entry.text().strip() != '':
            self.strList_end = autocomplete_address(self.end_entry.text())
            self.completer_end_entry = QtWidgets.QCompleter(self.strList_end, self)
            self.completer_end_entry.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.completer_end_entry.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
            self.end_entry.setCompleter(self.completer_end_entry)

    def start_calculation(self):
        self.completed = 0
        self.progress_bar.show()
        self.progress_bar.setValue(self.completed)
        
        self.my_network.addresses = []
        self.my_network.routes = []
        self.my_network.nearest_nodes = []
        self.my_network.coords = []
        self.my_network.route_lengths = []
        self.crime_rating = []

        self.completed = 5
        self.progress_bar.setValue(self.completed)
        
        self.my_network.addresses.append(self.start_entry.text())
        self.my_network.addresses.append(self.end_entry.text())
        self.my_network.check_input()

        self.completed = 20
        self.progress_bar.setValue(self.completed)
        
        if False not in self.my_network.coords:
            self.calc_btn.setEnabled(False)
            self.start_entry.setEnabled(False)
            self.end_entry.setEnabled(False)
            self.chk_box.setEnabled(False)
            self.swap_btn.setEnabled(False)
            self.start_clear.setEnabled(False)
            self.end_clear.setEnabled(False)
            self.help_btn.setEnabled(False)
            
            self.my_network.FindNearestNode()
            self.completed = 50
            self.progress_bar.setValue(self.completed)
            if not self.avoid_crime_bool:
                try:
                    self.my_network.FindShortestPath('length')
                    self.completed = 90
                    self.progress_bar.setValue(self.completed)
                    self.window = self.my_network.DisplayMap()
                    self.completed = 100
                    self.progress_bar.setValue(self.completed)
                except:
                    QtWidgets.QMessageBox.about(self, "Error" ,"Could not find shortest path.")
                    self.completed = 0
                    self.progress_bar.setValue(self.completed)
            else:
                try:
                    self.my_network.FindShortestPath('length')
                    self.completed = 65
                    self.progress_bar.setValue(self.completed)
                    self.my_network.FindShortestSafePath('length')
                    self.completed = 80
                    self.progress_bar.setValue(self.completed)
                    self.my_network.GetCrimeRating()
                    self.my_network.FindRouteLengths()
                    self.completed = 90
                    self.progress_bar.setValue(self.completed)
                    self.window = self.my_network.AvoidHighCrime()
                    self.completed = 100
                    self.progress_bar.setValue(self.completed)
                except:
                    QtWidgets.QMessageBox.about(self, "Error" ,"Could not find shortest path.")
                    self.completed = 0
                    self.progress_bar.setValue(self.completed)
                
            self.calc_btn.setEnabled(True)
            self.start_entry.setEnabled(True)
            self.end_entry.setEnabled(True)
            self.chk_box.setEnabled(True)
            self.swap_btn.setEnabled(True)
            self.start_clear.setEnabled(True)
            self.end_clear.setEnabled(True)
            self.help_btn.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self, "Error" ,"Make sure the locations entered are within the boundaries and try again.")
            self.completed = 0
            self.progress_bar.setValue(self.completed)
