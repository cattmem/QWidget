from functools import partial

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel,
                             QSizePolicy, QMenu)
from PyQt6.QtGui import QPainter, QAction

from modules.widget_data import Widget

from src.fonts.connect import fonts


class ListWidget(QWidget):
    TYPES = {
        0: 'W',
        1: 'S'
    }

    def __init__(self, widget_data: Widget) -> None:
        super().__init__()
        self.widget_data = widget_data

        all_widget = QVBoxLayout()
        all_widget.setContentsMargins(0, 0, 0, 0)
        all_widget.setSpacing(0)
        ##
        self.preview = QLabel()
        self.preview.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.preview.setMaximumWidth(144)
        self.preview.setStyleSheet('''margin: 0;
                                   padding: 0;
                                   border-top-left-radius: 5px;
                                   border-top-right-radius: 5px;
                                   border-top: 1px solid #4F4F4F;
                                   border-left: 1px solid #4F4F4F;
                                   border-right: 1px solid #4F4F4F;
                                   background: #1A1A1A;
                                   color: #818181;''')
        self.widget_data.preview = self.preview
        all_widget.addWidget(self.preview)
        ##
        self.info_layout = QHBoxLayout()
        #
        self.title = QLabel()
        self.title.setStyleSheet('''margin: 0;
                                 padding: 5px;
                                 color: #818181;
                                 border-left: 1px solid #4F4F4F;
                                 border-right: 1px solid #4F4F4F;
                                 border-top: 1px solid #4F4F4F;
                                 background: #151515;''')
        self.title.setFont(fonts.side)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.widget_data.title = self.title
        self.info_layout.addWidget(self.title)
        #
        self.type = QLabel(self.TYPES[self.widget_data.type])
        self.type.setStyleSheet('''margin: 0;
                                padding: 5px;
                                color: #818181;
                                border-right: 1px solid #4F4F4F;
                                border-top: 1px solid #4F4F4F;
                                background: #151515;''')
        self.type.setFont(fonts.side)
        self.type.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.info_layout.addWidget(self.type)
        #
        all_widget.addLayout(self.info_layout)

        ##
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(0)
        #
        self.button1 = QPushButton()
        self.button1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button1.clicked.connect(self.widget_data.b1_func)
        self.button1.setIcon(self.widget_data.b1_icon)
        self.button1.setIconSize(QSize(20, 20))
        self.button1.setStyleSheet('''QPushButton {
                              margin: 0;
                              padding: 0;
                              border-bottom-left-radius: 5px;
                              border: 1px solid #4F4F4F;
                              background: #151515;}
                              QPushButton:hover:!pressed {
                              background: #4F4F4F; }''')
        buttons_layout.addWidget(self.button1)
        #
        self.button2 = QPushButton()
        self.button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button2.clicked.connect(self.widget_data.b2_func)
        self.button2.setIcon(self.widget_data.b2_icon)
        self.button2.setIconSize(QSize(20, 20))
        self.button2.setStyleSheet('''QPushButton {
                              margin: 0;
                              padding: 0;
                              border-bottom-right-radius: 5px;
                              border-bottom: 1px solid #4F4F4F;
                              border-right: 1px solid #4F4F4F;
                              border-top: 1px solid #4F4F4F;
                              background: #151515;}
                              QPushButton:hover:!pressed {
                              background: #4F4F4F; }''')
        buttons_layout.addWidget(self.button2)
        #
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons_layout)
        buttons_widget.setFixedHeight(40)
        ##
        all_widget.addWidget(buttons_widget)
        ##
        self.setLayout(all_widget)
        self.setFixedWidth(144)
        self.setFixedHeight(200)
    
    def contextMenuEvent(self, event):
        
        if self.widget_data.context_menu:
            self.context_menu = []
            menu = QMenu(self)

            for this_menu in self.widget_data.context_menu:
                self.context_menu.append(QAction(this_menu['title'], self))
                self.context_menu[-1].setFont(fonts.side)
                self.context_menu[-1].triggered.connect(partial(this_menu['func'], self.widget_data.copy().id))
                menu.addAction(self.context_menu[-1])

            menu.setStyleSheet('''QMenu {
                               background: #151515;
                               border: 1px solid #4F4F4F;
                               border-radius: 5px; }
                               QMenu::item {
                               color: #818181;
                               padding: 5px 10px;
                               border-bottom: 1px solid #4F4F4F; }
                               QMenu::item:selected {
                               background: #4F4F4F;
                               color: #151515 }''')
            menu.exec(event.globalPos())