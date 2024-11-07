import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QListWidgetItem, QLabel,
                             QGridLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from ui.main_ui import Ui_MainWindow


MENU = ('Главная', 'Виджеты', 'Редактор')


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.initUI()
    
    def initUI(self) -> None:
        # easy data
        self.side_menu = self.ui.listMenu
        self.main = self.ui.stackedWidget

        # visual
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # clear widgets
        self.side_menu.clear()
        widgets = self.main.findChildren(QWidget)
        for widget in widgets:
            self.main.removeWidget(widget)
    
        for title in MENU:
            # side menu ---------------
            item = QListWidgetItem()
            font = QFont('src\fonts\Inter.ttf')
            item.setText(title)
            item.setFont(font)
            self.side_menu.addItem(item)

            # main --------------------
            grid_layout = QGridLayout()
            label = QLabel(title)
            grid_layout.addWidget(label)

            widget = QWidget()
            widget.setLayout(grid_layout)

            self.main.addWidget(widget)

        # connect side menu and main
        self.side_menu.currentRowChanged['int'].connect(self.main.setCurrentIndex)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('src\styles\style.qss') as qss:
        style = qss.read()
    app.setStyleSheet(style)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
