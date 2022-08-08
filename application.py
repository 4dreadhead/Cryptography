import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from lib.ui import UiMainMenu
from lib.methods import *


class MainMenuWindow(QMainWindow, UiMainMenu):
    """
    Class of the main menu of the application
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('lib/media/icon.png'))
        self.mySecond = None

        self.pushButton_Atbash.clicked.connect(self.run_atbash)
        self.pushButton_Scytale.clicked.connect(self.run_scytale)
        self.pushButton_PolybiusSquare.clicked.connect(self.run_polybius_square)
        self.pushButton_Caesar.clicked.connect(self.run_caesar)
        self.pushButton_Cardano.clicked.connect(self.run_cardano)
        self.pushButton_Richelieu.clicked.connect(self.run_richelieu)
        self.pushButton_Gronsfeld.clicked.connect(self.run_gronsfeld)
        self.pushButton_Alberti.clicked.connect(self.run_alberti)
        self.pushButton_Vigenere.clicked.connect(self.run_vigenere)
        self.pushButton_Playfair.clicked.connect(self.run_playfair)
        self.pushButton_11.clicked.connect(self.in_development)
        self.pushButton_12.clicked.connect(self.in_development)
        self.pushButton_exit.clicked.connect(self.close_program)

        self.pushButton_DES.clicked.connect(self.run_des)

    def run_atbash(self):
        self.statusbar.showMessage("Запущено: Шифр Атбаш.")
        self.mySecond = AtbashWindow()
        self.mySecond.show()

    def run_scytale(self):
        self.statusbar.showMessage("Запущено: Шифр Сцитала.")
        self.mySecond = ScytaleWindow()
        self.mySecond.show()

    def run_polybius_square(self):
        self.statusbar.showMessage("Запущено: Шифр Квадрат Полибия.")
        self.mySecond = PolybiusSquareWindow()
        self.mySecond.show()

    def run_caesar(self):
        self.statusbar.showMessage("Запущено: Шифр Цезаря.")
        self.mySecond = CaesarWindow()
        self.mySecond.show()

    def run_richelieu(self):
        self.statusbar.showMessage("Запущено: Шифр Ришелье.")
        self.mySecond = RichelieuWindow()
        self.mySecond.show()

    def run_cardano(self):
        self.statusbar.showMessage("Запущено: Решетка Кардано.")
        self.mySecond = CardanoWindow()
        self.mySecond.show()

    def run_alberti(self):
        self.statusbar.showMessage("Запущено: Диск Альберти.")
        self.mySecond = AlbertiWindow()
        self.mySecond.show()

    def run_gronsfeld(self):
        self.statusbar.showMessage("Запущено: Шифр Гросфельда.")
        self.mySecond = GronsfeldWindow()
        self.mySecond.show()

    def run_vigenere(self):
        self.statusbar.showMessage("Запущено: Шифр Виженера.")
        self.mySecond = VigenereWindow()
        self.mySecond.show()

    def run_playfair(self):
        self.statusbar.showMessage("Запущено: Шифр Плейфера.")
        self.mySecond = PlayfairWindow()
        self.mySecond.show()

    def run_des(self):
        self.statusbar.showMessage("Запущено: Шифр DES.")
        self.mySecond = DesWindow()
        self.mySecond.show()

    def in_development(self):
        self.statusbar.showMessage("Метод в разработке.")

    def close_program(self):
        if self.mySecond:
            self.mySecond.close()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainMenuWindow()
    myapp.show()
    sys.exit(app.exec_())
