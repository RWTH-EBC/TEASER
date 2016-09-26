# created June 2015
# by TEASER4 Development Team

from PyQt4 import QtGui


class TrackableItem (QtGui.QStandardItem):

    def __init__(self, text, internal_id):
        QtGui.QStandardItem.__init__(self, text)

        self.internal_id = internal_id
        self.setText(text)
