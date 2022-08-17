import os

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QApplication

from .custom_byte import CustomByte


class FileHelper:
    """
    Class with methods for reading/writing files
    Must have defined fields described below
    """
    plainTextEdit: QtWidgets.QPlainTextEdit
    textBrowser: QtWidgets.QTextBrowser
    centralwidget: QtWidgets.QWidget
    statusbar: QtWidgets.QStatusBar
    file_size: int
    file_data: bytes or str

    def open_in(self):
        """
        Open file and try to get utf-8 encoded data
        Return flow of the bytes if can't
        :return: [str | generator] read file
        """
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, "Открыть файл:")

        if not file_name:
            return

        self.statusbar.showMessage("Считывание файла...")
        QApplication.processEvents()

        result = self.open_from_file(self.plainTextEdit, file_name)
        if result:
            return

        self.plainTextEdit.setPlainText("")
        self.statusbar.showMessage(f"Файл {file_name} успешно прочитан. Будет произведено побайтовое кодирование.")

        try:
            self.file_data = open(file_name, "rb")
            self.file_size = os.path.getsize(file_name)
            self.textBrowser.setPlainText(f"Размер файла: {self.file_size} байт.")
        except Exception as error:
            self.statusbar.showMessage(f"Ошибка открытия файла: {str(error)}")

    def open_from_file(self, field_to_write, file_name=None):
        """
        Open file as utf-8 encoded data and write it to passed field
        :param field_to_write:  [QtWidgets.QPlainTextEdit] field where data will be writen
        :param file_name:       [str] full name of file (with path)
        :return:                [bool] success or not
        """
        if file_name is None:
            file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, "Открыть файл:")

        if not file_name:
            return

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = file.read()
                field_to_write.setPlainText(data)
                self.statusbar.showMessage(f"Файл {file_name} успешно прочитан.")
            return True

        except Exception as error:
            self.statusbar.showMessage(f"Ошибка открытия / чтения файла: {str(error)}")
            return False

    def save_as_text(self, data):
        """
        Save file as utf-8 encoded data
        :param data: [str] incoming data
        """
        self.save_in_file("w", data)

    def save_as_data(self, data):
        """
        Save file as bytes (write file in any format)
        :param data: [bytearray] incoming data
        """
        self.save_in_file("wb", data)

    def save_in_file(self, mode, data):
        """
        Save data to file
        :param mode:    [str] mode of writing ('w' or 'wb')
        :param data:    [str | bytearray] incoming data
        """
        if not data:
            self.statusbar.showMessage("Нечего сохранять.")
            return

        if mode not in ['w', 'wb']:
            self.statusbar.showMessage("Неверная настройка функции открытия файла. Режим может быть 'w' или 'wb'.")
            return

        file_name, _ = QFileDialog.getSaveFileName(self.centralwidget, "Сохранить в:")
        if not file_name:
            return
        try:
            with open(file_name, mode) as file:
                file.write(data)
                self.statusbar.showMessage(f"Данные успешно сохранены в {file_name}")
        except Exception as error:
            self.statusbar.showMessage(f"Ошибка записи в файл: {str(error)}")

    def file_blocks(self, bytes_amount=8):
        """
        Read bytes from file while it present in passed amount and give them to algorithm
        :param bytes_amount: [int] amount of bytes that will be read in one iteration
        :yield               [bytearray] read bytes in passed amount
        """
        while True:
            try:
                block = self.file_data.read(bytes_amount)
            except Exception as error:
                self.statusbar.showMessage(f"Ошибка чтения файла: {str(error)}.")
                block = None

            if not block:
                break

            yield "".join([CustomByte.load_from_dec(byte).to_bin() for byte in block]).ljust(bytes_amount * 8, "0")

        self.file_data.close()
        self.file_data = None
        self.file_size = None
