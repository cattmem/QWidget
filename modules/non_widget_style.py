from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout,
                             QLabel, QSizePolicy)

from src.fonts.connect import fonts


class NoneWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        all_widget = QVBoxLayout()
        all_widget.setContentsMargins(0, 0, 0, 0)
        all_widget.setSpacing(0)
        all_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel('Пусто')
        label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(fonts.side)
        label.setStyleSheet('color: #818181')
        all_widget.addWidget(label)

        self.setStyleSheet('''border: 1px solid #4F4F4F;
                           border-radius: 5px''')
        self.setLayout(all_widget)
        self.setMaximumWidth(144)
        self.setMaximumHeight(200)
