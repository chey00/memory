from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGridLayout

from MyLabel import MyLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        list_of_cards = list() # []
        number_of_cards = 8
        for i in range(number_of_cards):
            list_of_cards.append(MyLabel("cover.jpg", "BMW.jpg", parent))

        layout = QGridLayout()

        for i in range(number_of_cards):
            layout.addWidget(list_of_cards[i], int(2 * i / number_of_cards), i % 4)

        self.setLayout(layout)

