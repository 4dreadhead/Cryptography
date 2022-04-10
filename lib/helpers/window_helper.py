import pyperclip
from PyQt5.QtWidgets import QPlainTextEdit, QStatusBar, QTextBrowser


class WindowHelper:
    # Describe variables
    plainTextEdit: QPlainTextEdit
    textBrowser: QTextBrowser
    statusbar: QStatusBar
    result: str

    def clear_input(self):
        """
        This function clears the user input area
        """
        self.plainTextEdit.clear()
        self.statusbar.showMessage("Поле ввода очищено.")

    def clear_output(self):
        """
        This function clears the method result area
        """
        self.textBrowser.clear()
        self.result = ""
        self.statusbar.showMessage("Поле вывода очищено.")

    def copy_to_buffer(self):
        """
        This function copies result to the buffer
        """
        pyperclip.copy(self.result)
        self.statusbar.showMessage("Результат скопирован в буффер обмена.")

    def paste_from_buffer(self):
        """
        This function pastes text from the buffer
        """
        self.plainTextEdit.setPlainText(pyperclip.paste())
        self.statusbar.showMessage("Текст вставлен из буффера обмена.")
