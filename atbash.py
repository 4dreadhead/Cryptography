import string as ascii_symbols
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Atbash(object):
    def setupUi(self, Atbash):
        Atbash.setObjectName("Atbash")
        Atbash.resize(800, 600)
        Atbash.setMinimumSize(QtCore.QSize(800, 600))
        Atbash.setMaximumSize(QtCore.QSize(800, 600))
        Atbash.setStyleSheet("background-color: rgb(32, 28, 42);")
        self.centralwidget = QtWidgets.QWidget(Atbash)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label.setText("")
        self.label.setObjectName("label")
        gif = QtGui.QMovie("atbash.gif")
        self.label.setMovie(gif)
        gif.start()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 30, 291, 221))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(48, 42, 61);\n"
                                   "color: rgb(238, 238, 236);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 270, 739, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(48, 42, 61);\n"
                                         "color: rgb(238, 238, 236);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 380, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 380, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 420, 739, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(48, 42, 61);\n"
                                       "color: rgb(238, 238, 236);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 530, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 530, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 530, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("""QPushButton:hover { background-color: rgb(64, 56, 84);
                                                               color: rgb(14,149,226); }
                                           QPushButton:!hover { background-color: rgb(48, 42, 61);
                                                                color: rgb(14,149,226); }
                                           QPushButton:pressed { background-color: rgb(24, 21, 30);
                                                                 color: rgb(14,149,226); }""")
        self.pushButton_6.setObjectName("pushButton_6")
        Atbash.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Atbash)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Atbash.setStatusBar(self.statusbar)

        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))


        self.retranslateUi(Atbash)
        QtCore.QMetaObject.connectSlotsByName(Atbash)

    def retranslateUi(self, Atbash):
        _translate = QtCore.QCoreApplication.translate
        Atbash.setWindowTitle(_translate("Atbash", "MainWindow"))
        self.label_2.setText(_translate("Atbash", "Поддерживаемые алфавиты:\n"
                                                  "⚫ Латинский\n"
                                                  "⚫ Кириллица\n"
                                                  "\n"
                                                  "⚠ Все символы,\n"
                                                  "не входящие в них,\n"
                                                  "останутся неизменными.\n"
                                                  "\n"
                                                  "Ввод текста - верхнее поле\n"
                                                  "Результат - нижнее поле"))
        self.pushButton_2.setText(_translate("Atbash", "Вставить из буфера обмена"))
        self.pushButton.setText(_translate("Atbash", "Зашифровать/Расшифровать"))
        self.textBrowser.setHtml(_translate("Atbash",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \""
                                            "http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                            "<style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; "
                                            "font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                                            "\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("Atbash", "Копировать в буфер обмена"))
        self.pushButton_4.setText(_translate("Atbash", "Закрыть окно"))
        self.pushButton_5.setText(_translate("Atbash", "Очистить"))
        self.pushButton_6.setText(_translate("Atbash", "Очистить"))

    def __str__(self):
        return "Atbash"


class UiMethod(QtWidgets.QMainWindow, Ui_Atbash):
    def __init__(self):
        super().__init__()

        a = ord('а')
        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.result = ""

        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.paste_from_buffer)
        self.pushButton_4.clicked.connect(self.close_window)
        self.pushButton_3.clicked.connect(self.copy_to_buffer)
        self.pushButton_5.clicked.connect(self.clear_input)
        self.pushButton_6.clicked.connect(self.clear_output)

    def clear_input(self):
        self.plainTextEdit.clear()
        self.statusbar.showMessage("Поле ввода очищено.")

    def clear_output(self):
        self.textBrowser.clear()
        self.result = ""
        self.statusbar.showMessage("Поле вывода очищено.")

    def close_window(self):
        self.close()

    def copy_to_buffer(self):
        pyperclip.copy(self.result)
        self.statusbar.showMessage("Результат скопирован в буффер обмена.")

    def paste_from_buffer(self):
        self.plainTextEdit.setPlainText(pyperclip.paste())
        self.statusbar.showMessage("Текст вставлен из буффера обмена.")

    def encrypt_and_decrypt(self, encrypted_or_decrypted_string):
        decrypted_or_encrypted_string = ""
        for symbol in encrypted_or_decrypted_string:
            if symbol in self.cyrillic_low:
                symbol = self.transform(symbol, self.cyrillic_low)

            elif symbol in self.cyrillic_high:
                symbol = self.transform(symbol, self.cyrillic_high)

            elif symbol in self.latin_low:
                symbol = self.transform(symbol, self.latin_low)

            elif symbol in self.latin_high:
                symbol = self.transform(symbol, self.latin_high)

            decrypted_or_encrypted_string += symbol
        return decrypted_or_encrypted_string

    def encrypt(self):
        string = self.plainTextEdit.toPlainText()
        self.result = self.encrypt_and_decrypt(string)
        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован/расшифрован.")

    @staticmethod
    def transform(symbol, container):
        index = container.index(symbol)
        return container[len(container) - (index + 1)]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = UiMethod()
    myapp.show()
    sys.exit(app.exec_())