import string as ascii_symbols
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from lib.ui import UiPolybiusSquare
from lib.helpers import WindowHelper


class PolybiusSquareWindow(QMainWindow, UiPolybiusSquare, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        # Window initialization area
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('lib/media/icon.png'))
        self.pushButton_encrypt.clicked.connect(self.encrypt)
        self.pushButton_decrypt.clicked.connect(self.decrypt)
        self.pushButton_paste.clicked.connect(self.paste_from_buffer)
        self.pushButton_clearInput.clicked.connect(self.copy_to_buffer)
        self.pushButton_copy.clicked.connect(self.clear_input)
        self.pushButton_clearOutput.clicked.connect(self.clear_output)
        self.pushButton_exit.clicked.connect(self.close)

        # Method area
        self.rus_table = self.set_rus_table()
        self.eng_table = self.set_eng_table()

        self.result = ""
        a = ord('а')
        self.eng = ascii_symbols.printable[36:62]
        self.rus = [chr(i).upper() for i in range(a, a + 6)] + \
                   [chr(a + 33).upper()] + ["`", "~", "^"] + \
                   [chr(i).upper() for i in range(a + 6, a + 32)]

    def encrypt(self):
        string = self.plainTextEdit.toPlainText()
        string = string.replace("J", "I").replace("j", "i")
        self.textBrowser.setText("")

        for key in range(2):
            table, locale = (self.eng_table, self.eng) if key == 0 else (self.rus_table, self.rus)

            result = ""
            coordinates = ["", ""]
            converted_coordinates = ""

            for letter in string:
                if letter.upper() not in locale:
                    continue

                for i in range(len(table)):
                    for j in range(len(table)):
                        if letter.upper() == table[i][j]:
                            coordinates[0] += str(j)
                            coordinates[1] += str(i)
                            break

            for i in range(2):
                for coordinate in coordinates[i]:
                    converted_coordinates += coordinate

            for letter in string:
                if letter.upper() not in locale:
                    result += letter
                    continue

                y = int(converted_coordinates[1])
                x = int(converted_coordinates[0])
                converted_coordinates = converted_coordinates[2:]

                result += table[y][x] if letter.isupper() else table[y][x].lower()

            string = result
        self.result = string
        self.textBrowser.setText(string)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        string = self.plainTextEdit.toPlainText()
        string = string.replace("J", "I").replace("j", "i")
        self.textBrowser.setText("")
        for key in range(2):
            table, locale = (self.eng_table, self.eng) if key == 0 else (self.rus_table, self.rus)

            result = ""
            coordinates = ["", ""]
            converted_coordinates = ""

            for letter in string:
                if letter.upper() not in locale:
                    continue

                for i in range(len(table)):
                    for j in range(len(table)):
                        if letter.upper() == table[i][j]:
                            converted_coordinates += str(j) + str(i)
                            break

            coordinates[0] = converted_coordinates[:len(converted_coordinates)//2]
            coordinates[1] = converted_coordinates[len(converted_coordinates)//2:]

            for letter in string:
                if letter.upper() not in locale:
                    result += letter
                    continue

                y = int(coordinates[1][0])
                x = int(coordinates[0][0])
                coordinates[0] = coordinates[0][1:]
                coordinates[1] = coordinates[1][1:]

                result += table[y][x] if letter.isupper() else table[y][x].lower()
            string = result
        self.result = string

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
