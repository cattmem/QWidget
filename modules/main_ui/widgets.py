from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QSizePolicy, QSpacerItem)
from PyQt6.QtGui import QFont

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from src.fonts.connect import fonts

from modules.non_widget_style import NoneWidget


class Ui_Form(QWidget):
    def __init__(self, title_form: str, widgets_data: list | None = []) -> None:
        super().__init__()
    
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0, 15, 0, 0)
        self.box.setSpacing(11)

        title_label = QLabel(title_form)
        title_label.setFont(fonts.title)
        title_label.setStyleSheet('color: #DBDBDB; margin-left: 15px')
        self.box.addWidget(title_label)

        self.widget_list_layout = QHBoxLayout()
        self.widget_list_layout.setSpacing(11)
        self.widget_list_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.widget_list_layout.setContentsMargins(0, 0, 0, 0)
        
        self.update(widgets_data)

        self.box_widget = QWidget()
        self.box_widget.setLayout(self.widget_list_layout)
        self.box_widget.setFixedHeight(200)
        
        # ------------------

        self.scroll_box = QScrollArea()
        self.scroll_box.setWidgetResizable(True)
        self.scroll_box.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_box.setStyleSheet('''QScrollArea {
                                 border: 0;
                                 }
                                 QScrollBar {
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
        self.scroll_box.setFixedHeight(217)

        self.scroll_box.setWidget(self.box_widget)
        self.scroll_box_layout = QHBoxLayout()
        self.scroll_box_layout.addWidget(self.scroll_box)
        self.scroll_box_layout.setContentsMargins(0, 0, 0, 0)
        self.box.addLayout(self.scroll_box_layout)
        self.setLayout(self.box)
    
    def update(self, widgets_data: list) -> None:
        while self.widget_list_layout.count():
            w = self.widget_list_layout.itemAt(0).widget()
            self.widget_list_layout.removeWidget(w)
            del w
        
        widgets = widgets_data.copy()

        spacer = QLabel()
        spacer.setFixedSize(8, 1)
        self.widget_list_layout.addWidget(spacer)

        if not widgets:
            self.widget_list_layout.addWidget(NoneWidget())
        else:
            for widget in widgets:
                self.widget_list_layout.addWidget(ListWidget(widget))
    
        
        #spacer = QLabel()
        #spacer.setFixedSize(8, 1)
        #self.widget_list_layout.addWidget(spacer)