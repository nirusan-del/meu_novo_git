import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout




class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)
        self.init_ui()


    def init_ui(self):
        # Layout principal
        layout = QVBoxLayout()


        # Campo de exibição
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        layout.addWidget(self.display)


        # Grid para os botões
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4),
        ]


        for btn_text, row, col, *opt in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("font-size: 20px; padding: 20px;")
            rowspan, colspan = opt if opt else (1, 1)
            grid.addWidget(btn, row, col, rowspan, colspan)
            btn.clicked.connect(self.on_button_click)


        layout.addLayout(grid)
        self.setLayout(layout)


    def on_button_click(self):
        sender = self.sender()
        text = sender.text()


        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Erro")
        else:
            self.display.setText(self.display.text() + text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())



