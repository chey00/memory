from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, back, front, parent=None):
        super(MyLabel, self).__init__(parent)

        self.str_front = front
        self.pixmap_front = QPixmap(front).scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)

        self.show_back = False
        self.pixmap_back = QPixmap(back).scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.pixmap_back)

    def mouseReleaseEvent(self, ev) -> None:
        self.switch()

    @pyqtSlot()
    def switch(self):
        if self.show_back:
            self.setPixmap(self.pixmap_back)
            self.show_back = False
        else:
            self.setPixmap(self.pixmap_front)
            self.show_back = True
