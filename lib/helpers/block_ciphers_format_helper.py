import time

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from .custom_byte import CustomByte


class BlockCiphersFormatHelper:
    statusbar: QtWidgets.QStatusBar
    combo_in: QtWidgets.QComboBox
    combo_out: QtWidgets.QComboBox
    combo_key: QtWidgets.QComboBox
    combo_iv: QtWidgets.QComboBox
    combo_mode: QtWidgets.QComboBox
    plainTextEdit_key: QtWidgets.QPlainTextEdit
    plainTextEdit_iv: QtWidgets.QPlainTextEdit
    textBrowser: QtWidgets.QTextBrowser
    plainTextEdit: QtWidgets.QPlainTextEdit
    with_control_bits_box: QtWidgets.QCheckBox
    file_data: str or bytes
    file_size: int
    size: int
    result: str
    full_result: bytearray

    def prepare_to_process(self, keygen, with_iv=True, iv_size=64):
        """
        Read all input data and prepare it to cipher process
        :param keygen:          [class <'${Cipher}KeyGen'>] KeyGen class for method
        :param with_iv:         [bool] say to method read iv if exists
        :param iv_size:         [str] size of IV (length of binary string)
        :return: [tuple]:
            processed_data:     [list] empty list
            preprocessed_data:  [generator] flow of input message(or ciphertext)
            blocks:             [integer] amount of blocks
            control_block:      [bool] need to add or read control block
            key:                [${Cipher}KeyGen] KeyGen instance, generated key(s)
            output_format:      [str] format of output data
            cipher_mode:        [str] cipher mode
        """
        self.statusbar.showMessage("Считывание входных данных...")
        QApplication.processEvents()

        data_format = self.combo_in.currentText()
        output_format = self.combo_out.currentText()
        key_format = self.combo_key.currentText()
        iv_format = self.combo_iv.currentText()
        cipher_mode = self.combo_mode.currentText()
        if with_iv:
            iv_format = self.combo_iv.currentText()

        key = keygen(self.plainTextEdit_key.toPlainText(), key_format, self.plainTextEdit_key)
        if with_iv:
            iv = self.read_iv_from_bytes(self.plainTextEdit_iv.toPlainText(), iv_format,
                                         cipher_mode, self.plainTextEdit_iv, keygen, iv_size=iv_size)
        else:
            iv = None

        self.size = None
        if self.file_data:
            preprocessed_data, blocks = self.file_blocks(), self.file_size // 8
            self.size = self.file_size
        else:
            if len(self.plainTextEdit.toPlainText()) == 0:
                raise ValueError("Нечего шифровать.")
            preprocessed_data, blocks = self.read_bytes_from_data(data_format, self.plainTextEdit.toPlainText())

        processed_data = []
        control_block = self.with_control_bits_box.isChecked()

        return processed_data, preprocessed_data, blocks, control_block, key, iv, output_format, cipher_mode

    def show_result(self, processed_data, output_format, action, start_time):
        """
        Format and show cipher result
        :param processed_data:  [list[str]] result of cipher as binary data
        :param output_format:   [str] format of output data
        :param action:          [str] encrypt or decrypt
        :param start_time:      [float] time when cipher was started
        """
        self.statusbar.showMessage("Форматирование выходных данных...")
        QApplication.processEvents()
        self.full_result = bytearray()

        self.result, out_message = self.format_result(processed_data, output_format, action)
        self.textBrowser.setText(self.result)
        self.statusbar.showMessage(out_message + f" Всего времени затрачено: {time.time() - start_time} сек.")

    def read_bytes_from_data(self, data_format, data, block_size=64):
        """
        Read and format incoming data with the passed format
        :param data_format: [str] format of data (TEXT or HEX or BIN or DEC)
        :param data:        [str] incoming data
        :param block_size:  [int] size of block
        :return: [tuple]:
            tuple[0]:       [generator] flow of incoming data
            tuple[1]:       [int] amount of blocks
        """
        formatted_data = CustomByte.read_bytes(data, data_format)

        self.size = len(formatted_data) // 8

        return (formatted_data[i:i + block_size].ljust(block_size, "0")
                for i in range(0, len(formatted_data), block_size)), len(formatted_data) // block_size + 1

    @staticmethod
    def read_iv_from_bytes(iv, iv_format, cipher_mode, iv_field, keygen, iv_size=64):
        """
        Format initialization vector (IV) from inputs with passed format
        :param iv:          [str] incoming IV from inputs
        :param iv_format:   [str] format of incoming IV (TEXT or HEX or BIN or DEC)
        :param cipher_mode: [str] mode of the cipher
        :param iv_field:    [QtWidgets.QPlainTextEdit] IV input field
        :param keygen:      [class <'${Cipher}KeyGen'>] KeyGen class for method
        :param iv_size:     [str] size of IV (length of binary string)
        :return: result:    [str] formatted IV as binary string
        """
        match cipher_mode:
            case "ECB":
                return None
            case "CBC" | "CFB" | "OFB":
                if not iv:
                    iv = keygen.generate_random_key(iv_format, iv_field, size=iv_size//8)

                result = CustomByte.read_bytes(iv, iv_format)

                if len(result) != iv_size:
                    raise ValueError(f"Неверная длина вектора инициализации (IV):"
                                     f"{len(result)} бит. Ожидалось: {iv_size}.")
                return result
            case _:
                raise ValueError(f"Неизвестный режим шифрования: {cipher_mode}")

    def format_result(self, data, data_format, action):
        """
        Format cipher result with passed parameters
        :param data:        [list[str]] result of cipher as binary data
        :param data_format: [str] format of output data
        :param action:      [str] encrypt or decrypt
        :return: [tuple]:
            result:         [str] formatted result
            message:        [str] message for statusbar
        """
        for block in data:
            self.full_result += self.from_bin_to_bytes(block)

        if action == "decrypt" and self.size:
            self.full_result = self.full_result[:self.size]

        match data_format:
            case "BIN":
                result = " ".join([CustomByte.load_from_dec(byte).to_bin() for byte in self.full_result])
                message = "Результат выведен в двоичном формате."
            case "HEX":
                result = " ".join([CustomByte.load_from_dec(byte).to_hex() for byte in self.full_result])
                message = "Результат выведен в шеснадцатиричном формате."
            case "DEC":
                result = " ".join([str(CustomByte.load_from_dec(byte).to_dec()) for byte in self.full_result])
                message = "Результат выведен в десятеричном формате."
            case "TEXT":
                try:
                    result = self.full_result.decode("utf-8")
                    message = "Результат выведен в UTF-8."
                except UnicodeDecodeError:
                    result = " ".join([CustomByte.load_from_dec(byte).to_hex() for byte in self.full_result])
                    message = "Ошибка декодирования в utf-8. Результат выведен в шеснадцатиричном формате."
            case _:
                raise ValueError("Неверный формат выходных данных.")
        return result, message

    @staticmethod
    def from_bin_to_bytes(block):
        """
        Convert binary string to bytes
        :param block: [str] incoming block
        :return:      [bytearray] converted block
        """
        return bytearray([int(block[i:i + 8], 2) for i in range(0, len(block), 8)])

    def out_message(self, data_format):
        match data_format:
            case "BIN":
                message = "Результат выведен в двоичном формате."
            case "HEX":
                message = "Результат выведен в шеснадцатиричном формате."
            case "DEC":
                message = "Результат выведен в десятеричном формате."
            case "TEXT":
                message = "Результат выведен в UTF-8."
            case _:
                raise ValueError("Неверный формат выходных данных.")
        self.statusbar.showMessage(message)
