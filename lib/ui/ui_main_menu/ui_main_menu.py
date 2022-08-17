from PyQt6 import QtCore, QtGui, QtWidgets
from lib.helpers import UiHelper


class UiMainMenu(object):
    """
    UI class of Main Menu
    Describe all widgets
    """
    pushButton_Alberti: QtWidgets.QPushButton
    pushButton_Richelieu: QtWidgets.QPushButton
    pushButton_Cardano: QtWidgets.QPushButton
    pushButton_Caesar: QtWidgets.QPushButton
    pushButton_PolybiusSquare: QtWidgets.QPushButton
    pushButton_Scytale: QtWidgets.QPushButton
    pushButton_Atbash: QtWidgets.QPushButton
    pushButton_Gronsfeld: QtWidgets.QPushButton
    pushButton_Vigenere: QtWidgets.QPushButton
    pushButton_Playfair: QtWidgets.QPushButton
    pushButton_DES: QtWidgets.QPushButton
    pushButton_GOST: QtWidgets.QPushButton
    pushButton_exit: QtWidgets.QPushButton
    label_MainMenu_gif: QtWidgets.QLabel
    centralwidget: QtWidgets.QWidget
    statusbar: QtWidgets.QStatusBar

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(825, 600))
        MainWindow.setMaximumSize(QtCore.QSize(825, 600))
        MainWindow.setBaseSize(QtCore.QSize(825, 600))
        MainWindow.setStyleSheet("background-color: rgb(32, 28, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = UiHelper.set_font("Droid Sans Mono", size=11, bold=True)

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(150, 520, 530, 45))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_exit.setStyleSheet(UiHelper.exit_style())
        self.pushButton_exit.setObjectName("Exit")

        self.pushButton_Atbash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Atbash.setGeometry(QtCore.QRect(10, 200, 265, 65))
        self.pushButton_Atbash.setFont(font)
        self.pushButton_Atbash.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Atbash.setObjectName("Atbash")
        self.pushButton_Atbash.setStyleSheet(UiHelper.default_style())

        self.pushButton_Scytale = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Scytale.setGeometry(QtCore.QRect(10, 270, 265, 65))
        self.pushButton_Scytale.setFont(font)
        self.pushButton_Scytale.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Scytale.setObjectName("pushButton_Scytale")
        self.pushButton_Scytale.setStyleSheet(UiHelper.default_style())

        self.pushButton_PolybiusSquare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PolybiusSquare.setGeometry(QtCore.QRect(10, 340, 265, 65))
        self.pushButton_PolybiusSquare.setFont(font)
        self.pushButton_PolybiusSquare.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_PolybiusSquare.setObjectName("pushButton_PolybiusSquare")
        self.pushButton_PolybiusSquare.setStyleSheet(UiHelper.default_style())

        self.pushButton_Caesar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Caesar.setGeometry(QtCore.QRect(10, 410, 265, 65))
        self.pushButton_Caesar.setFont(font)
        self.pushButton_Caesar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Caesar.setStyleSheet(UiHelper.default_style())
        self.pushButton_Caesar.setObjectName("pushButton_Caesar")

        self.pushButton_Cardano = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cardano.setGeometry(QtCore.QRect(280, 200, 265, 65))
        self.pushButton_Cardano.setFont(font)
        self.pushButton_Cardano.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cardano.setStyleSheet(UiHelper.default_style())
        self.pushButton_Cardano.setObjectName("pushButton_Cardano")

        self.pushButton_Richelieu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Richelieu.setGeometry(QtCore.QRect(280, 270, 265, 65))
        self.pushButton_Richelieu.setFont(font)
        self.pushButton_Richelieu.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Richelieu.setStyleSheet(UiHelper.default_style())
        self.pushButton_Richelieu.setObjectName("pushButton_Richelieu")

        self.pushButton_Alberti = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Alberti.setGeometry(QtCore.QRect(280, 340, 265, 65))
        self.pushButton_Alberti.setFont(font)
        self.pushButton_Alberti.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Alberti.setStyleSheet(UiHelper.default_style())
        self.pushButton_Alberti.setObjectName("pushButton_Alberti")

        self.pushButton_Gronsfeld = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gronsfeld.setGeometry(QtCore.QRect(280, 410, 265, 65))
        self.pushButton_Gronsfeld.setFont(font)
        self.pushButton_Gronsfeld.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Gronsfeld.setStyleSheet(UiHelper.default_style())
        self.pushButton_Gronsfeld.setObjectName("pushButton_Gronsfeld")

        self.pushButton_Vigenere = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Vigenere.setGeometry(QtCore.QRect(550, 200, 265, 65))
        self.pushButton_Vigenere.setFont(font)
        self.pushButton_Vigenere.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Vigenere.setStyleSheet(UiHelper.default_style())
        self.pushButton_Vigenere.setObjectName("pushButton_Vigenere")

        self.pushButton_Playfair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Playfair.setGeometry(QtCore.QRect(550, 270, 265, 65))
        self.pushButton_Playfair.setFont(font)
        self.pushButton_Playfair.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_Playfair.setStyleSheet(UiHelper.default_style())
        self.pushButton_Playfair.setObjectName("pushButton_Playfair")

        self.pushButton_DES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DES.setGeometry(QtCore.QRect(550, 340, 265, 65))
        self.pushButton_DES.setFont(font)
        self.pushButton_DES.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_DES.setStyleSheet(UiHelper.default_style())
        self.pushButton_DES.setObjectName("pushButton_DES")

        self.pushButton_GOST = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GOST.setGeometry(QtCore.QRect(550, 410, 265, 65))
        self.pushButton_GOST.setFont(font)
        self.pushButton_GOST.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_GOST.setStyleSheet(UiHelper.default_style())
        self.pushButton_GOST.setObjectName("pushButton_GOST")

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
        self.pushButton_Gronsfeld.setText(_translate("MainWindow", "Шифр Гронсфельда"))
        self.pushButton_Alberti.setText(_translate("MainWindow", "Шифр Диск Альберти"))
        self.pushButton_Vigenere.setText(_translate("MainWindow", "Шифр Вижинера"))
        self.pushButton_Cardano.setText(_translate("MainWindow", "Шифр Кардано"))
        self.pushButton_Richelieu.setText(_translate("MainWindow", "Шифр Ришелье"))
        self.pushButton_Playfair.setText(_translate("MainWindow", "Шифр Плейфера"))
        self.pushButton_DES.setText(_translate("MainWindow", "Шифр DES"))
        self.pushButton_GOST.setText(_translate("MainWindow", "Шифр ГОСТ"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход из программы"))
