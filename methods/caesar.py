import string as ascii_symbols
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Caesar(object):
    def setupUi(self, Caesar):
        Caesar.setObjectName("Caesar")
        Caesar.resize(800, 650)
        Caesar.setMinimumSize(QtCore.QSize(800, 650))
        Caesar.setMaximumSize(QtCore.QSize(800, 650))
        Caesar.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Caesar)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Caesar_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Caesar_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_Caesar_gif.setObjectName("label_caesar_gif")
        gif = QtGui.QMovie("media/caesar.gif")
        self.label_Caesar_gif.setMovie(gif)
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

        Caesar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Caesar)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Caesar.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.retranslateUi(Caesar)
        QtCore.QMetaObject.connectSlotsByName(Caesar)

    def retranslateUi(self, Caesar):
        _translate = QtCore.QCoreApplication.translate
        Caesar.setWindowTitle(_translate("Caesar", "CAESAR"))

        self.pushButton_encrypt.setText(_translate("Caesar", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Caesar", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Caesar", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Caesar", "Копировать"))
        self.pushButton_copy.setText(_translate("Caesar", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Caesar", "Очистить"))
        self.pushButton_exit.setText(_translate("Caesar", "Закрыть окно"))

        self.label_info.setText(_translate("Caesar", "Поддерживаемые алфавиты:\n⚫ Латинский\n⚫ Кириллица\n\n"
                                                     "⚠ Все символы,\nне входящие в них,\nостанутся неизменными.\n\n"
                                                     "Ввод текста: верхнее поле\nРезультат: нижнее поле"))

        self.label_info_key.setText(_translate("Caesar", "⟵ Введите ключ (целое число)."))

        self.textBrowser.setHtml(_translate("Scytale",
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


class UiMethod(QtWidgets.QMainWindow, Ui_Caesar):
    def __init__(self):
        super().__init__()

        a = ord('а')
        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('media/icon.png'))
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

    def scan_string(self, string):
        for letter in string:
            if letter in self.rus:
                return self.rus_table, self.rus
            elif letter in self.eng:
                return self.eng_table, self.eng
            else:
                continue
        return "empty", None

    def encrypt(self):
        key = self.extract_key()
        if not key:
            self.statusbar.showMessage("Некорректное значение ключа")
            return

        string = self.plainTextEdit.toPlainText()
        self.result = string
        self.textBrowser.setText("")

        mixed_alphabets = self.mix_alphabets(key)
        for i in range(4):
            origin = mixed_alphabets[0]
            destination = mixed_alphabets[1]
            mixed_alphabets = mixed_alphabets[2:]

            self.result = self.replace_symbols(self.result, origin, destination)

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        key = self.extract_key()
        if not key:
            self.statusbar.showMessage("Некорректное значение ключа")
            return

        string = self.plainTextEdit.toPlainText()
        self.result = string
        self.textBrowser.setText("")

        mixed_alphabets = self.mix_alphabets(key)
        for i in range(4):
            origin = mixed_alphabets[1]
            destination = mixed_alphabets[0]
            mixed_alphabets = mixed_alphabets[2:]

            self.result = self.replace_symbols(self.result, origin, destination)

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def extract_key(self):
        try:
            return int(self.plainTextEdit_key.toPlainText())
        except Exception:
            return None

    def mix_alphabets(self, key):
        return [
            "".join(self.cyrillic_low), "".join(self.transform(self.cyrillic_low, key)),
            "".join(self.cyrillic_high), "".join(self.transform(self.cyrillic_high, key)),
            "".join(self.latin_low), "".join(self.transform(self.latin_low, key)),
            "".join(self.latin_high), "".join(self.transform(self.latin_high, key))
        ]

    @staticmethod
    def transform(alphabet, key):
        mixed_alphabet = []
        for i in range(len(alphabet)):
            mixed_alphabet.append(alphabet[(i + key) % len(alphabet)])
        return mixed_alphabet

    @staticmethod
    def replace_symbols(string, origin, destination):
        result_string = ""
        for letter in string:
            try:
                index = origin.index(letter)
                result_string += destination[index]
            except ValueError:
                result_string += letter
        return result_string
