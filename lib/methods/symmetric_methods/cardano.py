import re
import random
import string as ascii_symbols
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from lib.ui import UiCardano
from lib.helpers import WindowHelper
from lib.helpers.exceptions import InvalidKey


class CardanoWindow(QMainWindow, UiCardano, WindowHelper):
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
        self.pushButton_generate_key.clicked.connect(self.generate_grille)

        # Method area
        self.result = ""
        a = ord('а')

        self.cyrillic_low = "".join(
            [chr(i) for i in range(a, a + 6)] +
            [chr(a + 33)] +
            [chr(i) for i in range(a + 6, a + 32)]
        )
        self.cyrillic_high = "".join([i.swapcase() for i in self.cyrillic_low])
        self.latin_low = ascii_symbols.printable[10:36]
        self.latin_high = ascii_symbols.printable[36:62]

    def parse_keys(self):
        keys_pattern = r"\(\d+(?:,\d+)*\)"
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
                raise InvalidKey("Wrong Cardano Grille size.")
            if parsed_keys[size//2][size//2] == 1:
                raise InvalidKey(f"Wrong Cardano Grille: check cell value at {size//2, size//2}.")

        for i in range(size//2):
            for j in range(size//2):
                if (
                        parsed_keys[i][j] +
                        parsed_keys[size-1 - i][size-1 - j] +
                        parsed_keys[j][size-1 - i] +
                        parsed_keys[size-1 - j][i]
                ) not in allowed_values:
                    raise InvalidKey(f"Wrong Cardano Grille: check cell value at {i, j}.")
            if size % 2 != 0:
                if (
                        parsed_keys[i][size//2] +
                        parsed_keys[size//2][i] +
                        parsed_keys[size-1 - i][size//2] +
                        parsed_keys[size//2][size-1 - i]
                ) > 1:
                    raise InvalidKey(f"Wrong Cardano Grille: check cell value at {i, size//2}.")

        return parsed_keys, size

    def parse_size(self):
        size = int(self.plainTextEdit_key_size.toPlainText())
        if size <= 1 or size > 4096:
            raise ValueError
        return size

    def generate_grille(self):
        try:
            size = self.parse_size()
        except ValueError:
            self.statusbar.showMessage("Некорректная размерность решетки.")
            return

        grille = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size//2):
            for j in range(size//2):
                box = [0 for _ in range(4)]
                box[random.randint(0, 3)] = 1
                if box[0] == 1:
                    grille[i][j] = 1
                elif box[1] == 1:
                    grille[j][size-1 - i] = 1
                elif box[2] == 1:
                    grille[size-1 - i][size-1 - j] = 1
                elif box[3] == 1:
                    grille[size-1 - j][i] = 1

            if size % 2 == 1:
                column = [0 for _ in range(size//2)]
                column[random.randint(0, size//2 - 1)] = 1
                if column[0] == 1:
                    grille[i][size//2] = 1
                elif column[1] == 1:
                    grille[size//2][size-1 - i] = 1
                elif column[2] == 1:
                    grille[size-1 - i][size//2] = 1
                elif column[3] == 1:
                    grille[size//2][i] = 1

        grille_output = ""
        for row in grille:
            grille_output += "(" + ",".join(list(map(str, row))) + ")\n"

        self.plainTextEdit_key.setPlainText(grille_output[:-1])
        self.statusbar.showMessage("Решетка сгенерирована.")

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
