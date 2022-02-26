import string as ascii_symbols
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PolybiusSquare(object):
    def setupUi(self, PolybiusSquare):
        PolybiusSquare.setObjectName("PolybiusSquare")
        PolybiusSquare.resize(800, 600)
        PolybiusSquare.setMinimumSize(QtCore.QSize(800, 600))
        PolybiusSquare.setMaximumSize(QtCore.QSize(800, 600))
        PolybiusSquare.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(PolybiusSquare)
        self.centralwidget.setObjectName("centralwidget")

        self.label_PolybiusSquare_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_PolybiusSquare_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_PolybiusSquare_gif.setObjectName("label_PolybiusSquare_gif")
        gif = QtGui.QMovie("media/polybius_square.gif")
        self.label_PolybiusSquare_gif.setMovie(gif)
        gif.start()

        font = self.set_font(size=9)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(480, 30, 291, 221))
        self.label_info.setFont(font)
        self.label_info.setStyleSheet(self.text_area_style())
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        font = self.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 270, 739, 101))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(self.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 420, 739, 101))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(self.text_area_style())
        self.textBrowser.setObjectName("textBrowser")

        font = self.set_font("Uroob", size=10, weight=75, bold=True)

        self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 380, 201, 31))
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setStyleSheet(self.encrypt_style())

        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(240, 380, 201, 31))
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setStyleSheet(self.encrypt_style())

        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(460, 380, 151, 31))
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_paste.setStyleSheet(self.default_style())

        self.pushButton_clearInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearInput.setGeometry(QtCore.QRect(460, 530, 151, 31))
        self.pushButton_clearInput.setFont(font)
        self.pushButton_clearInput.setObjectName("pushButton_clearInput")
        self.pushButton_clearInput.setStyleSheet(self.default_style())

        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(620, 380, 151, 31))
        self.pushButton_copy.setFont(font)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setStyleSheet(self.default_style())

        self.pushButton_clearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setGeometry(QtCore.QRect(620, 530, 151, 31))
        self.pushButton_clearOutput.setFont(font)
        self.pushButton_clearOutput.setObjectName("pushButton_clearOutput")
        self.pushButton_clearOutput.setStyleSheet(self.default_style())

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 530, 201, 31))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet(self.exit_style())

        PolybiusSquare.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PolybiusSquare)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        PolybiusSquare.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.retranslateUi(PolybiusSquare)
        QtCore.QMetaObject.connectSlotsByName(PolybiusSquare)

    def retranslateUi(self, PolybiusSquare):
        _translate = QtCore.QCoreApplication.translate
        PolybiusSquare.setWindowTitle(_translate("PolybiusSquare", "POLYBIUS SQUARE"))

        self.pushButton_encrypt.setText(_translate("PolybiusSquare", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("PolybiusSquare", "Расшифровать"))
        self.pushButton_paste.setText(_translate("PolybiusSquare", "Вставить"))
        self.pushButton_clearInput.setText(_translate("PolybiusSquare", "Копировать"))
        self.pushButton_copy.setText(_translate("PolybiusSquare", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("PolybiusSquare", "Очистить"))
        self.pushButton_exit.setText(_translate("PolybiusSquare", "Закрыть окно"))

        self.label_info.setText(_translate("PolybiusSquare", "⚠ Алфавит для шифрования и\nрасшифрования "
                                                             "определяется по\nпервой встреченной букве.\n\n"
                                                             "⚠ J отождествляется с I.\n\n"
                                                             "⚠ Символы, не попавшие в\nалфавит,"
                                                             " останутся неизменными.\n\n"
                                                             "Ввод текста: верхнее поле.\nРезультат: нижнее поле"))

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


class UiMethod(QtWidgets.QMainWindow, Ui_PolybiusSquare):
    def __init__(self):
        super().__init__()

        self.rus_table = self.set_rus_table()
        self.eng_table = self.set_eng_table()

        a = ord('а')
        self.eng = ascii_symbols.printable[36:62]
        self.rus = [chr(i).upper() for i in range(a, a + 6)] + \
                   [chr(a + 33).upper()] + ["`", "~", "^"] + \
                   [chr(i).upper() for i in range(a + 6, a + 32)]

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
        string = self.plainTextEdit.toPlainText().upper()
        string = string.replace("J", "I")
        self.textBrowser.setText("")

        table, locale = self.scan_string(string)
        if table == "empty":
            self.textBrowser.setText(string)
            self.statusbar.showMessage("Текст зашифрован.")
            return

        self.result = ""
        coordinates = ["", ""]
        converted_coordinates = ""

        for letter in string:
            if letter not in locale:
                continue

            for i in range(len(table)):
                for j in range(len(table)):
                    if letter == table[i][j]:
                        coordinates[0] += str(j)
                        coordinates[1] += str(i)
                        break

        for i in range(2):
            for coordinate in coordinates[i]:
                converted_coordinates += coordinate

        for letter in string:
            if letter not in locale:
                self.result += letter
                continue

            y = int(converted_coordinates[1])
            x = int(converted_coordinates[0])
            converted_coordinates = converted_coordinates[2:]

            self.result += table[y][x]

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        string = self.plainTextEdit.toPlainText().upper()
        self.textBrowser.setText("")

        table, locale = self.scan_string(string)
        if table == "empty":
            self.textBrowser.setText(string)
            self.statusbar.showMessage("Текст зашифрован.")
            return

        self.result = ""
        coordinates = ["", ""]
        converted_coordinates = ""

        for letter in string:
            if letter not in locale:
                continue

            for i in range(len(table)):
                for j in range(len(table)):
                    if letter == table[i][j]:
                        converted_coordinates += str(j) + str(i)
                        break

        coordinates[0] = converted_coordinates[:len(converted_coordinates)//2]
        coordinates[1] = converted_coordinates[len(converted_coordinates)//2:]

        for letter in string:
            if letter not in locale:
                self.result += letter
                continue

            y = int(coordinates[1][0])
            x = int(coordinates[0][0])
            coordinates[0] = coordinates[0][1:]
            coordinates[1] = coordinates[1][1:]

            self.result += table[y][x]

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст расшифрован")

    @staticmethod
    def set_rus_table():
        return [
            ["А", "Б", "В", "Г", "Д", "Е"],
            ["Ё", "Ж", "З", "И", "Й", "К"],
            ["Л", "М", "Н", "О", "П", "Р"],
            ["С", "Т", "У", "Ф", "Х", "Ц"],
            ["Ч", "Ш", "Щ", "Ъ", "Ы", "Ь"],
            ["Э", "Ю", "Я", "~", "`", "^"]
        ]

    @staticmethod
    def set_eng_table():
        return [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "K"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z"],
        ]