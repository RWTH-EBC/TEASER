# created June 2015
# by TEASER4 Development Team

from PyQt4.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt

from teaser.gui.controller import Controller


class ZoneUI(QAbstractListModel):
    """ GUI elements for the zones tab """

    def __init__(self, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.Zonenliste = []
        ctrl = Controller()
        # gets all usages for the zone paired with the usage times
        self.listOFUsages = ctrl.fillBoundaryConditions()
        self.usageTimes = ctrl.fillUsageTimes()
        self.selectionOfZones = []
        for index, wert in enumerate(self.listOFUsages):
            usage = wert.Nutzung
            nutzungDecoded = usage.decode('iso-8859-1')
            self.selectionOfZones.append(nutzungDecoded)

    def rowCount(self, parent=QModelIndex()):
        return len(self.Zonenliste)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            label_Flaeche = u" Flaeche:      "
            label_qm = u" m�"
            return QVariant(u" Name:       " + str(self.Zonenliste[index.row()].Name) + "\n" + u" Typ:            " + self.Zonenauswahl[self.Zonenliste[index.row()].Typ] + "\n" + label_Flaeche + str(self.Zonenliste[index.row()].Flaeche) + label_qm)
        else:
            return QVariant()
