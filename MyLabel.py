from PyQt6.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QStyle, QFrame, QStyleOptionFrame


class MyLabel(QLabel):
    signal_front_cover_name = pyqtSignal()

    def __init__(self, back, front, parent=None):
        super(MyLabel, self).__init__(parent)

        self.setFrameStyle(QFrame.Shape.Panel + QFrame.Shadow.Raised)
        self.setLineWidth(3)

        self.__str_front = front
        self.pixmap_front = QPixmap(self.__str_front).scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)

        self.show_back = False
        self.pixmap_back = QPixmap(back).scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.pixmap_back)

    def str_front(self):
        return self.__str_front

    def mouseReleaseEvent(self, ev) -> None:
        self.signal_front_cover_name.emit()

    @pyqtSlot()
    def switch(self):
        if self.show_back:
            self.setPixmap(self.pixmap_back)
            self.show_back = False
        else:
            self.setPixmap(self.pixmap_front)
            self.show_back = True

    @pyqtSlot()
    def deactivate(self):
        self.setFrameStyle(QFrame.Shape.Panel + QFrame.Shadow.Sunken)
