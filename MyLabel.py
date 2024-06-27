import typing

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from PyQt6.uic.properties import QtGui


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mouseReleaseEvent(self, ev) -> None:
        pixmap_cover = QPixmap("porsche.jpeg").scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(pixmap_cover)
