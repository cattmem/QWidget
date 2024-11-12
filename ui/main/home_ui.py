from PyQt6.QtWidgets import (QWidget, QLabel, QScrollArea,
                             QVBoxLayout,
                             QSizePolicy, QSpacerItem, QGridLayout)

from modules.main_ui import widgets
from modules.widget_data import Widget


class Ui_Form(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # scroll_box = QScrollArea()
    
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        w = Widget('', '', lambda a: a, '', lambda a: a)

        data = widgets.Ui_Form('Загружено', [w, w, w])
        layout.addWidget(data)
        data = widgets.Ui_Form('Выгружено', [w, w, w, w, w, w])
        layout.addWidget(data)

        spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        # scroll_box = QScrollArea()
        # scroll_box.setWidgetResizable(True)
        # scroll_box.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # scroll_box.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        # scroll_box.setLayout(layout)

        # scroll_box_layout = QGridLayout()
        # scroll_box_layout.addWidget(scroll_box)
        # scroll_box_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)