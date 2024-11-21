import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QPushButton,
                             QSizePolicy, QFileDialog)
from PyQt6.QtCore import Qt, QSize

from ui.main_ui import Ui_MainWindow

from modules.widget_data import Widget
from modules.widget_files_managment import import_

from src.fonts.connect import fonts
from src.images.connect import icons
from src.styles import style

import ui.main.home_ui as main_home
import ui.main.widgets_list_ui as main_widgets


class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()

        self.TOP_MENU = [{ 'title': 'Главная', 'frame': main_home }, 
        { 'title': 'Виджеты', 'frame': main_widgets }]
        self.BOTTOM_MENU = [{ 'title': 'Импорт', 'func': self.select_file }]

        self.all_menu = [self.TOP_MENU, self.BOTTOM_MENU]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.widgets = []

        self.initUI()
    
    def initUI(self) -> None:
        # easy data
        self.main = self.ui.stackedWidget
        self.side_menu = self.ui.leftSideLayout

        self.buttons_page = []
        self.buttons_func = []

        self.ui.topLayout.setContentsMargins(189, 0, 0, 0)
        spacer = QLabel()
        spacer.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer.setMaximumHeight(30)
        spacer.setStyleSheet('border-right: 1px solid #4F4F4F;')
        self.side_menu.addWidget(spacer)

        self.forms = []

        for i, menu in enumerate(self.all_menu):
            for page in menu:
                # side menu ---------------
                button = QPushButton(page['title'])
                button.setFont(fonts.side)
                button.setMinimumWidth(190)
                button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
                button.setCursor(Qt.CursorShape.PointingHandCursor)
                self.side_menu.addWidget(button)

                # main -------------------
                if 'frame' in page.keys():
                    button.clicked.connect(self.change_page)
                    form = page['frame'].Ui_Form(self)
                    self.buttons_page.append(button)
                    self.forms.append(form)
                    self.main.addWidget(form)
                else:
                    button.clicked.connect(page['func'])
                    button.setStyleSheet('''
                    ''')
                    self.buttons_func.append(button)

            if i + 1 != len(self.all_menu):
                spacer = QLabel()
                spacer.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
                spacer.setStyleSheet('border-right: 1px solid #4F4F4F;')
                self.side_menu.addWidget(spacer)
        
        self.buttons_page[0].click()
        for i in range(len(self.buttons_func)):
            self.style_btn(self.buttons_func, i, False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_preview)
        self.timer.start(3000)

        self.ui.close.setText('✕')
        self.ui.close.clicked.connect(self.close)
        self.ui.hide.clicked.connect(self.showMinimized)
        self.ui.hide.setText('–')
    
    def change_page(self) -> None:
        i = int(self.buttons_page.index(self.sender()))
        self.main.setCurrentIndex(i)

        self.style_btn(self.buttons_page, i)
    
    def style_btn(self, list_: list, i: int, is_active: bool = True) -> None:
        if not is_active:
            i = i + 1
        fixed = '''QPushButton:hover { background: #4F4F4F; color: #151515 }'''

        for btn in list_:
            if i < int(list_.index(btn)):
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
            elif i > int(list_.index(btn)):
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
        widget.qwidget.show()
        widget.qwidget.destroyed.connect(lambda _, w=widget: self.remove_widget(w, True))
        widget.qwidget.button_unload.clicked.connect(lambda _, w=widget: self.unload_widget(w))
        widget.qwidget.button_on_top.clicked.connect(lambda _, w=widget: self.pin_widget(w))
        widget.qwidget.button_delete.clicked.connect(lambda _, w=widget: self.remove_widget(w))
        widget.context_menu.clear()

        widget.b2_func = lambda _, w=widget: self.remove_widget(w)
        widget.b2_icon = icons.delete

        self.update_forms()
    
    def pin_widget(self, widget: Widget) -> None:
        if widget.qwidget.windowFlags() & Qt.WindowType.WindowStaysOnTopHint:
            widget.qwidget.setWindowFlags(widget.qwidget.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
        else:
            widget.qwidget.setWindowFlags(widget.qwidget.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        widget.qwidget.show()

    def load_widget(self, widget: Widget) -> None:
        widget.loaded = True
        widget.b1_func = lambda _, w=widget: self.unload_widget(w)
        widget.b1_icon = icons.unload
        widget.qwidget.show()
        self.update_forms()
    
    def remove_widget(self, widget: Widget, by_user: bool = False) -> None:
        try:
            if not by_user:
                widget.qwidget.destroy()
            self.widgets.remove(widget)
        except Exception:
            pass

        self.update_forms()
    
    def unload_widget(self, widget: Widget) -> None:
        widget.loaded = False
        widget.b1_func = lambda _, w=widget: self.load_widget(w)
        widget.b1_icon = icons.load
        widget.qwidget.hide()
        
        self.update_forms()
    
    def update_forms(self) -> None:
        self.forms[0].data_load.update(list(filter(lambda w: w.loaded, self.widgets)))
        self.forms[0].data_unload.update(list(filter(lambda w: not w.loaded, self.widgets)))

        self.update_preview()
    
    def select_file(self, _) -> None:
        file, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'Виджет Qwidget (*.qwd)')
        if file:
            import_(file)
    
    def update_preview(self) -> None:
        for w in self.widgets:
            w.preview.setPixmap(
                w.qwidget.grab(w.qwidget.rect()).scaled(w.preview.size(), Qt.AspectRatioMode.KeepAspectRatio)
            )
            w.title.setText(w.qwidget.title.text())

    def mousePressEvent(self, event) -> None:
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet(style.style)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())