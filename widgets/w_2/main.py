from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QPushButton
from PyQt6.QtGui import QFont


class Main(QWidget):
    ''' секундомер '''

    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(300, 250)

        self.box = QHBoxLayout()
        self.is_work = False

        self.buttons = QVBoxLayout()
        self.manage_btn = QPushButton('-')
        self.manage_btn.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding)
        self.manage_btn.setFixedWidth(25)
        self.manage_btn.clicked.connect(self.manage)
        self.buttons.addWidget(self.manage_btn)

        self.clear_btn = QPushButton('C')
        self.clear_btn.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding)
        self.clear_btn.setFixedWidth(25)
        self.clear_btn.clicked.connect(self.clear)
        self.buttons.addWidget(self.clear_btn)

        self.box.addLayout(self.buttons)

        self.layout_timer = QVBoxLayout()
        self.layout_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time = QTime(0, 0, 0)
        self.label_timer = QLabel(self.time.toString('hh:mm:ss'))
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        font = QFont()
        font.setPixelSize(50)
        font.setBold(True)

        self.label_timer.setFont(font)
        self.label_timer.setStyleSheet('color: #DBDBDB')
        self.label_timer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)

        self.layout_timer.addWidget(self.label_timer)

        self.box.addLayout(self.layout_timer)

        self.setLayout(self.box)

    def update(self) -> None:
        if self.is_work:
            self.time = self.time.addSecs(1)
            self.label_timer.setText(self.time.toString('hh:mm:ss'))

    def manage(self) -> None:
        if self.manage_btn.text() == '-':
            self.is_work = True
            self.manage_btn.setText('+')
        else:
            self.is_work = False
            self.manage_btn.setText('-')

    def clear(self) -> None:
        self.time = QTime(0, 0, 0)
        self.label_timer.setText(self.time.toString('hh:mm:ss'))
        self.timer.stop()
        self.timer.start(1000)
