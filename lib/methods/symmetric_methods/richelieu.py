import re
import string as ascii_symbols
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiRichelieu
from lib.helpers import WindowHelper
from lib.helpers.exceptions import InvalidKey


class RichelieuWindow(QMainWindow, UiRichelieu, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        # Window initialize area
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
        a = ord('а')
        self.cyrillic_low = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        self.cyrillic_high = [i.swapcase() for i in self.cyrillic_low]
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

    def parse_keys(self):
        keys_pattern = r"\(\d+(?:,\d+)*\)"
        parsed_keys = []

        user_input_key = self.plainTextEdit_key.toPlainText()
        received_keys_string = re.findall(keys_pattern, user_input_key)

        # Check for valid user input string format
        if user_input_key != "".join(received_keys_string):
            raise InvalidKey("Unexpended key format, see tips label.")

        # Convert keys to int
        for keys_block in received_keys_string:
            parsed_keys.append(list(map(int, keys_block[1:-1].split(","))))

        # Check for valid keys values
        size = 0
        for keys in parsed_keys:
            if len(keys) != len(set(keys)):
                raise InvalidKey(f"Wrong key value at {keys}, see tips label.")
            for key in keys:
                if key not in range(1, len(keys) + 1):
                    raise InvalidKey(f"Wrong key value at {keys}, see tips label.")
            size += len(keys)

        return parsed_keys, size

    def encrypt(self):
        try:
            keys_list, key_size = self.parse_keys()
            string = self.plainTextEdit.toPlainText()

            encrypted_string_parts = []

            if key_size > len(string):
                raise InvalidKey("Too short string / too long key value.")

            for keys in keys_list:
                part_of_string = string[:len(keys)]
                string = string[len(keys):]

                encrypted_string_part = ""
                for key in keys:
                    encrypted_string_part += part_of_string[key - 1]

                encrypted_string_parts.append(encrypted_string_part)

            self.result = "".join(encrypted_string_parts) + string

            self.textBrowser.setText(self.result)
            self.statusbar.showMessage("Текст зашифрован")

        except InvalidKey as error:
            self.textBrowser.setText(str(error))
            self.statusbar.showMessage("Неверные входные данные, попробуйте снова.")
        finally:
            pass

    def decrypt(self):
        try:
            keys_list, key_size = self.parse_keys()
            string = self.plainTextEdit.toPlainText()

            decrypted_string_parts = []

            if key_size > len(string):
                raise InvalidKey("Wrong key value: Too short string / too long key.")

            for keys in keys_list:
                decrypted_part_list = ["" for _ in range(len(keys))]
                part_of_string = string[:len(keys)]
                string = string[len(keys):]

                for index, key in enumerate(keys):
                    decrypted_part_list[key-1] += part_of_string[index]

                decrypted_string_parts.append("".join(decrypted_part_list))

            self.result = "".join(decrypted_string_parts) + string

            self.textBrowser.setText(self.result)
            self.statusbar.showMessage("Текст расшифрован")

        except InvalidKey as error:
            self.textBrowser.setText(str(error))
            self.statusbar.showMessage("Неверные входные данные, попробуйте снова.")
        finally:
            pass
