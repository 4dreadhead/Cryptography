import string as ascii_symbols
from lib.helpers import WindowHelper
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiAtbash


class AtbashWindow(QMainWindow, UiAtbash, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        # Window initialization area
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('lib/media/icon.png'))
        self.pushButton_encrypt.clicked.connect(self.encrypt)
        self.pushButton_paste.clicked.connect(self.paste_from_buffer)
        self.pushButton_clearInput.clicked.connect(self.copy_to_buffer)
        self.pushButton_copy.clicked.connect(self.clear_input)
        self.pushButton_clearOutput.clicked.connect(self.clear_output)
        self.pushButton_exit.clicked.connect(self.close)

        # Method Area
        self.result = ""
        a = ord('а')

        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

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
