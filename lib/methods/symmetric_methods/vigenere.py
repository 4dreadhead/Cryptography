import string as ascii_symbols
from lib.helpers import WindowHelper
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from lib.ui import UiVigenere
from lib.helpers.exceptions import InvalidKey


class VigenereWindow(QMainWindow, UiVigenere, WindowHelper):
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

    def parse_key(self, string):
        user_input_key = self.plainTextEdit_key.toPlainText()
        if len(user_input_key) == 0:
            raise InvalidKey("Key is empty.")
        for symbol in user_input_key:
            if symbol not in (self.latin_low + self.latin_high + self.cyrillic_low + self.cyrillic_high):
                raise InvalidKey("Use only cyrillic or latin symbols.")

        key = list(user_input_key * (len(string) // len(user_input_key) + 1))[:len(string)]
        for alphabet in [self.cyrillic_low, self.cyrillic_high, self.latin_low, self.latin_high]:
            for index, symbol in enumerate(key):
                if symbol in alphabet:
                    key[index] = alphabet.index(symbol)

        return key

    def encrypt(self):
        message = self.plainTextEdit.toPlainText()

        try:
            key = self.parse_key(message)
        except InvalidKey as error:
            self.statusbar.showMessage("Некорректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        self.result = self.transform(message, key, action="encrypt")

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        ciphertext = self.plainTextEdit.toPlainText()

        try:
            key = self.parse_key(ciphertext)
        except InvalidKey as error:
            self.statusbar.showMessage("Некорректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        self.result = self.transform(ciphertext, key, action="decrypt")

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст расшифрован")

    def transform(self, text, key, action=None):
        multiplier = -1 if action == "decrypt" else 1

        result = list(text)
        for alphabet in [self.cyrillic_low, self.cyrillic_high, self.latin_low, self.latin_high]:
            for index, symbol in enumerate(text):
                if symbol in alphabet:
                    result[index] = alphabet[(alphabet.index(symbol) + key[index] * multiplier) % len(alphabet)]

        return "".join(result)
