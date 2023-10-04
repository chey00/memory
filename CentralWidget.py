import random

from PyQt6.QtWidgets import QWidget, QGridLayout

from MyLabel import MyLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        cards = [MyLabel("ara.jpg"), MyLabel("ara.jpg"), MyLabel("cat.jpg"), MyLabel("cat.jpg"), MyLabel("dog.jpg"),
                 MyLabel("dog.jpg"), MyLabel("fish.jpg"), MyLabel("fish.jpg")]

        random.shuffle(cards)

        for card in cards:
            card.card_clicked.connect(self.handel_clicks)

        layout = QGridLayout(self)
        self.setLayout(layout)

        for i in range(1, 3):
            for j in range(1, 5):
                layout.addWidget(cards.pop(), i, j)

        self.__last_card_clicked = None

    def handel_clicks(self):
        if self.__last_card_clicked is None:
            self.__last_card_clicked = self.sender()
        else:
            if self.__last_card_clicked.get_image_name() == self.sender().get_image_name() and \
                    self.__last_card_clicked is not self.sender():
                self.sender().set_found()
                self.__last_card_clicked.set_found()

            self.__last_card_clicked = None
