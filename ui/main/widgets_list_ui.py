from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QGridLayout, QHBoxLayout,
                             QSizePolicy, QSpacerItem)
from PyQt6.QtGui import QFont

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from src.fonts.connect import fonts

from database.connect import database as db

class Ui_Form(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        box = QGridLayout()
        box.setContentsMargins(11, 11, 0, 0)
        box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        box.setSpacing(11)

        widgets = db.get_widgets(0)

        count = 0
        x, y = 0, 0
        while count < len(widgets):
            widget = ListWidget(Widget('', '', lambda a: a, '', lambda a: a))
            box.addWidget(widget, y, x, Qt.AlignmentFlag.AlignTop)
            if x == 2:
                y += 1
                x = 0
            else:
                x += 1
            count += 1

        scroll_box_widget = QWidget()
        scroll_box_widget.setLayout(box)

        scroll_box = QScrollArea()
        scroll_box.setWidgetResizable(True)
        scroll_box.setStyleSheet('''QScrollBar {
                                 border: 1px 4F4F4F solid;
                                 margin-top: 5px;
                                 height: 15px;
                                 }
                                 QScrollBar::handle {
                                 background: #4F4F4F;
                                 border-radius: 10px;
                                 }
                                 QScrollBar::add-page, QScrollBar::sub-page {
                                 background: none;
                                 }
                                 QScrollBar::add-line, QScrollBar::sub-line  {
                                 background: none; }''')
        scroll_box.setWidget(scroll_box_widget)

        layout = QHBoxLayout()
        layout.addWidget(scroll_box)

        self.setLayout(layout)