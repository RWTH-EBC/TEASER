# created September 2015
# by TEASER4 Development Team


import sys
from PyQt4.QtGui import QApplication
from teaser.gui.mainui import MainUI


def startGUI():
    """starts the GUI

    The GUI is a beta relaese, not tested and probably buggy, please consider
    this when using the GUI. If you find any bugs, please report them :)
    """

    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    app.exec_()
if __name__ == '__main__':
    startGUI()
