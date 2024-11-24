from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QSizePolicy, QSpacerItem)

from modules.main_ui import widgets


class Ui_Form(QWidget):
    def __init__(self, main: QMainWindow) -> None:
        super().__init__()

        self.main = main

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.data_load = widgets.Ui_Form('Загружено', [])
        layout.addWidget(self.data_load)

        self.data_unload = widgets.Ui_Form('Выгружено', [])
        layout.addWidget(self.data_unload)

        spacer = QSpacerItem(
            1,
            1,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        self.setLayout(layout)
