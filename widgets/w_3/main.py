from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(300, 250)

        self.layout_test = QVBoxLayout()
        self.label_test = QLabel('test')
        self.layout_test.addWidget(self.label_test)

        self.setLayout(self.layout_test)