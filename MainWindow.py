from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        memory = CentralWidget(parent)

        self.setCentralWidget(memory)

        self.setWindowTitle("Memory")