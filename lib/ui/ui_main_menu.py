from PyQt5 import QtCore, QtGui, QtWidgets
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
    pushButton_exit: QtWidgets.QPushButton
    label_MainMenu_gif: QtWidgets.QLabel
    centralwidget: QtWidgets.QWidget
    statusbar: QtWidgets.QStatusBar

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(810, 600))
        MainWindow.setMaximumSize(QtCore.QSize(810, 600))
        MainWindow.setBaseSize(QtCore.QSize(810, 600))
        MainWindow.setStyleSheet("background-color: rgb(32, 28, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = UiHelper.set_font("Uroob", size=11, bold=True)

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(140, 520, 530, 45))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setStyleSheet(UiHelper.exit_style())
        self.pushButton_exit.setObjectName("Exit")

        self.pushButton_Atbash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Atbash.setGeometry(QtCore.QRect(0, 200, 270, 70))
        self.pushButton_Atbash.setFont(font)
        self.pushButton_Atbash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Atbash.setObjectName("Atbash")
        self.pushButton_Atbash.setStyleSheet(UiHelper.default_style())

        self.pushButton_Scytale = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Scytale.setGeometry(QtCore.QRect(0, 270, 270, 70))
        self.pushButton_Scytale.setFont(font)
        self.pushButton_Scytale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Scytale.setObjectName("pushButton_Scytale")
        self.pushButton_Scytale.setStyleSheet(UiHelper.default_style())

        self.pushButton_PolybiusSquare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PolybiusSquare.setGeometry(QtCore.QRect(0, 340, 270, 70))
        self.pushButton_PolybiusSquare.setFont(font)
        self.pushButton_PolybiusSquare.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_PolybiusSquare.setObjectName("pushButton_PolybiusSquare")
        self.pushButton_PolybiusSquare.setStyleSheet(UiHelper.default_style())

        self.pushButton_Caesar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Caesar.setGeometry(QtCore.QRect(0, 410, 270, 70))
        self.pushButton_Caesar.setFont(font)
        self.pushButton_Caesar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Caesar.setStyleSheet(UiHelper.default_style())
        self.pushButton_Caesar.setObjectName("pushButton_Caesar")

        self.pushButton_Cardano = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cardano.setGeometry(QtCore.QRect(270, 200, 270, 70))
        self.pushButton_Cardano.setFont(font)
        self.pushButton_Cardano.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Cardano.setStyleSheet(UiHelper.default_style())
        self.pushButton_Cardano.setObjectName("pushButton_Cardano")

        self.pushButton_Richelieu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Richelieu.setGeometry(QtCore.QRect(270, 270, 270, 70))
        self.pushButton_Richelieu.setFont(font)
        self.pushButton_Richelieu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Richelieu.setStyleSheet(UiHelper.default_style())
        self.pushButton_Richelieu.setObjectName("pushButton_Richelieu")

        self.pushButton_Alberti = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Alberti.setGeometry(QtCore.QRect(270, 340, 270, 70))
        self.pushButton_Alberti.setFont(font)
        self.pushButton_Alberti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Alberti.setStyleSheet(UiHelper.default_style())
        self.pushButton_Alberti.setObjectName("pushButton_Alberti")

        self.pushButton_Gronsfeld = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gronsfeld.setGeometry(QtCore.QRect(270, 410, 270, 70))
        self.pushButton_Gronsfeld.setFont(font)
        self.pushButton_Gronsfeld.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Gronsfeld.setStyleSheet(UiHelper.default_style())
        self.pushButton_Gronsfeld.setObjectName("pushButton_Gronsfeld")

        self.pushButton_Vigenere = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Vigenere.setGeometry(QtCore.QRect(540, 200, 270, 70))
        self.pushButton_Vigenere.setFont(font)
        self.pushButton_Vigenere.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Vigenere.setStyleSheet(UiHelper.default_style())
        self.pushButton_Vigenere.setObjectName("pushButton_Vigenere")

        self.pushButton_Playfair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Playfair.setGeometry(QtCore.QRect(540, 270, 270, 70))
        self.pushButton_Playfair.setFont(font)
        self.pushButton_Playfair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Playfair.setStyleSheet(UiHelper.default_style())
        self.pushButton_Playfair.setObjectName("pushButton_Playfair")

        # In development buttons area

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 340, 270, 70))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(UiHelper.in_development_style())
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 410, 270, 70))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(UiHelper.in_development_style())
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
        self.pushButton_Atbash.setText(_translate("MainWindow", "???????? ??????????"))
        self.pushButton_Scytale.setText(_translate("MainWindow", "???????? ??????????????"))
        self.pushButton_PolybiusSquare.setText(_translate("MainWindow", "???????? ?????????????? ??????????????"))
        self.pushButton_Caesar.setText(_translate("MainWindow", "???????? ????????????"))
        self.pushButton_Gronsfeld.setText(_translate("MainWindow", "???????? ??????????????????????"))
        self.pushButton_Alberti.setText(_translate("MainWindow", "???????? ???????? ????????????????"))
        self.pushButton_Vigenere.setText(_translate("MainWindow", "???????? ????????????????"))
        self.pushButton_Cardano.setText(_translate("MainWindow", "???????? ??????????????"))
        self.pushButton_Richelieu.setText(_translate("MainWindow", "???????? ??????????????"))
        self.pushButton_Playfair.setText(_translate("MainWindow", "???????? ????????????????"))
        self.pushButton_11.setText(_translate("MainWindow", "?????????????????????? ??????????"))
        self.pushButton_12.setText(_translate("MainWindow", "???????? ??????????????"))
        self.pushButton_exit.setText(_translate("MainWindow", "?????????? ???? ??????????????????"))
