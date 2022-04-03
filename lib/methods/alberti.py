import string as ascii_symbols
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class UiAlberti(object):
    def setupUi(self, Alberti):
        Alberti.setObjectName("Alberti")
        Alberti.resize(800, 650)
        Alberti.setMinimumSize(QtCore.QSize(800, 650))
        Alberti.setMaximumSize(QtCore.QSize(800, 650))
        Alberti.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Alberti)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Alberti_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Alberti_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_Alberti_gif.setObjectName("label_alberti_gif")
        gif = QtGui.QMovie("lib/media/alberti.gif")
        self.label_Alberti_gif.setMovie(gif)
        gif.start()

        font = self.set_font(size=9)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(480, 30, 289, 279))
        self.label_info.setFont(font)
        self.label_info.setStyleSheet(self.text_area_style())
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        self.label_info_key = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key.setGeometry(QtCore.QRect(201, 278, 260, 31))
        self.label_info_key.setFont(font)
        self.label_info_key.setStyleSheet(self.text_area_style())
        self.label_info_key.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_key.setObjectName("label_info")

        font = self.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 320, 739, 101))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(self.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_key.setGeometry(QtCore.QRect(30, 278, 150, 31))
        self.plainTextEdit_key.setFont(font)
        self.plainTextEdit_key.setStyleSheet(self.text_area_style())
        self.plainTextEdit_key.setObjectName("plainTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 470, 739, 101))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(self.text_area_style())
        self.textBrowser.setObjectName("textBrowser")

        font = self.set_font("Uroob", size=10, weight=75, bold=True)

        self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 430, 201, 31))
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setStyleSheet(self.encrypt_style())

        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(240, 430, 201, 31))
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setStyleSheet(self.encrypt_style())

        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(460, 430, 151, 31))
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_paste.setStyleSheet(self.default_style())

        self.pushButton_clearInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearInput.setGeometry(QtCore.QRect(460, 580, 151, 31))
        self.pushButton_clearInput.setFont(font)
        self.pushButton_clearInput.setObjectName("pushButton_clearInput")
        self.pushButton_clearInput.setStyleSheet(self.default_style())

        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(620, 430, 151, 31))
        self.pushButton_copy.setFont(font)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setStyleSheet(self.default_style())

        self.pushButton_clearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setGeometry(QtCore.QRect(620, 580, 151, 31))
        self.pushButton_clearOutput.setFont(font)
        self.pushButton_clearOutput.setObjectName("pushButton_clearOutput")
        self.pushButton_clearOutput.setStyleSheet(self.default_style())

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 580, 201, 31))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet(self.exit_style())

        Alberti.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Alberti)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Alberti.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.retranslateUi(Alberti)
        QtCore.QMetaObject.connectSlotsByName(Alberti)

    def retranslateUi(self, Alberti):
        _translate = QtCore.QCoreApplication.translate
        Alberti.setWindowTitle(_translate("Alberti", "ALBERTI"))

        self.pushButton_encrypt.setText(_translate("Alberti", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Alberti", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Alberti", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Alberti", "Копировать"))
        self.pushButton_copy.setText(_translate("Alberti", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Alberti", "Очистить"))
        self.pushButton_exit.setText(_translate("Alberti", "Закрыть окно"))

        self.label_info.setText(_translate("Alberti", "Поддерживаемые алфавиты:\n⚫ Латинский\n⚫ Кириллица\n\n"
                                                     "⚠ Все символы,\nне входящие в них,\nостанутся неизменными.\n\n"
                                                     "Ввод текста: верхнее поле\nРезультат: нижнее поле"))

        self.label_info_key.setText(_translate("Alberti", "⟵ Введите ключ."))

        self.textBrowser.setHtml(_translate("Alberti",
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

    @staticmethod
    def set_font(family=None, size=12, weight=None, bold=False, italic=False):
        font = QtGui.QFont()
        if family:
            font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        if weight:
            font.setWeight(weight)
        return font

    @staticmethod
    def text_area_style():
        style = "background-color: rgb(48, 42, 61);\ncolor: rgb(238, 238, 236);"
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
    def encrypt_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                       color: rgb(28,180,230); }
                   QPushButton:!hover { background-color: rgb(48, 42, 61);
                                        color: rgb(28,180,230); }
                   QPushButton:pressed { background-color: rgb(24, 21, 30);
                                         color: rgb(28,180,230); }"""
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


class AlbertiWindow(QtWidgets.QMainWindow, UiAlberti):
    def __init__(self):
        super().__init__()

        a = ord('а')
        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = list(ascii_symbols.printable[10:36])
        self.latin_high = list(ascii_symbols.printable[36:62])

        self.cyrillic_low_disk = self.generate_disk(self.cyrillic_low)
        self.cyrillic_high_disk = self.generate_disk(self.cyrillic_high)
        self.latin_low_disk = self.generate_disk(self.latin_low)
        self.latin_high_disk = self.generate_disk(self.latin_high)

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('lib/media/icon.png'))
        self.result = ""

        self.pushButton_encrypt.clicked.connect(self.encrypt)
        self.pushButton_decrypt.clicked.connect(self.decrypt)
        self.pushButton_paste.clicked.connect(self.paste_from_buffer)
        self.pushButton_clearInput.clicked.connect(self.copy_to_buffer)
        self.pushButton_copy.clicked.connect(self.clear_input)
        self.pushButton_clearOutput.clicked.connect(self.clear_output)
        self.pushButton_exit.clicked.connect(self.close_window)

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

    @staticmethod
    def generate_disk(alphabet):
        return {index: alphabet[index:] + alphabet[:index] for index in range(len(alphabet))}

    @staticmethod
    def generate_dict(alphabet):
        return {letter: index for index, letter in enumerate(alphabet)}

    def parse_key(self, string):
        user_input_key = self.plainTextEdit_key.toPlainText()
        if len(user_input_key) == 0:
            self.statusbar.showMessage("Некорректное значение ключа.")
            return
        for symbol in user_input_key:
            if symbol not in (self.latin_low + self.latin_high + self.cyrillic_low + self.cyrillic_high):
                self.statusbar.showMessage("Некорректное значение ключа.")
                return

        key = user_input_key
        while len(key) < len(string):
            key += user_input_key
        key = list(key[:len(string)])

        for alphabet in [
            self.generate_dict(self.cyrillic_low),
            self.generate_dict(self.cyrillic_high),
            self.generate_dict(self.latin_low),
            self.generate_dict(self.latin_high)
        ]:
            for index, symbol in enumerate(key):
                if symbol in alphabet:
                    key[index] = alphabet[symbol]

        return key

    def encrypt(self):
        string = self.plainTextEdit.toPlainText()

        key = self.parse_key(string)
        if not key:
            return

        result = ""
        for symbol, index in zip(string, key):
            if symbol in self.cyrillic_low:
                result += self.cyrillic_low_disk[index][self.cyrillic_low.index(symbol)]
            elif symbol in self.cyrillic_high:
                result += self.cyrillic_high_disk[index][self.cyrillic_high.index(symbol)]
            elif symbol in self.latin_low:
                result += self.latin_low_disk[index % 26][self.latin_low.index(symbol)]
            elif symbol in self.latin_high:
                result += self.latin_high_disk[index % 26][self.latin_high.index(symbol)]
            else:
                result += symbol

        self.result = result
        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        string = self.plainTextEdit.toPlainText()

        key = self.parse_key(string)
        if not key:
            return

        result = ""

        for symbol, index in zip(string, key):
            if symbol in self.cyrillic_low:
                result += self.cyrillic_low[self.cyrillic_low_disk[index].index(symbol)]
            elif symbol in self.cyrillic_high:
                result += self.cyrillic_high[self.cyrillic_high_disk[index].index(symbol)]
            elif symbol in self.latin_low:
                result += self.latin_low[self.latin_low_disk[index % 26].index(symbol)]
            elif symbol in self.latin_high:
                result += self.latin_high[self.latin_high_disk[index % 26].index(symbol)]
            else:
                result += symbol

        self.result = result
        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован.")
