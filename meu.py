import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculadora_gui import Ui_MainWindow  # interface gerada

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar os botões às funções
        self.ui.btn_somar.clicked.connect(self.somar)
        self.ui.btn_subtrair.clicked.connect(self.subtrair)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir)

    def pegar_valores(self):
        try:
            a = float(self.ui.txt_num1.text())
            b = float(self.ui.txt_num2.text())
            return a, b
        except ValueError:
            self.ui.lbl_resultado.setText("Digite números válidos")
            return None, None

    def somar(self):
        a, b = self.pegar_valores()
        if a is not None:
            self.ui.lbl_resultado.setText(f"Resultado: {a + b}")

    def subtrair(self):
        a, b = self.pegar_valores()
        if a is not None:
            self.ui.lbl_resultado.setText(f"Resultado: {a - b}")

    def multiplicar(self):
        a, b = self.pegar_valores()
        if a is not None:
            self.ui.lbl_resultado.setText(f"Resultado: {a * b}")

    def dividir(self):
        a, b = self.pegar_valores()
        if a is not None:
            if b == 0:
                self.ui.lbl_resultado.setText("Erro: divisão por zero")
            else:
                self.ui.lbl_resultado.setText(f"Resultado: {a / b}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec_())
