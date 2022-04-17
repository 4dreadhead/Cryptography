import string as ascii_symbols
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiGronsfeld
from lib.helpers import WindowHelper
from lib.helpers.exceptions import InvalidKey


class GronsfeldWindow(QMainWindow, UiGronsfeld, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        super().__init__()
        # Window initialization area
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
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

    def parse_key(self):
        key = self.plainTextEdit_key.toPlainText()
        text_length = len(self.plainTextEdit.toPlainText())
        if text_length == 0:
            return
        if len(key) == 0:
            raise InvalidKey("Key not entered.")

        try:
            key_multiplied = (key * (text_length // len(key) + 1))[:text_length]
            return [int(digit) for digit in key_multiplied]
        except ValueError:
            raise InvalidKey

    def encrypt(self):
        message = self.plainTextEdit.toPlainText()

        try:
            key = self.parse_key()
        except InvalidKey as error:
            self.statusbar.showMessage("Некоректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        self.result = self.transform(message, key, action="encrypt")

        self.statusbar.showMessage("Текст зашифрован.")
        self.textBrowser.setText(self.result)

    def decrypt(self):
        ciphertext = self.plainTextEdit.toPlainText()

        try:
            key = self.parse_key()
        except InvalidKey as error:
            self.statusbar.showMessage("Некоректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        self.result = self.transform(ciphertext, key, action="decrypt")

        self.statusbar.showMessage("Текст расшифрован.")
        self.textBrowser.setText(self.result)

    def transform(self, text, key, action=None):
        multiplier = -1 if action == "decrypt" else 1

        result = list(text)
        for alphabet in [self.cyrillic_low, self.cyrillic_high, self.latin_low, self.latin_high]:
            for index, symbol in enumerate(text):
                if symbol in alphabet:
                    result[index] = alphabet[(alphabet.index(symbol) + key[index] * multiplier) % len(alphabet)]

        return "".join(result)




