import sys
from functools import partial

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QPushButton, QMenu,
                             QSizePolicy, QFileDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

from ui.main_ui import Ui_MainWindow
from ui.main import home_ui as main_home
from ui.main import widgets_list_ui as main_widgets

from modules.widget_data import Widget
from modules.widget_files_managment import import_, import_from_folder
from modules import loger as lg

from src.fonts.connect import fonts
from src.images.connect import icons
from src.styles import style

from database.connect import database as db


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.TOP_MENU = ({'title': 'Главная', 'frame': main_home},
                         {'title': 'Виджеты', 'frame': main_widgets})
        self.BOTTOM_MENU = ({'title': 'Импорт', 'func': self.select_file,
                             'menu': {'title': 'Импорт как папка', 'func': self.select_folder}},)

        self.all_menu = [self.TOP_MENU, self.BOTTOM_MENU]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.widgets = []

        self.initUI()

    def initUI(self) -> None:
        lg.info('init ui')

        self.main = self.ui.stackedWidget
        self.side_menu = self.ui.leftSideLayout

        self.buttons_page = []
        self.buttons_func = []

        self.ui.topLayout.setContentsMargins(189, 0, 0, 0)
        spacer = QLabel()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)
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
                
                if 'menu' in page.keys():
                    self.menu_data = page['menu']
                    
                    button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                    button.customContextMenuRequested.connect(lambda e, me=button: self.context_menu(e, me))


            if i + 1 != len(self.all_menu):
                spacer = QLabel()
                spacer.setSizePolicy(
                    QSizePolicy.Policy.Minimum,
                    QSizePolicy.Policy.Expanding)
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
        lg.info(f'page changed ({i})')
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

    def context_menu(self, event, me: QPushButton):
        context_menu = []
        menu = QMenu(self)

        context_menu.append(QAction(self.menu_data['title'], self))
        context_menu[-1].setFont(fonts.side)
        context_menu[-1].triggered.connect(self.menu_data['func'])
        menu.addAction(context_menu[-1])

        menu.exec(me.mapToGlobal(event))

    def open_widget(self, widget: Widget) -> None:
        lg.info(f'new widget (loaded, {widget.id}, {widget.title.text()}, {widget.type})')
        widget.work()
        widget.qwidget.start_work()
        widget.type = widget.qwidget.type
        self.widgets.append(widget)
        self.load_widget(widget)
        widget.qwidget.show()
        widget.qwidget.destroyed.connect(
            lambda _, w=widget: self.remove_widget(w, True))
        if widget.type == 1:
            widget.qwidget.button_unload.clicked.connect(
                lambda _, w=widget: self.unload_widget(w))
            widget.qwidget.button_on_top.clicked.connect(
                lambda _, w=widget: self.pin_widget(w))
            widget.qwidget.button_delete.clicked.connect(
                lambda _, w=widget: self.remove_widget(w))
        widget.context_menu.clear()

        widget.b2_func = lambda _, w=widget: self.remove_widget(w)
        widget.b2_icon = icons.delete

        self.update_forms()

    def pin_widget(self, widget: Widget) -> None:
        lg.info(
            f'widget pin (loaded, {widget.id}, {widget.title.text()}, {widget.type})')
        if widget.qwidget.windowFlags() & Qt.WindowType.WindowStaysOnTopHint:
            widget.qwidget.setWindowFlags(
                widget.qwidget.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
        else:
            widget.qwidget.setWindowFlags(
                widget.qwidget.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        widget.qwidget.show()

    def load_widget(self, widget: Widget) -> None:
        lg.info(
            f'widget loaded ({widget.id}, {widget.title.text()}, {widget.type})')
        widget.loaded = True
        widget.b1_func = lambda _, w=widget: self.unload_widget(w)
        widget.b1_icon = icons.unload
        widget.qwidget.show()
        self.update_forms()

    def remove_widget(self, widget: Widget, by_user: bool = False) -> None:
        try:
            lg.info(
                f'widget removed ({widget.id}, {widget.title.text()}, {widget.type})')
            if not by_user:
                widget.qwidget.destroy()
            self.widgets.remove(widget)
            widget.qwidget = None
        except Exception as err:
            lg.warn(f'{type(err)}')

        self.update_forms()

    def unload_widget(self, widget: Widget) -> None:
        lg.info(f'widget unloaded ({widget.id}, {widget.title.text()}, {widget.type})')
        widget.loaded = False
        widget.b1_func = lambda _, w=widget: self.load_widget(w)
        widget.b1_icon = icons.load
        widget.qwidget.hide()

        self.update_forms()

    def update_forms(self) -> None:
        lg.info(f'updated lists (loaded/unloaded widgets)')
        self.forms[0].data_load.update(
            list(filter(lambda w: w.loaded, self.widgets)))
        self.forms[0].data_unload.update(
            list(filter(lambda w: not w.loaded, self.widgets)))

        self.update_preview()

    def select_file(self, _) -> None:
        file, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', 'Виджет Qwidget (*.qwd)')
        if file:
            lg.info(f'try import widget ({file})')
            import_(file)
        
    def select_folder(self, _) -> None:
        folder = QFileDialog.getExistingDirectory(
            self, 'Открыть папку', '', QFileDialog.Option.ShowDirsOnly)
        if folder:
            lg.info(f'try import widget ({folder})')
            import_from_folder(folder)

    def update_preview(self) -> None:
        lg.info(f'updated preview (loaded/unloaded widgets)')

        for w in self.widgets:
            if w.type == 1:
                w.preview.setPixmap(
                    w.qwidget.main_widget.grab(w.qwidget.main_widget.rect())
                    .scaled(w.preview.size(), Qt.AspectRatioMode.KeepAspectRatio)
                )
                w.title.setText(w.qwidget.title.text())
            else:
                w.title.setText(db.get_title_by_id(w.id))

    def closeEvent(self, _) -> None:
        lg.to_file()

    def mousePressEvent(self, event) -> None:
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        try:
            self.move(
                self.pos() +
                event.globalPosition().toPoint() -
                self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
            event.accept()
        except Exception as _:
            pass


if __name__ == '__main__':
    lg.info(f'work started')

    app = QApplication(sys.argv)
    app.setStyleSheet(style.style)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
