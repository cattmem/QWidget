import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QPushButton,
                             QSizePolicy)
from PyQt6.QtCore import Qt

from ui.main_ui import Ui_MainWindow

from modules.widget_data import Widget

from src.fonts.connect import fonts

import ui.main.home_ui as main_home
import ui.main.widgets_list_ui as main_widgets


MENU = ({ 'title': 'Главная', 'frame': main_home },
        { 'title': 'Виджеты', 'frame': main_widgets })


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.widgets = []

        self.initUI()
    
    def initUI(self) -> None:
        # easy data
        self.main = self.ui.stackedWidget
        self.side_menu = self.ui.leftSideLayout

        self.buttons = []

        self.ui.topLayout.setContentsMargins(189, 0, 0, 0)
        spacer = QLabel()
        spacer.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer.setMaximumHeight(30)
        spacer.setStyleSheet('border-right: 1px solid #4F4F4F;')
        self.side_menu.addWidget(spacer)

        self.forms = []

        for i, page in enumerate(MENU):
            # side menu ---------------
            button = QPushButton(page['title'])
            button.setFont(fonts.side)
            button.setMinimumWidth(190)
            button.setObjectName(str(i))
            button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(self.change_page)
            self.buttons.append(button)
            self.side_menu.addWidget(button)

            # main -------------------
            form = page['frame'].Ui_Form(self)
            self.forms.append(form)
            self.main.addWidget(form)
        
        self.buttons[0].click()

        spacer = QLabel()
        spacer.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer.setStyleSheet('border-right: 1px solid #4F4F4F;')
        self.side_menu.addWidget(spacer)
    
    def change_page(self) -> None:
        i = int(self.buttons.index(self.sender()))
        self.main.setCurrentIndex(i)

        # -------------------------------------------------
        # SO BAD CODE
        # time release
        # -------------------------------------------------

        fixed = '''QPushButton:hover { background: #4F4F4F; color: #151515 }'''
        # clear selecting
        for btn in self.buttons:
            if i < int(self.buttons.index(btn)):
                btn.setStyleSheet('''QPushButton {
                                  margin: 0;
                                  padding: 15px;
                                  border-radius: 0;
                                  border-bottom: 1px solid #4F4F4F;
                                  border-right: 1px solid #4F4F4F;
                                  text-align:left;
                                  background: #151515;
                                  color: #818181; }
                                  ''' + fixed)
            elif i > int(self.buttons.index(btn)):
                btn.setStyleSheet('''QPushButton {
                                  margin: 0;
                                  padding: 15px;
                                  border-radius: 0;
                                  border-top: 1px solid #4F4F4F;
                                  border-right: 1px solid #4F4F4F;
                                  text-align:left;
                                  background: #151515;
                                  color: #818181; }
                                  ''' + fixed)
            else:
                btn.setStyleSheet('''QPushButton {
                                  margin: 0;
                                  padding: 15px;
                                  border-radius: 0;
                                  border-top: 1px solid #3A5CE4;
                                  border-bottom: 1px solid #3A5CE4;
                                  border-right: 1px solid #3A5CE4;
                                  text-align:left;
                                  background: #3A5CE4;
                                  color: #151515; }
                                  ''')
                
    def open_widget(self, widget: Widget) -> None:
        self.widgets.append(widget)
        self.load_widget(widget)
        self.widgets[-1].qwidget.show()

        self.update_forms()
    
    def load_widget(self, widget: Widget) -> None:
        widget.loaded = True
        widget.b1_func = lambda _, w=widget: self.unload_widget(w)
        widget.qwidget.show()

        self.update_forms()
    
    def unload_widget(self, widget: Widget) -> None:
        widget.loaded = False
        widget.b1_func = lambda _, w=widget: self.load_widget(w)
        widget.qwidget.hide()
        
        self.update_forms()
    
    def update_forms(self) -> None:
        self.forms[0].data_load.update(list(filter(lambda w: w.loaded, self.widgets)))
        self.forms[0].data_unload.update(list(filter(lambda w: not w.loaded, self.widgets)))

        print(list(map(lambda w: w.loaded, self.widgets)))

    def mousePressEvent(self, event) -> None:
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('src\styles\style.qss') as qss:
        style = qss.read()
    app.setStyleSheet(style)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())