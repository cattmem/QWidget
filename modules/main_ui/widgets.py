from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QSizePolicy, QSpacerItem)
from PyQt6.QtGui import QFont


class Ui_Form(QWidget):
    def __init__(self, title: str, data: list,
                 button1_image, button1_func,
                 button2_image, button2_func) -> None:
        super().__init__()
    
        box = QVBoxLayout()
        box.setContentsMargins(19, 15, 0, 15)
        box.setSpacing(11)

        # fonts
        font_title = QFont('..\..\src\fonts\Inter.ttf')
        font_title.setPixelSize(20)
        font_title.setWeight(600)
        font_title.setKerning(True)

        title_label = QLabel(title)
        title_label.setFont(font_title)
        title_label.setStyleSheet('color: #DBDBDB')
        box.addWidget(title_label)
        
        # ------------------
        widget_list_layout = QHBoxLayout()
        widget_list_layout.setSpacing(11)
        widget_list_layout.setContentsMargins(0, 0, 0, 0)

        for widget in data:
            all_widget = QVBoxLayout()
            all_widget.setContentsMargins(0, 0, 0, 0)
            all_widget.setSpacing(0)
            ##
            preview = QLabel()
            preview.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            preview.setContentsMargins(0, 0, 0, 0)
            preview.setFixedHeight(160)
            preview.setFixedWidth(144)
            preview.setStyleSheet('''margin: 0;
                                  padding: 0;
                                  border-top-left-radius: 5px;
                                  border-top-right-radius: 5px;
                                  border-top: 1px solid #4F4F4F;
                                  border-left: 1px solid #4F4F4F;
                                  border-right: 1px solid #4F4F4F;
                                  background: #1A1A1A;
                                  color: #818181;''')
            all_widget.addWidget(preview)
            ##
            buttons_layout = QHBoxLayout()
            buttons_layout.setContentsMargins(0, 0, 0, 0)
            buttons_layout.setSpacing(0)
            #
            button1 = QPushButton()
            button1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button1.clicked.connect(button1_func)
            button1.setStyleSheet('''margin: 0;
                                  padding: 0;
                                  border-bottom-left-radius: 5px;
                                  border: 1px solid #4F4F4F;
                                  background: #151515;
                                  color: #818181;''')
            buttons_layout.addWidget(button1)
            #
            button2 = QPushButton()
            button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button2.clicked.connect(button2_func)
            button2.setStyleSheet('''margin: 0;
                                  padding: 0;
                                  border-bottom-right-radius: 5px;
                                  border-bottom: 1px solid #4F4F4F;
                                  border-right: 1px solid #4F4F4F;
                                  border-top: 1px solid #4F4F4F;
                                  background: #151515;
                                  color: #818181;''')
            buttons_layout.addWidget(button2)
            #
            buttons_widget = QWidget()
            buttons_widget.setLayout(buttons_layout)
            buttons_widget.setFixedHeight(40)
            ##
            all_widget.addWidget(buttons_widget)
            ##
            widget_list_layout.addLayout(all_widget)

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