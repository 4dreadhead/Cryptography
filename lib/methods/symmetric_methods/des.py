import os
import time

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt6.QtGui import QIcon

from lib.ui import UiDes
from lib.helpers import WindowHelper
from lib.helpers.des_helper import Byte, KeyGen
from lib.helpers.des_const import P_TABLE, IP_TABLES, S_TABLES, E_TABLE

# ----------------------------------------------------------------------------------------------------------
#                                                 TODO
# ----------------------------------------------------------------------------------------------------------
# ✓ Реализовать метод

# ✓ Добавить описание

# ✓ Добавить выбор формата входных / выходных данных

# ✓ Реализовать все виджеты в окне метода

# ✓ Добавить работу с файлами
#       Теперь доступно открытие/сохранение любого из полей окна
#       Так же реализована побайтовая запись результата в файл

# - Добавить новые режимы шифрования

# ✓ Оптимизировать скорость работы алгоритма
#       Ранее при работе с большими файлами требовалось больше времени, иногда скорость доходила до ~50 байт/сек
#       Сейчас скорость обработки не зависит от размера файла и состовляет ~24 кб/сек


class DesWindow(QMainWindow, UiDes, WindowHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        super().__init__()
        # Window initialization area
        self.setupUi(self)
        self.setWindowIcon(QIcon('lib/media/icon.png'))
        self.pushButton_encrypt.clicked.connect(lambda: self.let_des_algorithm(action="encrypt"))
        self.pushButton_decrypt.clicked.connect(lambda: self.let_des_algorithm(action="decrypt"))
        self.pushButton_paste.clicked.connect(self.paste_from_buffer)
        self.pushButton_clearInput.clicked.connect(self.copy_to_buffer)
        self.pushButton_copy.clicked.connect(self.clear_input)
        self.pushButton_clearOutput.clicked.connect(self.clear_output)
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_open_in.clicked.connect(self.open_in)
        self.pushButton_save_in.clicked.connect(lambda: self.save_as_text(self.plainTextEdit.toPlainText()))
        self.pushButton_save_out.clicked.connect(lambda: self.save_as_text(self.result))
        self.pushButton_write_out.clicked.connect(lambda: self.save_as_data(self.full_result))
        self.pushButton_save_iv.clicked.connect(lambda: self.save_as_text(self.plainTextEdit_iv.toPlainText()))
        self.pushButton_save_key.clicked.connect(lambda: self.save_as_text(self.plainTextEdit_key.toPlainText()))
        self.pushButton_open_iv.clicked.connect(lambda: self.open_from_file(self.plainTextEdit_iv))
        self.pushButton_open_key.clicked.connect(lambda: self.open_from_file(self.plainTextEdit_key))

        self.file_data = None
        self.file_size = None
        self.result = None
        self.full_result = None
        self.size = None

    # ----------------------------------------------------------------------------------------------------------
    #                            Основной поток функции шифрования / расшифрования
    # ----------------------------------------------------------------------------------------------------------

    def let_des_algorithm(self, action="encrypt"):
        try:
            start_time = time.time()
            data_format = self.combo_in.currentText()
            output_format = self.combo_out.currentText()
            key_format = self.combo_key.currentText()

            key = KeyGen(self.plainTextEdit_key.toPlainText(), key_format)

            self.statusbar.showMessage("Считывание входных данных...")
            QApplication.processEvents()

            if self.file_data:
                preprocessed_data, blocks = self.file_blocks(), self.file_size // 8
                self.size = self.file_size
            else:
                if len(self.plainTextEdit.toPlainText()) == 0:
                    raise ValueError("Given empty text.")
                preprocessed_data, blocks = self.read_bytes_from_data(data_format, self.plainTextEdit.toPlainText())

            processed_data = []
            counter = 0

            first_iteration = True

            for incoming_block in preprocessed_data:
                if first_iteration and action == "encrypt":
                    processed_data.append(
                        self.process_block(
                            bin(self.size).lstrip('0b').zfill(64),
                            action,
                            key,
                            counter,
                            blocks
                        )
                    )
                    first_iteration = False

                processed_data.append(self.process_block(incoming_block, action, key, counter, blocks))
                counter += 1

                if first_iteration and action == "decrypt":
                    self.size = int(processed_data.pop(), 2)
                    first_iteration = False

            self.statusbar.showMessage("Форматирование выходных данных...")
            QApplication.processEvents()
            self.full_result = bytearray()

            self.result, out_message = self.format_result(processed_data, output_format, action)
            self.textBrowser.setText(self.result)
            self.statusbar.showMessage(out_message + f" Всего времени затрачено: {time.time() - start_time} сек.")

        except Exception as error:
            self.textBrowser.setText(str(error))

    # ----------------------------------------------------------------------------------------------------------
    #                               Форматирование входных и выходных данных
    # ----------------------------------------------------------------------------------------------------------

    def read_bytes_from_data(self, data_format, data):
        match data_format:
            case "BIN":
                formatted_data = data.replace(" ", "").replace("\n", "")
            case "HEX":
                formatted_data = data.replace(" ", "").replace("\n", "")
                formatted_data = "".join([
                    Byte.load_from_hex(
                        formatted_data[2*i:2*(i+1)]
                    ).to_bin() for i in range(len(formatted_data) // 2)
                ])
            case "DEC":
                preparing_data = data.split(" ")
                formatted_data = []
                for byte in preparing_data:
                    if not 0 <= int(byte) < 256:
                        raise ValueError(f"Incorrect byte value: {byte}.")
                    formatted_data.append(Byte.load_from_dec(byte).to_bin())
                formatted_data = "".join(formatted_data)

            case "TEXT":
                formatted_data = "".join(
                    [
                        Byte.load_from_dec(byte).to_bin() for byte in bytearray(
                            data, "utf-8"
                        )
                    ]
                )
            case _:
                raise ValueError("Unknown data type")

        self.size = len(formatted_data) // 8

        if len(formatted_data) % 64 != 0:
            formatted_data += "0" * (64 - len(formatted_data) % 64)

        return (formatted_data[i:i+64] for i in range(0, len(formatted_data), 64)), len(formatted_data) // 64

    def format_result(self, data, data_format, action):
        for block in data:
            self.full_result += self.from_bin_to_bytes(block)

        if action == "decrypt":
            self.full_result = self.full_result[:self.size]

        showed_bytes = self.full_result

        match data_format:
            case "BIN":
                result = " ".join([Byte.load_from_dec(byte).to_bin() for byte in showed_bytes])
                message = "Результат выведен в двоичном формате."
            case "HEX":
                result = " ".join([Byte.load_from_dec(byte).to_hex() for byte in showed_bytes])
                message = "Результат выведен в шеснадцатиричном формате."
            case "DEC":
                result = " ".join([str(Byte.load_from_dec(byte).to_dec()) for byte in showed_bytes])
                message = "Результат выведен в десятеричном формате."
            case "TEXT":
                try:
                    result = showed_bytes.decode("utf-8")
                    message = "Результат выведен в UTF-8."
                except UnicodeDecodeError:
                    result = " ".join([Byte.load_from_dec(byte).to_hex() for byte in showed_bytes])
                    message = "Ошибка декодирования в utf-8. Результат выведен в шеснадцатиричном формате."
            case _:
                raise ValueError("Unknown output format.")
        return result, message

    @staticmethod
    def from_bin_to_bytes(block):
        return bytearray([int(block[i:i+8], 2) for i in range(0, len(block), 8)])

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
                raise ValueError("Unknown output format.")
        self.statusbar.showMessage(message)

    # ----------------------------------------------------------------------------------------------------------
    #                                           Методы логики шифра
    # ----------------------------------------------------------------------------------------------------------

    def process_block(self, incoming_block, action, key, counter, blocks):
        block = self.message_shuffle(incoming_block, "START")

        if action == "encrypt":
            rounds = range(1, 17)
        elif action == "decrypt":
            rounds = range(16, 0, -1)
        else:
            raise ValueError(f"Unknown action: {action}. Expected: 'encrypt' or 'decrypt'")

        if action == "decrypt":
            block = block[32:64] + block[:32]

        for round_ in rounds:
            block = self.one_round(block, key.round_keys[round_], action)

        if action == "encrypt":
            block = block[32:64] + block[:32]

        result = self.message_shuffle(block, "END")

        if counter % 256 == 0:
            self.statusbar.showMessage(
                f"Прогресс: {round(counter / blocks * 100)}% ({counter}/{blocks} блоков обработано)"
            )
            QApplication.processEvents()

        return result

    @staticmethod
    def message_shuffle(bit_message, action):
        return "".join([bit_message[i - 1] for i in IP_TABLES[action]])

    @staticmethod
    def widen_block(block):
        return "".join([block[i - 1] for i in E_TABLE])

    @staticmethod
    def block_p_shuffle(block):
        return "".join([block[i - 1] for i in P_TABLE])

    @staticmethod
    def xor(x, y, length):
        x, y = int(x, 2), int(y, 2)
        return bin(x ^ y)[2:].zfill(length)

    def process_message_block(self, block, key):
        wide_block = self.widen_block(block)
        wide_block = self.xor(wide_block, key, 48)

        _6bit_groups = [wide_block[6*i:6*(i+1)] for i in range(8)]
        result_block = "".join(
            [self.process_6bit_group(group, s_table) for group, s_table in zip(_6bit_groups, S_TABLES)]
        )
        return self.block_p_shuffle(result_block)

    @staticmethod
    def process_6bit_group(_6bit_group, s_table):
        row = int(_6bit_group[0] + _6bit_group[-1], 2)
        column = int(_6bit_group[1:-1], 2)
        return bin(s_table[row][column])[2:].zfill(4)

    def one_round(self, block, round_key, action):
        first_block = block[:32]
        second_block = block[32:64]

        if action == "encrypt":
            processed_block = self.process_message_block(second_block, round_key)
            return "".join([second_block, self.xor(first_block, processed_block, 32)])
        else:
            processed_block = self.process_message_block(first_block, round_key)
            return "".join([self.xor(processed_block, second_block, 32), first_block])

    # ----------------------------------------------------------------------------------------------------------
    #                                          Работа с файлами
    # ----------------------------------------------------------------------------------------------------------

    def open_in(self):
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, "Открыть файл:")

        if not file_name:
            return

        self.statusbar.showMessage("Считывание файла...")
        QApplication.processEvents()

        result = self.open_from_file(self.plainTextEdit, file_name)
        if result:
            return

        self.plainTextEdit.setPlainText("")
        self.statusbar.showMessage("Не удалось открыть файл как текст, будет произведено побайтовое считывание.")

        try:
            self.file_data = open(file_name, "rb")
            self.file_size = os.path.getsize(file_name)
            self.textBrowser.setPlainText(f"Размер файла: {self.file_size} байт.")
        except Exception as error:
            self.statusbar.showMessage(f"Ошибка открытия файла: {str(error)}")

    def open_from_file(self, field_to_write, file_name=None):
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
        self.save_in_file("w", data)

    def save_as_data(self, data):
        self.save_in_file("wb", data)

    def save_in_file(self, mode, data):
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

    def file_blocks(self):
        while True:
            try:
                block = self.file_data.read(8)
            except Exception as error:
                self.statusbar.showMessage(f"Ошибка чтения файла: {str(error)}.")
                block = None

            if not block:
                break

            yield "".join([Byte.load_from_dec(byte).to_bin() for byte in block]).ljust(64, "0")

        self.file_data.close()
        self.file_data = None
        self.file_size = None
