from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QGridLayout,
                             QSizePolicy, QSpacerItem)
from PyQt6.QtGui import QFont

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from src.fonts.connect import fonts


class Ui_Form(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        box = QGridLayout()
        box.setContentsMargins(19, 19, 0, 0)
        box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        box.setSpacing(11)

        for y in range(3):
            for x in range(3):
                test = Widget('', '', lambda a: a, '', lambda a: a)
                w = ListWidget(test)

                print(x, y)
                box.addWidget(w, x, y)

        self.setLayout(box)