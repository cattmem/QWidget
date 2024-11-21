from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt6.QtGui import QFont


class Main(QWidget):
    ''' timer '''

    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(300, 250)

        self.layout_timer = QVBoxLayout()
        self.layout_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_timer = QLabel('00:00:00')
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPixelSize(30)
        font.setBold(True)
        self.label_timer.setFont(font)
        self.label_timer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.layout_timer.addWidget(self.label_timer)

        self.setLayout(self.layout_timer)