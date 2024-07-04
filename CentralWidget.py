import random

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout

from MyLabel import MyLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.last_clicked_front_cover = None

        list_of_front_covers = ["Audi.jpg", "BMW.jpg", "Mercedes.jpg", "Porsche.jpeg"] * 2
        random.shuffle(list_of_front_covers)

        list_of_cards = list() # []
        number_of_cards = 8
        for i in range(number_of_cards):
            list_of_cards.append(MyLabel("cover.jpg", list_of_front_covers[i], parent))

        for i in range(number_of_cards):
            list_of_cards[i].signal_front_cover_name.connect(self.handle_cards)

        layout = QGridLayout()

        for i in range(number_of_cards):
            layout.addWidget(list_of_cards[i], int(2 * i / number_of_cards), i % 4)

        self.setLayout(layout)

    @pyqtSlot(str)
    def handle_cards(self, front_cover_name):
        print(front_cover_name)

        if self.last_clicked_front_cover:
            if self.last_clicked_front_cover == front_cover_name:
                print("Match!")
                
            self.last_clicked_front_cover = None
        else:
            self.last_clicked_front_cover = front_cover_name
