from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QSizePolicy, QSpacerItem)
from PyQt6.QtGui import QFont

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from src.fonts.connect import fonts


class Ui_Form(QWidget):
    def __init__(self, title_form: str, widgets_data: list) -> None:
        super().__init__()
    
        box = QVBoxLayout()
        box.setContentsMargins(19, 15, 0, 15)
        box.setSpacing(11)

        title_label = QLabel(title_form)
        title_label.setFont(fonts.title)
        title_label.setStyleSheet('color: #DBDBDB')
        box.addWidget(title_label)
        
        # ------------------
        widget_list_layout = QHBoxLayout()
        widget_list_layout.setSpacing(11)
        widget_list_layout.setContentsMargins(0, 0, 0, 0)

        for widget in widgets_data:
            widget_layout = QHBoxLayout()
            widget_layout.setContentsMargins(0, 0, 0, 0)
            widget_layout.setSpacing(0)
            widget_layout.addWidget(ListWidget(widget))
            widget_list_layout.addLayout(widget_layout)

        spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        widget_list_layout.addItem(spacer)

        scroll_box = QScrollArea()
        scroll_box.setWidgetResizable(True)
        scroll_box.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        box_widget = QWidget()
        box_widget.setLayout(widget_list_layout)

        scroll_box.setWidget(box_widget)
        scroll_box_layout = QHBoxLayout()
        scroll_box_layout.addWidget(scroll_box)
        scroll_box_layout.setContentsMargins(0, 0, 0, 0)
        box.addLayout(scroll_box_layout)
        self.setLayout(box)