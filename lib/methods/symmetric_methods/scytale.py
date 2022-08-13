from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from lib.ui import UiScytale
from lib.helpers import WindowHelper


class ScytaleWindow(QMainWindow, UiScytale, WindowHelper):
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
        self.result = ""

    def encrypt(self):
        string = self.plainTextEdit.toPlainText()
        self.textBrowser.setText("")

        table_size = self.set_table_size(string, encrypt=True)
        string = string.ljust(table_size["row_count"] * table_size["row_size"], "⋆")
        self.result = self.transform(string, table_size)

        self.textBrowser.setText(self.result)
        self.statusbar.showMessage("Текст зашифрован.")

    def decrypt(self):
        string = self.plainTextEdit.toPlainText()
        self.textBrowser.setText("")

        table_size = self.set_table_size(string, decrypt=True)
        string = string.ljust(table_size["row_count"] * table_size["row_size"], "⋆")
        self.result = self.transform(string, table_size)

        self.textBrowser.setText(self.result.replace("⋆", ""))
        self.statusbar.showMessage("Текст расшифрован.")

    @staticmethod
    def set_table_size(incoming_string, encrypt=False, decrypt=False):
        table_size = {}
        row_size = len(incoming_string) ** (1 / 2)
        if row_size % 1 == 0:
            table_size = {"row_size": int(row_size), "row_count": int(row_size)}
        else:
            row_size = int(row_size) + 1
            row_count = row_size if len(incoming_string) > row_size * (row_size - 1) else row_size - 1
            if encrypt:
                table_size = {"row_size": row_size, "row_count": row_count}
            if decrypt:
                table_size = {"row_size": row_count, "row_count": row_size}
        return table_size

    @staticmethod
    def transform(incoming_string, table_size):
        table = []
        for i in range(table_size["row_count"]):
            table.append(incoming_string[:table_size["row_size"]])
            incoming_string = incoming_string[table_size["row_size"]:]

        result_table = [["" for _ in range(table_size["row_count"])] for _ in range(table_size["row_size"])]
        for i in range(table_size["row_count"]):
            for j in range(table_size["row_size"]):
                result_table[j][i] = table[i][j]

        result = ""
        for row in result_table:
            result += "".join(row)
        return result
