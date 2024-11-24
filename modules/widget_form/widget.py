import sys

from PyQt6.QtGui import QEnterEvent
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QPushButton,
                             QLabel, QSizePolicy)
from PyQt6.QtCore import Qt, QSize

from src.fonts.connect import fonts
from src.images.connect import icons

from database.connect import database as db


class WidgetWindow(QWidget):
    def __init__(self, id_widget: int) -> None:
        super().__init__()

        self.id_widget = id_widget

        sys.path.append('widgets/')
        exec(f'from w_{id_widget} import main, config', globals())

        self.type = config.type

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        if self.type == 1:
            self.start_work = self.work_widget
        elif self.type == 2:
            self.start_work = self.work_screen
    
    def work_widget(self) -> None:
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.title = QLineEdit(db.get_title_by_id(self.id_widget))
        self.title.setStyleSheet('''QLineEdit {
                                 border: 0;
                                 background: rgba(0, 0, 0, 0);
                                 padding-right: 20px;
                                 color: rgba(128, 128, 128, 60); }
                                 QLineEdit:focus {
                                 border: 1px solid rgba(128, 128, 128, 40);
                                 border-radius: 2px;
                                 background: rgba(0, 0, 0, 0.01); }''')
        self.title.setFont(fonts.widget_title)

        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('''background: rgba(128, 128, 128, 10);
                                       border-radius: 10px;''')

        self.data = main.Main()
        self.main_widget.setFixedSize(self.data.size())

        custom_layout = QVBoxLayout()
        custom_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        custom_widget = self.data
        custom_widget.setStyleSheet('''border: 1px solid rgba(128, 128, 128, 50);
                                    border-radius: 5px;
                                    background: none;''')

        custom_layout.addWidget(custom_widget)
        custom_layout.setContentsMargins(0, 0, 0, 0)
        self.main_widget.setLayout(custom_layout)
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.main_widget)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setContentsMargins(25, 0, 5, 5)
        self.buttons_layout.setSpacing(0)

        self.button_unload = QPushButton()
        self.button_unload.setFixedSize(45, 45)
        self.button_unload.setIcon(icons.unload)
        self.button_unload.setIconSize(QSize(20, 20))
        self.button_unload.setStyleSheet('''QPushButton {
                                         border: 0;
                                         border-radius: 0;
                                         background: rgba(128, 128, 128, 10);
                                         border: 1px solid rgba(128, 128, 128, 50);
                                         border-bottom-left-radius: 5px; }
                                         QPushButton:hover:!pressed {
                                         background: rgba(128, 128, 128, 50);
                                         border: 0; }''')
        self.buttons_layout.addWidget(self.button_unload)
        self.buttons_layout.setParent(None)

        self.button_on_top = QPushButton()
        self.button_on_top.setFixedSize(45, 45)
        self.button_on_top.setIcon(icons.pin)
        self.button_on_top.setIconSize(QSize(20, 20))
        self.button_on_top.setStyleSheet('''QPushButton {
                                         border: 0;
                                         border-radius: 0;
                                         background: rgba(128, 128, 128, 10);
                                         border-top: 1px solid rgba(128, 128, 128, 50);
                                         border-bottom: 1px solid rgba(128, 128, 128, 50);
                                         border-right: 1px solid rgba(128, 128, 128, 50); }
                                         QPushButton:hover:!pressed {
                                         background: rgba(128, 128, 128, 50);
                                         border: 0; }''')
        self.buttons_layout.addWidget(self.button_on_top)

        self.button_delete = QPushButton()
        self.button_delete.setFixedSize(45, 45)
        self.button_delete.setIcon(icons.delete)
        self.button_delete.setIconSize(QSize(20, 20))
        self.button_delete.setStyleSheet('''QPushButton {
                                         border: 0;
                                         border-radius: 0;
                                         background: rgba(128, 128, 128, 10);
                                         border-top: 1px solid rgba(128, 128, 128, 50);
                                         border-bottom: 1px solid rgba(128, 128, 128, 50);
                                         border-right: 1px solid rgba(128, 128, 128, 50);
                                         border-bottom-right-radius: 5px; }
                                         QPushButton:hover:!pressed {
                                         background: rgba(128, 128, 128, 50);
                                         border: 0; }''')
        self.buttons_layout.addWidget(self.button_delete)
        self.buttons_managment(False)

        self.main_layout.addLayout(self.buttons_layout)

        spacer = QLabel()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)
        self.main_layout.addWidget(spacer)

        self.setLayout(self.main_layout)
    
    def work_screen(self) -> None:
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.data = main.Main()
        custom_widget = self.data
        screen = QApplication.primaryScreen().size()

        self.setFixedSize(screen)

        self.main_layout.addWidget(custom_widget)
        self.setLayout(self.main_layout)

    def buttons_managment(self, flag: bool) -> None:
        for i in range(self.buttons_layout.count()):
            widget = self.buttons_layout.itemAt(i).widget()
            if flag:
                widget.show()
            else:
                widget.hide()

    def leaveEvent(self, event: QEnterEvent | None) -> None:
        if self.type == 1:
            self.buttons_managment(False)
            super().leaveEvent(event)

    def enterEvent(self, event: QEnterEvent | None) -> None:
        if self.type == 1:
            self.buttons_managment(True)
            super().enterEvent(event)

    def mousePressEvent(self, event) -> None:
        if self.type == 1:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        if self.type == 1:
            self.move(
                self.pos() +
                event.globalPosition().toPoint() -
                self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
            event.accept()
