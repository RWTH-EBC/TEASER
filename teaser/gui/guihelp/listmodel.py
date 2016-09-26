# created June 2015
# by TEASER4 Development Team

from PyQt4.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt


class ListModel(QAbstractListModel):
    '''
    QAbstractListModel is a nice interface for 1D Lists but since it is an abstract class we must subclass it which is where this class comes from.
    '''

    def __init__(self, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.listOfZonesForDisplay = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.listOfZonesForDisplay)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant("test")
        else:
            return QVariant("test1")
