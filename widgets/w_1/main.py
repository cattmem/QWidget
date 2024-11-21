from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit, QSizePolicy


class Main(QWidget):
    ''' Note '''
    
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(300, 250)

        self.layout_note = QVBoxLayout()
        self.label_note = QPlainTextEdit()
        self.label_note.setStyleSheet('''margin: 5px; 
                                      padding: 5px;
                                      background: rgba(255, 255, 255, 0.1)''')
        self.label_note.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_note.addWidget(self.label_note)

        self.setLayout(self.layout_note)