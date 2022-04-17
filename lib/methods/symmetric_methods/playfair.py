import string as ascii_symbols
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiPlayfair
from lib.helpers import WindowHelper
from lib.helpers.exceptions import InvalidKey


class PlayfairWindow(QMainWindow, UiPlayfair, WindowHelper):
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

        self.cyrillic = [chr(i).upper() for i in range(a, a + 32)]
        self.latin = list(ascii_symbols.printable[36:62].replace("J", ""))

    def parse_key(self):
        # Reading entered key
        user_input_key = self.plainTextEdit_key.toPlainText() \
            .replace(" ", "") \
            .replace("J", "I") \
            .replace("j", "i") \
            .replace("Ё", "Е") \
            .replace("ё", "е")

        # Check for not entered key
        if len(user_input_key) == 0:
            raise InvalidKey("Key not entered.")

        # Parsing unique symbols
        key = []
        for symbol in user_input_key:
            if symbol.upper() not in key:
                key.append(symbol.upper())

        # Check alphabet
        if key[0] in self.cyrillic:
            alphabet = self.cyrillic
        elif key[0] in self.latin:
            alphabet = self.latin
        else:
            raise InvalidKey

        # Check for all symbols from same alphabet
        for symbol in key:
            if symbol not in alphabet:
                raise InvalidKey("Key must contain symbols from the same alphabet.")

        # Generate key matrix
        key = key + [symbol for symbol in alphabet if symbol not in key]
        if alphabet == self.cyrillic:
            final_key = [["" for _ in range(4)] for _ in range(8)]
            for i in range(len(final_key)):
                for j in range(len(final_key[i])):
                    final_key[i][j] = key[0]
                    key = key[1:]
        else:
            final_key = [["" for _ in range(5)] for _ in range(5)]
            for i in range(len(final_key)):
                for j in range(len(final_key[i])):
                    final_key[i][j] = key[0]
                    key = key[1:]

        return final_key, alphabet

    def encrypt(self):
        # Parsing key
        try:
            key, alphabet = self.parse_key()
        except InvalidKey as error:
            self.statusbar.showMessage("Некоректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        # Parsing message
        message = self.plainTextEdit.toPlainText() \
            .replace("J", "I") \
            .replace("j", "i") \
            .replace("Ё", "Е") \
            .replace("ё", "е")

        almost_ready_text = ""
        for symbol in message:
            if symbol.upper() in alphabet:
                almost_ready_text += symbol.upper()

        # Encrypting
        symbol_to_add = "X" if alphabet == self.latin else "Ъ"
        while True:
            need_to_repeat = False
            for index in range(0, len(almost_ready_text) - len(almost_ready_text) % 2, 2):
                if almost_ready_text[index] == almost_ready_text[index + 1]:
                    almost_ready_text = almost_ready_text[:index + 1] + symbol_to_add + almost_ready_text[index + 1:]
                    need_to_repeat = True
                    break
            if need_to_repeat:
                continue
            if len(almost_ready_text) % 2 == 1:
                almost_ready_text += symbol_to_add
            break
        message_pairs = [almost_ready_text[index:index + 2] for index in range(0, len(almost_ready_text), 2)]

        result = ""
        for pair in message_pairs:
            for encoded_pair in self.en_de_coder(pair, key, action="encrypt"):
                if encoded_pair:
                    result += encoded_pair
                    break

        # Setting result
        self.result = result
        self.statusbar.showMessage("Текст зашифрован.")
        self.textBrowser.setText(self.result)

    def decrypt(self):
        # Parsing key
        try:
            key, alphabet = self.parse_key()
        except InvalidKey as error:
            self.statusbar.showMessage("Некоректное значение ключа.")
            self.textBrowser.setText(str(error))
            return

        # Parsing ciphertext
        ciphertext = self.plainTextEdit.toPlainText()

        almost_ready_text = ""
        for symbol in ciphertext:
            if symbol.upper() in alphabet:
                almost_ready_text += symbol.upper()
        if len(almost_ready_text) % 2 == 1:
            self.statusbar.showMessage("Некорректные входные данные.")
            self.textBrowser.setText("")
            return

        # Decrypting
        message_pairs = [almost_ready_text[index:index + 2] for index in range(0, len(almost_ready_text), 2)]

        result = ""
        for pair in message_pairs:
            for encoded_pair in self.en_de_coder(pair, key, action="decrypt"):
                if encoded_pair:
                    result += encoded_pair
                    break

        # Setting result
        self.result = result.replace("X", "").replace("Ъ", "")
        self.statusbar.showMessage("Текст расшифрован.")
        self.textBrowser.setText(self.result)

    @staticmethod
    def en_de_coder(pair, key, action=None):
        result = None
        addendum = -1 if action == "decrypt" else 1

        # Check if pair in one line
        for line in key:
            if pair[0] in line and pair[1] in line:
                result = line[(line.index(pair[0]) + addendum) % len(line)] +\
                         line[(line.index(pair[1]) + addendum) % len(line)]
                break
        yield result

        # Check if pair in one column
        for column in zip(*key):
            if pair[0] in column and pair[1] in column:
                result = column[(column.index(pair[0]) + addendum) % len(column)] +\
                         column[(column.index(pair[1]) + addendum) % len(column)]
                break
        yield result

        # Replacing by rectangle coordinates
        first_line_index, first_column_index, second_line_index, second_column_index = 0, 0, 0, 0
        for line in key:
            if pair[0] in line:
                first_line_index = key.index(line)
                first_column_index = line.index(pair[0])
            if pair[1] in line:
                second_line_index = key.index(line)
                second_column_index = line.index(pair[1])
        result = key[first_line_index][second_column_index] + key[second_line_index][first_column_index]
        yield result
