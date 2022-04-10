import string as ascii_symbols
from lib.helpers import WindowHelper
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiAlberti


class AlbertiWindow(QMainWindow, UiAlberti, WindowHelper):
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
        self.result = ""
        a = ord('а')

        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = list(ascii_symbols.printable[10:36])
        self.latin_high = list(ascii_symbols.printable[36:62])

        self.cyrillic_low_disk = self.generate_disk(self.cyrillic_low)
        self.cyrillic_high_disk = self.generate_disk(self.cyrillic_high)
        self.latin_low_disk = self.generate_disk(self.latin_low)
        self.latin_high_disk = self.generate_disk(self.latin_high)

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
