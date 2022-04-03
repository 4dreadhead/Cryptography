from PyQt5 import QtCore, QtGui, QtWidgets
from lib.methods import scytale, polybius_square, atbash, caesar, richelieu, cardano, alberti
import sys


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(810, 600))
        MainWindow.setMaximumSize(QtCore.QSize(810, 600))
        MainWindow.setBaseSize(QtCore.QSize(810, 600))
        MainWindow.setStyleSheet("background-color: rgb(32, 28, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = self.set_font("Uroob", size=11, bold=True)

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(140, 520, 530, 45))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setStyleSheet(self.exit_style())
        self.pushButton_exit.setObjectName("Exit")

        self.pushButton_Atbash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Atbash.setGeometry(QtCore.QRect(0, 200, 270, 70))
        self.pushButton_Atbash.setFont(font)
        self.pushButton_Atbash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Atbash.setObjectName("Atbash")
        self.pushButton_Atbash.setStyleSheet(self.default_style())

        self.pushButton_Scytale = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Scytale.setGeometry(QtCore.QRect(0, 270, 270, 70))
        self.pushButton_Scytale.setFont(font)
        self.pushButton_Scytale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Scytale.setObjectName("pushButton_Scytale")
        self.pushButton_Scytale.setStyleSheet(self.default_style())

        self.pushButton_PolybiusSquare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PolybiusSquare.setGeometry(QtCore.QRect(0, 340, 270, 70))
        self.pushButton_PolybiusSquare.setFont(font)
        self.pushButton_PolybiusSquare.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_PolybiusSquare.setObjectName("pushButton_PolybiusSquare")
        self.pushButton_PolybiusSquare.setStyleSheet(self.default_style())

        self.pushButton_Caesar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Caesar.setGeometry(QtCore.QRect(0, 410, 270, 70))
        self.pushButton_Caesar.setFont(font)
        self.pushButton_Caesar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Caesar.setStyleSheet(self.default_style())
        self.pushButton_Caesar.setObjectName("pushButton_Caesar")

        self.pushButton_Cardano = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cardano.setGeometry(QtCore.QRect(270, 200, 270, 70))
        self.pushButton_Cardano.setFont(font)
        self.pushButton_Cardano.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Cardano.setStyleSheet(self.default_style())
        self.pushButton_Cardano.setObjectName("pushButton_Cardano")

        self.pushButton_Richelieu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Richelieu.setGeometry(QtCore.QRect(270, 270, 270, 70))
        self.pushButton_Richelieu.setFont(font)
        self.pushButton_Richelieu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Richelieu.setStyleSheet(self.default_style())
        self.pushButton_Richelieu.setObjectName("pushButton_Richelieu")

        # In development buttons area

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 410, 270, 70))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(self.in_development_style())
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_Alberti = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Alberti.setGeometry(QtCore.QRect(270, 340, 270, 70))
        self.pushButton_Alberti.setFont(font)
        self.pushButton_Alberti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Alberti.setStyleSheet(self.default_style())
        self.pushButton_Alberti.setObjectName("pushButton_Alberti")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 200, 270, 70))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(self.in_development_style())
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(540, 270, 270, 70))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(self.in_development_style())
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 340, 270, 70))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(self.in_development_style())
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 410, 270, 70))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(self.in_development_style())
        self.pushButton_12.setObjectName("pushButton_12")
        # End

        self.label_MainMenu_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_MainMenu_gif.setGeometry(QtCore.QRect(-10, 10, 831, 181))
        self.label_MainMenu_gif.setBaseSize(QtCore.QSize(0, 0))
        self.label_MainMenu_gif.setText("")
        self.label_MainMenu_gif.setObjectName("label")
        gif = QtGui.QMovie("lib/media/main_menu.gif")
        self.label_MainMenu_gif.setMovie(gif)
        gif.start()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHY"))
        self.pushButton_Atbash.setText(_translate("MainWindow", "Шифр Атбаш"))
        self.pushButton_Scytale.setText(_translate("MainWindow", "Шифр Сцитала"))
        self.pushButton_PolybiusSquare.setText(_translate("MainWindow", "Шифр Квадрат Полибия"))
        self.pushButton_Caesar.setText(_translate("MainWindow", "Шифр Цезаря"))
        self.pushButton_5.setText(_translate("MainWindow", "Шифр Гронсфельда"))
        self.pushButton_Alberti.setText(_translate("MainWindow", "Шифр Диск Альберти"))
        self.pushButton_7.setText(_translate("MainWindow", "Шифр Вижинера"))
        self.pushButton_Cardano.setText(_translate("MainWindow", "Шифр Кардано"))
        self.pushButton_Richelieu.setText(_translate("MainWindow", "Шифр Ришелье"))
        self.pushButton_10.setText(_translate("MainWindow", "Шифр Плейфера"))
        self.pushButton_11.setText(_translate("MainWindow", "Криптосхема Хилла"))
        self.pushButton_12.setText(_translate("MainWindow", "Шифр Вернама"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход из программы"))

    @staticmethod
    def set_font(family, size=12, weight=75, bold=False, italic=False):
        font = QtGui.QFont()
        if family:
            font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setWeight(weight)
        return font

    @staticmethod
    def in_development_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                       color: rgb(201,44,123); }
                   QPushButton:!hover { background-color: rgb(48, 42, 61);
                                        color: rgb(201,44,123); }
                   QPushButton:pressed { background-color: rgb(24, 21, 30);
                                        color: rgb(201,44,123); }"""
        return style

    @staticmethod
    def default_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                       color: rgb(14,149,226); }
                   QPushButton:!hover { background-color: rgb(48, 42, 61);
                                        color: rgb(14,149,226); }
                   QPushButton:pressed { background-color: rgb(24, 21, 30);
                                         color: rgb(14,149,226); }"""
        return style

    @staticmethod
    def exit_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                       color: rgb(255,65,100); }
                   QPushButton:!hover { background-color: rgb(48, 42, 61);
                                        color: rgb(255,65,100); }
                   QPushButton:pressed { background-color: rgb(24, 21, 30);
                                         color: rgb(255,65,100); }"""
        return style


class MainMenu(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('lib/media/icon.png'))
        self.mySecond = None

        self.pushButton_Atbash.clicked.connect(self.run_atbash)
        self.pushButton_Scytale.clicked.connect(self.run_scytale)
        self.pushButton_PolybiusSquare.clicked.connect(self.run_polybius_square)
        self.pushButton_Caesar.clicked.connect(self.run_caesar)
        self.pushButton_Cardano.clicked.connect(self.run_cardano)
        self.pushButton_Richelieu.clicked.connect(self.run_richelieu)
        self.pushButton_5.clicked.connect(self.in_development)
        self.pushButton_Alberti.clicked.connect(self.run_alberti)
        self.pushButton_7.clicked.connect(self.in_development)
        self.pushButton_10.clicked.connect(self.in_development)
        self.pushButton_11.clicked.connect(self.in_development)
        self.pushButton_12.clicked.connect(self.in_development)
        self.pushButton_exit.clicked.connect(self.close_program)

    def run_atbash(self):
        self.statusbar.showMessage("Запущено: Шифр Атбаш.")
        self.mySecond = atbash.AtbashWindow()
        self.mySecond.show()

    def run_scytale(self):
        self.statusbar.showMessage("Запущено: Шифр Сцитала.")
        self.mySecond = scytale.ScytaleWindow()
        self.mySecond.show()

    def run_polybius_square(self):
        self.statusbar.showMessage("Запущено: Шифр Квадрат Полибия.")
        self.mySecond = polybius_square.PolybiusSquareWindow()
        self.mySecond.show()

    def run_caesar(self):
        self.statusbar.showMessage("Запущено: Шифр Цезаря.")
        self.mySecond = caesar.CaesarWindow()
        self.mySecond.show()

    def run_richelieu(self):
        self.statusbar.showMessage("Запущено: Шифр Ришелье.")
        self.mySecond = richelieu.RichelieuWindow()
        self.mySecond.show()

    def run_cardano(self):
        self.statusbar.showMessage("Запущено: Решетка Кардано.")
        self.mySecond = cardano.CardanoWindow()
        self.mySecond.show()

    def run_alberti(self):
        self.statusbar.showMessage("Запущено: Диск Альберти.")
        self.mySecond = alberti.AlbertiWindow()
        self.mySecond.show()

    def in_development(self):
        self.statusbar.showMessage("Метод в разработке.")

    def close_program(self):
        if self.mySecond:
            self.mySecond.close()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainMenu()
    myapp.show()
    sys.exit(app.exec_())