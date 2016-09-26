# created June 2015
# by TEASER4 Development Team

from PyQt4.Qt import QItemDelegate
from PyQt4.QtGui import QFont, QPen, QColor, QStyle, QBrush
from PyQt4.QtCore import Qt, QSize


class ListViewZonesFiller(QItemDelegate):

    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

        # Set Color and font style
        self.font = QFont("Helvetica", 9)  # , QFont.Bold
        self.pencil = QPen(QColor(Qt.black))
        self.height = 45
        self.weight = 170

    def sizeHint(self, option, index):
        return QSize(self.weight, self.height)

    def paint(self, painter, option, index):
        painter.save()

        # set background color and text color
        if option.state & QStyle.State_Selected:
            painter.setBrush(QBrush(QColor("#FF9999")))
        else:
            painter.setBrush(QBrush(Qt.white))
        painter.drawRect(option.rect)
        painter.setPen(QPen(Qt.black))
        painter.setFont(self.font)
        text = index.data(Qt.DisplayRole)
        try:
            painter.drawText(option.rect, Qt.AlignLeft, text.toString())
        except:
            painter.drawText(option.rect, Qt.AlignLeft, text)
        painter.restore()
