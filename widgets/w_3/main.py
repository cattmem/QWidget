from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout_test = QVBoxLayout()
        self.label_test = QLabel('345')
        self.layout_test.addWidget(self.label_test)

        self.setLayout(self.layout_test)