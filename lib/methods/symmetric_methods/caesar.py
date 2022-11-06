import string as ascii_symbols
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from lib.ui import UiCaesar
from lib.helpers import WindowHelper


class CaesarWindow(QMainWindow, UiCaesar, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.result = ""
        a = ord('а')

        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

    def encrypt(self):
        key = self.extract_key()
        if not key:
            self.statusbar.showMessage("Некорректное значение ключа")
            return

        string = self.text_input.toPlainText()
        self.result = string
        self.text_output.setText("")

        mixed_alphabets = self.mix_alphabets(key)
        for i in range(4):
            origin = mixed_alphabets[0]
            destination = mixed_alphabets[1]
            mixed_alphabets = mixed_alphabets[2:]

            self.result = self.replace_symbols(self.result, origin, destination)

        self.text_output.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def decrypt(self):
        key = self.extract_key()
        if not key:
            self.statusbar.showMessage("Некорректное значение ключа")
            return

        string = self.text_input.toPlainText()
        self.result = string
        self.text_output.setText("")

        mixed_alphabets = self.mix_alphabets(key)
        for i in range(4):
            origin = mixed_alphabets[1]
            destination = mixed_alphabets[0]
            mixed_alphabets = mixed_alphabets[2:]

            self.result = self.replace_symbols(self.result, origin, destination)

        self.text_output.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован")

    def extract_key(self):
        try:
            return int(self.additional_input_key.toPlainText())
        except ValueError:
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
