import sys

from PyQt6.QtWidgets import (QMainWindow, QWidget, QLineEdit,
                             QVBoxLayout, QHBoxLayout,
                             QLabel, QSizePolicy)
from PyQt6.QtCore import Qt

from src.fonts.connect import fonts
from database.connect import database as db


class WidgetWindow(QWidget):
    def __init__(self, id_widget: int) -> None:
        super().__init__()
        exec(f'from widgets.w_{id_widget} import main', globals())

        self.setFixedSize(400, 350)
        
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(5, 5, 5, 5)

        self.title = QLineEdit(db.get_title_by_id(id_widget))
        self.title.setStyleSheet('''QLineEdit {
                                 background: rgba(0, 0, 0, 0);
                                 border: 0;
                                 padding-right: 20px;
                                 color: rgba(128, 128, 128, 60); }
                                 QLineEdit:focus {
                                 border: 1px solid rgba(128, 128, 128, 40);
                                 border-radius: 2px;
                                 }''')
        self.title.setFont(fonts.widget_title)

        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('''background: rgba(128, 128, 128, 10);
                                       border-radius: 10px; ''')
        
        self.data = main.Main()
        custom_layout = QVBoxLayout()
        custom_widget = self.data
        custom_widget.setStyleSheet('''border: 1px solid rgba(128, 128, 128, 50);
                                    border-radius: 5px;
                                    background: none;''')

        self.initUI()

        custom_layout.addWidget(custom_widget)
        custom_layout.setContentsMargins(0, 0, 0, 0)
        self.main_widget.setLayout(custom_layout)
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)
    
    def initUI(self) -> None:
        pass

    def mousePressEvent(self, event) -> None:
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()