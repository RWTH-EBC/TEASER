# created September 2015
# by TEASER4 Development Team


import sys
from PyQt4.QtGui import QApplication
from teaser.GUI.MainUI import MainUI


class GUIStart(object):
    """ General program class. Starts the program and contains
    information about the build version """

    def __init__(self, name, version, date):
        self.name = "TEASER4"
        self.version = "0.1.0"
        self.date = "22.10.2015"


def startGUI():
    # Startet die Eingabemaske
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    app.exec_()

startGUI()

