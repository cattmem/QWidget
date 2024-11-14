from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel,
                             QSizePolicy)

from modules.widget_data import Widget


class ListWidget(QWidget):
    def __init__(self, widget_data: Widget) -> None:
        super().__init__()
        super().__init__()

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
        button1.setCursor(Qt.CursorShape.PointingHandCursor)
        button1.clicked.connect(widget_data.b1_func)
        button1.setStyleSheet('''QPushButton {
                              margin: 0;
                              padding: 0;
                              border-bottom-left-radius: 5px;
                              border: 1px solid #4F4F4F;
                              background: #151515;
                              color: #818181; }
                              QPushButton:hover:!pressed {
                              background: #4F4F4F; }''')
        buttons_layout.addWidget(button1)
        #
        button2 = QPushButton()
        button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button2.setCursor(Qt.CursorShape.PointingHandCursor)
        button2.clicked.connect(widget_data.b2_func)
        button2.setStyleSheet('''QPushButton {
                              margin: 0;
                              padding: 0;
                              border-bottom-right-radius: 5px;
                              border-bottom: 1px solid #4F4F4F;
                              border-right: 1px solid #4F4F4F;
                              border-top: 1px solid #4F4F4F;
                              background: #151515;
                              color: #818181; }
                              QPushButton:hover:!pressed {
                              background: #4F4F4F; }''')
        buttons_layout.addWidget(button2)
        #
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons_layout)
        buttons_widget.setFixedHeight(40)
        ##
        all_widget.addWidget(buttons_widget)
        ##
        self.setLayout(all_widget)
        self.setMaximumWidth(144)
        self.setMaximumHeight(200)