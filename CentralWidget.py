import random

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout

from MyLabel import MyLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.last_sender = None

        list_of_front_covers = ["Audi.jpg", "BMW.jpg", "Mercedes.jpg", "Porsche.jpeg"] * 2
        random.shuffle(list_of_front_covers)

        list_of_cards = list()
        number_of_cards = 8
        for i in range(number_of_cards):
            list_of_cards.append(MyLabel("cover.jpg", list_of_front_covers[i], parent))

        for i in range(number_of_cards):
            list_of_cards[i].signal_front_cover_name.connect(self.handle_cards)

        layout = QGridLayout()

        for i in range(number_of_cards):
            layout.addWidget(list_of_cards[i], int(2 * i / number_of_cards), i % 4)

        self.setLayout(layout)

    @pyqtSlot()
    #  Erweitern Sie den Slot so, dass die Karte für eine Sekunde aufgedeckt bleibt.
    def handle_cards(self):
        self.sender().switch()

        if self.last_sender:
            if self.last_sender == self.sender():
                return

            elif self.last_sender.str_front() == self.sender().str_front():
                self.sender().deactivate()
                self.last_sender.deactivate()

                self.sender().signal_front_cover_name.disconnect(self.handle_cards)
                self.last_sender.signal_front_cover_name.disconnect(self.handle_cards)

                self.last_sender = None
            else:
                self.sender().switch()
                self.last_sender.switch()

                self.last_sender = None
        else:
            self.last_sender = self.sender()
