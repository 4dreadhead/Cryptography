from PyQt5 import QtCore, QtGui, QtWidgets
import atbash
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(810, 551)
        MainWindow.setMinimumSize(QtCore.QSize(810, 551))
        MainWindow.setMaximumSize(QtCore.QSize(810, 551))
        MainWindow.setBaseSize(QtCore.QSize(810, 551))
        MainWindow.setStyleSheet("background-color: rgb(32, 28, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 200, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 270, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 340, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 410, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 410, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 340, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 200, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 200, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 270, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(540, 270, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 340, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 410, 270, 70))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(201,44,123); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(201,44,123); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(201,44,123); }""")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 500, 810, 30))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 10, 831, 181))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("background-image: url(./main_menu.gif)")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHY"))
        self.pushButton.setText(_translate("MainWindow", "Шифр Атбаш"))
        self.pushButton_2.setText(_translate("MainWindow", "# Шифр Сцитала"))
        self.pushButton_3.setText(_translate("MainWindow", "# Шифр Квадрат Полибия"))
        self.pushButton_4.setText(_translate("MainWindow", "# Шифр Цезаря"))
        self.pushButton_5.setText(_translate("MainWindow", "# Шифр Гронсфельда"))
        self.pushButton_6.setText(_translate("MainWindow", "# Шифр Диск Альберти"))
        self.pushButton_7.setText(_translate("MainWindow", "# Шифр Вижинера"))
        self.pushButton_8.setText(_translate("MainWindow", "# Шифр Кардано"))
        self.pushButton_9.setText(_translate("MainWindow", "# Шифр Ришелье"))
        self.pushButton_10.setText(_translate("MainWindow", "# Шифр Плейфера"))
        self.pushButton_11.setText(_translate("MainWindow", "# Криптосхема Хилла"))
        self.pushButton_12.setText(_translate("MainWindow", "# Шифр Вернама"))
        self.pushButton_13.setText(_translate("MainWindow", "Выход из программы"))


class MainMenu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run_atbash)
        self.pushButton_13.clicked.connect(self.close_program)

    def run_atbash(self):
        self.mySecond = atbash.UiMethod()
        self.mySecond.show()

    def close_program(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainMenu()
    myapp.show()
    sys.exit(app.exec_())
