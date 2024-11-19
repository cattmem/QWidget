from PyQt6.QtWidgets import (QMainWindow, QWidget, QLabel, QScrollArea,
                             QVBoxLayout,
                             QSizePolicy, QSpacerItem, QGridLayout)

from modules.main_ui import widgets
from modules.widget_data import Widget


class Ui_Form(QWidget):
    def __init__(self, main: QMainWindow) -> None:
        super().__init__()

        self.main = main

        # scroll_box = QScrollArea()
    
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.data_load = widgets.Ui_Form('Загружено', [])
        layout.addWidget(self.data_load)

        self.data_unload = widgets.Ui_Form('Выгружено', [])
        layout.addWidget(self.data_unload)

        # data_unload = widgets.Ui_Form('Выгружено', [])
        # set_forms(get_forms() + data_load)
        # layout.addWidget(data_unload)

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