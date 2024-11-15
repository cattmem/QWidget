from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSizePolicy, QSpacerItem)

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from src.fonts.connect import fonts

from database.connect import database as db

class Ui_Form(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        all_box = QVBoxLayout()
        all_box.setContentsMargins(0, 0, 0, 0)
        all_box.setSpacing(0)
        
        self.search = QLineEdit()
        self.search.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.search.setStyleSheet('''border: 0; background: #151515;
                                  border-bottom: 1px solid #4F4F4F;
                                  padding: 15px;
                                  color: #DBDBDB;''')
        self.search.setFont(fonts.line_edit)
        self.search.setPlaceholderText('Поиск')
        self.search.textChanged.connect(self.search_changed)

        all_box.addWidget(self.search)

        self.box = QGridLayout()
        self.box.setContentsMargins(15, 0, 15, 0)
        self.box.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.box.setSpacing(11)

        buttons = QHBoxLayout()
        self.back_arrow = QPushButton('<')
        self.back_arrow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.back_arrow.setFixedHeight(40)
        self.back_arrow.setStyleSheet('''QPushButton {
                                      margin: 0;
                                      padding: 0;
                                      border-top: 1px solid #4F4F4F;
                                      background: #151515;
                                      color: #818181; }
                                      QPushButton:!enabled {
                                      opacity: .5;
                                      }
                                      QPushButton:hover:!pressed {
                                      background: #4F4F4F; }
                                      QPushButton:pressed {
                                      background: #3A5CE4;
                                      border: 1px solid #3A5CE4;
                                      } ''')
        self.back_arrow.clicked.connect(self.back_page)
        self.next_arrow = QPushButton('>')
        self.next_arrow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.next_arrow.setFixedHeight(40)
        self.next_arrow.setStyleSheet('''QPushButton {
                                      margin: 0;
                                      padding: 0;
                                      border-top: 1px solid #4F4F4F;
                                      background: #151515;
                                      color: #818181; }
                                      QPushButton:hover:!pressed {
                                      background: #4F4F4F; }
                                      QPushButton:pressed {
                                      background: #3A5CE4;
                                      border: 1px solid #3A5CE4;
                                      } ''')
        self.next_arrow.clicked.connect(self.next_page)

        scroll_box_widget = QWidget()
        scroll_box_widget.setLayout(self.box)

        self.scroll_box = QScrollArea()
        self.scroll_box.setWidgetResizable(True)
        self.scroll_box.setStyleSheet('''QScrollBar {
                                      background: #151515;
                                      width: 15px;
                                      border-left: 1px solid #4F4F4F;
                                      }
                                      QScrollBar::handle {
                                      background: #4F4F4F;
                                      }
                                      QScrollBar::sub-line, QScrollBar::add-line {
                                      background: none;
                                      }
                                      QScrollBar::add-page, QScrollBar::sub-page {
                                      background: none;
                                      }
                                      QScrollBar::up-arrow, QScrollBar::down-arrow {
                                      background: none;
                                      }''')
        self.scroll_box.setWidget(scroll_box_widget)

        self.page = 0
        self.title = ''
        self.update()

        all_box.addWidget(self.scroll_box)

        buttons.addWidget(self.back_arrow)
        buttons.addWidget(self.next_arrow)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setSpacing(0)
        all_box.addLayout(buttons)

        self.setLayout(all_box)

    def update(self) -> None:
        self.back_arrow.setHidden(False)
        self.next_arrow.setHidden(False)
        self.widgets = db.get_widgets(self.page, self.title)
        self.max_page = db.get_max_pages(self.title)

        if self.page == 0:
            self.back_arrow.setHidden(True)
        if self.page == self.max_page:
            self.next_arrow.setHidden(True)

        while self.box.count():
            w = self.box.itemAt(0).widget()
            self.box.removeWidget(w)
            del w

        spacer = QLabel()
        spacer.setFixedSize(1, 0)
        self.box.addWidget(spacer, 0, 0)

        count = 0
        x, y = 0, 1

        while count < len(self.widgets):
            widget = ListWidget(Widget('', '', lambda a: a, '', lambda a: a))
            self.box.addWidget(widget, y, x, Qt.AlignmentFlag.AlignTop)
            if x == 2:
                y += 1
                x = 0
            else:
                x += 1
            count += 1
        
        spacer = QLabel()
        spacer.setFixedSize(1, 0)
        self.box.addWidget(spacer, self.box.rowCount(), 0)
        
        sb = self.scroll_box.verticalScrollBar()
        sb.setValue(sb.minimum())

    def search_changed(self) -> None:
        self.page = 0
        self.title = self.search.text()
        self.update()
    
    def next_page(self) -> None:
        self.page += 1
        self.update()
    
    def back_page(self) -> None:
        self.page -= 1
        self.update()
