import re
import random
import string as ascii_symbols
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class InvalidKey(Exception):
    def __init__(self, *args):
        self.message = "" + str(args[0]) if args else "Wrong key value."

    def __str__(self):
        return f"{self.message}"


class UiCardano(object):
    def setupUi(self, Cardano):
        Cardano.setObjectName("Caesar")
        Cardano.resize(800, 650)
        Cardano.setMinimumSize(QtCore.QSize(800, 650))
        Cardano.setMaximumSize(QtCore.QSize(800, 650))
        Cardano.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Cardano)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Cardano_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Cardano_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_Cardano_gif.setObjectName("label_cardano_gif")
        gif = QtGui.QMovie("lib/media/cardano.gif")
        self.label_Cardano_gif.setMovie(gif)
        gif.start()

        font = self.set_font(size=9)

        self.label_info_key = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key.setGeometry(QtCore.QRect(201, 278, 260, 30))
        self.label_info_key.setFont(font)
        self.label_info_key.setStyleSheet(self.text_area_style())
        self.label_info_key.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_key.setObjectName("label_info")

        self.trash_box = QtWidgets.QCheckBox(self.centralwidget)
        self.trash_box.setGeometry(QtCore.QRect(30, 278, 150, 30))
        self.trash_box.setFont(font)
        self.trash_box.setStyleSheet("color: rgb(238, 238, 236);")
        self.trash_box.setObjectName("trash_box")
        self.trash_box.setChecked(True)

        font = self.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 320, 739, 101))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(self.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_key.setGeometry(QtCore.QRect(480, 40, 289, 269))
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

        Cardano.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Cardano)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Cardano.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.retranslateUi(Cardano)
        QtCore.QMetaObject.connectSlotsByName(Cardano)

    def retranslateUi(self, Cardano):
        _translate = QtCore.QCoreApplication.translate
        Cardano.setWindowTitle(_translate("Cardano", "RICHELIEU"))

        self.pushButton_encrypt.setText(_translate("Cardano", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Cardano", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Cardano", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Cardano", "Копировать"))
        self.pushButton_copy.setText(_translate("Cardano", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Cardano", "Очистить"))
        self.pushButton_exit.setText(_translate("Cardano", "Закрыть окно"))
        self.trash_box.setText(_translate("Cardano", "<<< Добавить мусор"))

        self.label_info_key.setText(_translate("Cardano", "Ключ >>>"))
        self.plainTextEdit_key.setPlainText(self.default_key())

        self.textBrowser.setHtml(_translate("Cardano",
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
    def default_key():
        key = "(0,1,0,0,0,0,1,0,0,1)\n" + \
              "(1,0,0,0,1,0,0,0,0,0)\n" + \
              "(0,1,0,0,0,1,0,0,1,0)\n" + \
              "(0,0,1,0,0,0,0,1,0,0)\n" + \
              "(1,0,0,1,0,1,1,0,0,1)\n" + \
              "(0,0,1,0,0,0,0,0,0,0)\n" + \
              "(1,1,0,0,0,0,1,0,1,0)\n" + \
              "(0,0,1,0,0,0,0,0,0,0)\n" + \
              "(0,0,0,0,1,0,0,0,1,0)\n" + \
              "(0,0,1,0,0,0,0,1,0,0)"
        return key

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


class CardanoWindow(QtWidgets.QMainWindow, UiCardano):
    def __init__(self):
        super().__init__()

        a = ord('а')
        self.cyrillic_low = "".join(
            [chr(i) for i in range(a, a + 6)] +
            [chr(a + 33)] +
            [chr(i) for i in range(a + 6, a + 32)]
        )
        self.cyrillic_high = "".join([i.swapcase() for i in self.cyrillic_low])
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

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

    def parse_keys(self):
        keys_pattern = r"\(\d+[,\d+]*\)"
        parsed_keys = []

        user_input_key = self.plainTextEdit_key.toPlainText()
        received_keys_string = re.findall(keys_pattern, user_input_key)

        # Check for valid user input string format
        if user_input_key != "\n".join(received_keys_string):
            raise InvalidKey("Unexpended key format.")

        # Convert keys to int
        for keys_block in received_keys_string:
            parsed_keys.append(list(map(int, keys_block[1:-1].split(","))))

        # Check for valid keys values
        size = len(received_keys_string)
        for keys in parsed_keys:
            if len(keys) != size:
                raise InvalidKey
            for key in keys:
                if key not in (0, 1):
                    raise InvalidKey

        # Check for non-duplicated cell after turn
        allowed_values = (0, 1) if self.trash_box.isChecked() else (1,)
        if size % 2 != 0:
            if not self.trash_box.isChecked():
                raise InvalidKey("Wrong Cardano Grill size.")
            if parsed_keys[size//2][size//2] == 1:
                raise InvalidKey(f"Wrong Cardano Grill: check cell value at {size//2, size//2}.")

        for i in range(size//2):
            for j in range(size//2):
                if (
                        parsed_keys[i][j] +
                        parsed_keys[size-1 - i][size-1 - j] +
                        parsed_keys[j][size-1 - i] +
                        parsed_keys[size-1 - j][i]
                ) not in allowed_values:
                    raise InvalidKey(f"Wrong Cardano Grill: check cell value at {i, j}.")
            if size % 2 != 0:
                if (
                        parsed_keys[i][size//2] +
                        parsed_keys[size//2][i] +
                        parsed_keys[size-1 - i][size//2] +
                        parsed_keys[size//2][size-1 - i]
                ) > 1:
                    raise InvalidKey(f"Wrong Cardano Grill: check cell value at {i, size//2}.")

        return parsed_keys, size

    def get_random_letter(self):
        return random.choice(self.cyrillic_low + self.cyrillic_high + self.latin_low + self.latin_high)

    def encrypt(self):
        try:
            grille, size = self.parse_keys()
            string = self.plainTextEdit.toPlainText()
            string += "␃" if self.trash_box.isChecked() else ""
            warning_message = ""

            control_sum = sum(map(lambda x: sum(x), grille)) * 4
            # Slice or add additional symbols if length of
            if len(string) < control_sum + 1 and not self.trash_box.isChecked():
                string = string.ljust(control_sum, "⋆")
                warning_message = " Предупреждение: Недостаточная длина строки, дополнена символами '⋆'."
            elif len(string) > control_sum + 1:
                string = string[:control_sum]
                warning_message = " Предупреждение: Слишком длинная строка, избыточные символы отброшены."

            encrypted_grid = [["" for _ in range(size)] for _ in range(size)]

            for _ in range(4):
                # Filling final grid
                for i in range(size):
                    for j in range(size):
                        if grille[i][j] == 1:
                            encrypted_grid[i][j] = string[0] if len(string) > 0 else self.get_random_letter()
                            string = string[1:]

                # Rotate the grille 90 degrees
                # grille = list(zip(*map(lambda x: list(reversed(x)), grille)))
                grille = list(zip(*grille[::-1]))

            if self.trash_box.isChecked():
                for i in range(size):
                    for j in range(size):
                        if len(encrypted_grid[i][j]) == 0:
                            encrypted_grid[i][j] = self.get_random_letter()

            self.result = "\n".join(list(map(lambda x: "".join(x), encrypted_grid)))
            self.statusbar.showMessage("Сообщение зашифровано." + warning_message)

            self.textBrowser.setText(self.result)

        except (InvalidKey, ValueError) as error:
            self.textBrowser.setText(str(error))
            self.statusbar.showMessage("Неверные входные данные, попробуйте снова.")

    def decrypt(self):
        try:
            grille, size = self.parse_keys()
            entered_string = list(self.plainTextEdit.toPlainText().replace("\n", ""))

            if len(entered_string) != size**2:
                raise ValueError("Entered message doesn't look correct.")

            string = []
            for _ in range(size):
                string.append(entered_string[:size])
                entered_string = entered_string[size:]

            result = ""
            for _ in range(4):
                # Catching symbols from grid
                for i in range(size):
                    for j in range(size):
                        if grille[i][j] == 1:
                            result += string[i][j]

                # Rotate the grille 90 degrees
                # grille = list(zip(*map(lambda x: list(reversed(x)), grille)))
                grille = list(zip(*grille[::-1]))

            self.result = result.split("␃")[0].replace("⋆", "")

            self.textBrowser.setText(self.result)
            self.statusbar.showMessage("Текст расшифрован")

        except (InvalidKey, ValueError) as error:
            self.textBrowser.setText(str(error))
            self.statusbar.showMessage("Неверные входные данные, попробуйте снова.")
