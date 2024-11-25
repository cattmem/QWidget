from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QListWidget, QFileDialog)

import cv2
import pyzbar


class Main(QWidget):
    ''' QR сканер '''

    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(400, 350)

        self.layout = QVBoxLayout()

        self.load_btn = QPushButton('Загрузить изображение')
        self.load_btn.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed)
        self.load_btn.clicked.connect(self.load_image)
        self.load_btn.setFixedHeight(25)
        self.layout.addWidget(self.load_btn)

        self.qr_codes = QListWidget()
        self.qr_codes.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        self.qr_codes.itemClicked.connect(self.copy)
        self.layout.addWidget(self.qr_codes)

        self.setLayout(self.layout)

    def load_image(self) -> None:
        file, _ = QFileDialog.getOpenFileName(
            self, 'Открыть изображение', '', 'Изображения (*.png *.jpg *.jpeg)')
        if file:
            self.scan_image(file)

    def scan_image(self, file: str) -> None:
        image = cv2.imread(file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        qr_codes = pyzbar.pyzbar.decode(image)
        self.qr_codes.clear()

        for idx, qr_code in enumerate(qr_codes):
            points = qr_code.polygon
            if len(points) == 4:
                qr_data = qr_code.data.decode('utf-8')
                identifier = f'QR-{idx+1}'

                self.qr_codes.addItem(f'{identifier} {qr_data}')

    def copy(self, item):
        # Copy the text of the selected item to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(' '.join(item.text().split(' ')[1:]))
