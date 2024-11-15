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
        box.setContentsMargins(0, 15, 0, 0)
        box.setSpacing(11)

        title_label = QLabel(title_form)
        title_label.setFont(fonts.title)
        title_label.setStyleSheet('color: #DBDBDB; margin-left: 15px')
        box.addWidget(title_label)
        
        # ------------------
        widget_list_layout = QHBoxLayout()
        widget_list_layout.setSpacing(11)
        widget_list_layout.setContentsMargins(0, 0, 0, 0)

        spacer = QLabel()
        spacer.setFixedSize(8, 1)
        widget_list_layout.addWidget(spacer)

        for widget in widgets_data:
            widget_layout = QHBoxLayout()
            widget_layout.setContentsMargins(0, 0, 0, 0)
            widget_layout.setSpacing(0)
            widget_layout.addWidget(ListWidget(widget))

            widget_list_layout.addLayout(widget_layout)
        
        spacer = QLabel()
        spacer.setFixedSize(8, 1)
        widget_list_layout.addWidget(spacer)

        spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        widget_list_layout.addItem(spacer)

        box_widget = QWidget()
        box_widget.setLayout(widget_list_layout)
        box_widget.setFixedHeight(200)

        scroll_box = QScrollArea()
        scroll_box.setWidgetResizable(True)
        scroll_box.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
                                 background: none; }
                                 QScrollBar::up-arrow, QScrollBar::down-arrow {
                                 background: none;
                                 }''')
        scroll_box.setFixedHeight(217)

        scroll_box.setWidget(box_widget)
        scroll_box_layout = QHBoxLayout()
        scroll_box_layout.addWidget(scroll_box)
        scroll_box_layout.setContentsMargins(0, 0, 0, 0)
        box.addLayout(scroll_box_layout)
        self.setLayout(box)