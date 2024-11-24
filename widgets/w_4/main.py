from PyQt6.QtWidgets import (QWidget, QVBoxLayout,
                             QSizePolicy, QLabel)


class Main(QWidget):
    ''' тест '''

    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel('test screen widget')
        self.label.setContentsMargins(0, 0, 0, 0)
        self.label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)

        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
