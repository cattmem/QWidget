import os
import shutil

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QMainWindow, QScrollArea, QLabel, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSizePolicy, QSpacerItem, QFileDialog)
from PyQt6.QtGui import QPixmap

from modules.widget_style import ListWidget
from modules.widget_data import Widget
from modules.widget_files_managment import export
from src.fonts.connect import fonts
from src.images.connect import icons

from database.connect import database as db


class Ui_Form(QWidget):
    def __init__(self, main: QMainWindow) -> None:
        super().__init__()

        self.main = main
        
        all_box = QVBoxLayout()
        all_box.setContentsMargins(0, 0, 0, 0)
        all_box.setSpacing(0)

        top_line = QHBoxLayout()
        top_line.setContentsMargins(0, 0, 0, 0)
        top_line.setSpacing(0)
        
        self.search = QLineEdit()
        self.search.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.search.setStyleSheet('''border: 0; background: #151515;
                                  border-bottom: 1px solid #4F4F4F;
                                  padding: 15px;
                                  color: #DBDBDB;''')
        self.search.setFont(fonts.line_edit)
        self.search.setPlaceholderText('Поиск')
        self.search.textChanged.connect(self.search_changed)

        self.reload = QPushButton('⟳')
        self.reload.setFont(fonts.line_edit)
        self.reload.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.reload.setStyleSheet('''QPushButton {
                                  border: 0;
                                  margin: 0;
                                  padding: 0 20px;
                                  border-bottom: 1px solid #4F4F4F;
                                  border-left: 1px solid #4F4F4F;
                                  background: #151515;
                                  color: #818181; }
                                  QPushButton:hover:!pressed {
                                  background: #4F4F4F; }
                                  QPushButton:pressed {
                                  background: #3A5CE4;
                                  border: 1px solid #3A5CE4; }''')
        self.reload.clicked.connect(self.update)
        
        top_line.addWidget(self.search)
        top_line.addWidget(self.reload)

        all_box.addLayout(top_line)

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
                                      border-right: 1px solid #4F4F4F;
                                      background: #151515;
                                      color: #818181; }
                                      QPushButton:!enabled {
                                      background: #1A1A1A;
                                      }
                                      QPushButton:hover:!pressed {
                                      background: #4F4F4F; }
                                      QPushButton:pressed {
                                      background: #3A5CE4;
                                      border: 1px solid #3A5CE4;
                                      } ''')
        self.back_arrow.clicked.connect(self.back_page)

        self.page_view = QLabel()
        self.page_view.setFont(fonts.line_edit)
        self.page_view.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.page_view.setFixedHeight(40)
        self.page_view.setStyleSheet('''border-top: 1px solid #4F4F4F;
                                     padding: 0 10px;''')

        self.next_arrow = QPushButton('>')
        self.next_arrow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.next_arrow.setFixedHeight(40)
        self.next_arrow.setStyleSheet('''QPushButton {
                                      margin: 0;
                                      padding: 0;
                                      border-top: 1px solid #4F4F4F;
                                      border-left: 1px solid #4F4F4F;
                                      background: #151515;
                                      color: #818181; }
                                      QPushButton:!enabled {
                                      background: #1A1A1A;
                                      }
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
        buttons.addWidget(self.page_view)
        buttons.addWidget(self.next_arrow)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setSpacing(0)
        all_box.addLayout(buttons)

        self.setLayout(all_box)   

    def update(self) -> None:
        def change_star(index: int) -> None:
            db.change_star(index)
            self.update()
        
        def remove_widget(index: int) -> None:
            try:
                db.remove_widget(index) 
                os.chmod(f'widgets\\w_{index}', 0o777)
                shutil.rmtree(f'widgets\\w_{index}')

                self.update() 
            except Exception as e:
                print(e)
        
        def export_widget(index: int) -> None:
            file, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Виджет Qwidget (*.qwd)')
            export(index, file)
                

        self.back_arrow.setDisabled(False)
        self.next_arrow.setDisabled(False)
        self.widgets = db.get_widgets(self.page, self.title)
        self.max_page = db.get_max_pages(self.title)

        if self.widgets:
            self.page_view.setText(f'{self.page + 1} / {self.max_page + 1}')
        else:
            self.page_view.setText('Пусто')

        if self.page == 0:
            self.back_arrow.setDisabled(True)
        if self.page == self.max_page:
            self.next_arrow.setDisabled(True)

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
            indx = self.widgets[count][0]

            # widget = Widget(indx, '', '', lambda a: a, '', lambda a: a)
            # set_widgets(get_widgets() + [widget])
            # get_widgets()[-1].b1_func = lambda _, wid=get_widgets()[-1].copy(): add_widget(wid)

            widget = Widget(indx, True, '', any, 0,
                            icons.add, lambda _: _,
                            (icons.full_star if db.get_star(indx) else icons.star), lambda _: _,
                            [{'title': 'Экспорт', 'func': lambda id_: export_widget(id_)},
                             {'title': 'Удалить', 'func': lambda id_: remove_widget(id_)}])
            widget.b1_func = lambda _, indx=indx: self.main.open_widget(widget.copy(indx))
            widget.b2_func = lambda _, indx=indx: change_star(indx)

            grid_widget = ListWidget(widget)
            grid_widget.title.setText(db.get_title_by_id(indx))
            widget.preview.setScaledContents(True)
            widget.preview.setPixmap(QPixmap(f'widgets\\w_{indx}\\preview.png'))
            self.box.addWidget(grid_widget, y, x, Qt.AlignmentFlag.AlignTop)
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
