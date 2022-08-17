import time

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon

from lib.ui import UiDes
from lib.helpers import WindowHelper, FileHelper, DesKeyGen, CustomByte, BlockCiphersFormatHelper
from lib.helpers.des_const import P_TABLE, IP_TABLES, S_TABLES, E_TABLE


class DesWindow(QMainWindow, UiDes, WindowHelper, FileHelper, BlockCiphersFormatHelper):
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

        self.result = ""
        self.full_result = None
        self.size = None
        self.file_size = None
        self.file_data = None

    def let_des_algorithm(self, action="encrypt"):
        try:
            start_time = time.time()
            processed_data, preprocessed_data, blocks, control_block, key, previous_block, output_format, cipher_mode =\
                self.prepare_to_process(keygen=DesKeyGen)

            for counter, incoming_block in enumerate(preprocessed_data):
                if control_block and action == "encrypt":
                    result, previous_block = self.process_block(format(self.size, "b").zfill(64), previous_block,
                                                                action, key, counter, blocks, cipher_mode)
                    processed_data.append(result)
                    control_block = False

                result, previous_block = self.process_block(incoming_block, previous_block,
                                                            action, key, counter, blocks, cipher_mode)
                processed_data.append(result)

                if control_block and action == "decrypt":
                    self.size = int(processed_data.pop(), 2)
                    control_block = False

            self.show_result(processed_data, output_format, action, start_time)

        except Exception as error:
            self.statusbar.showMessage(f"Произошла ошибка: '{str(error)}'. Проверьте входные данные.")

    def process_block(self, incoming_block, previous_block, action, key, counter, blocks, cipher_mode):
        result_used_by_mode = None

        match (cipher_mode, action):
            case ("ECB", _):
                pass

            case ("CBC", "encrypt"):
                incoming_block = self.xor(incoming_block, previous_block, 64)

            case ("CBC", "decrypt"):
                result_used_by_mode = incoming_block

            case ("CFB", "encrypt"):
                action = "encrypt"
                incoming_block, previous_block = previous_block, incoming_block

            case ("CFB", "decrypt"):
                action = "encrypt"
                incoming_block, previous_block = previous_block, incoming_block
                result_used_by_mode = previous_block

            case ("OFB", _):
                action = "encrypt"
                incoming_block, previous_block = previous_block, incoming_block
            case _:
                raise ValueError(f"Необработанная комбинация: {cipher_mode}, {action}")

        block = self.message_shuffle(incoming_block, "START")

        match action:
            case "encrypt":
                for round_ in range(1, 17):
                    block = self.one_round(block, key.round_keys[round_], action)
                block = block[32:64] + block[:32]

            case "decrypt":
                block = block[32:64] + block[:32]
                for round_ in range(16, 0, -1):
                    block = self.one_round(block, key.round_keys[round_], action)

            case _:
                raise ValueError(f"Неизвестное действие: {cipher_mode}, {action}")

        result = self.message_shuffle(block, "END")

        match (cipher_mode, action):
            case ("ECB", _):
                pass

            case ("CBC", "encrypt"):
                result_used_by_mode = result

            case ("CBC", "decrypt"):
                result = self.xor(result, previous_block, 64)

            case ("CFB", _):
                result = self.xor(result, previous_block, 64)
                result_used_by_mode = result_used_by_mode if result_used_by_mode else result

            case ("OFB", _):
                result_used_by_mode = result
                result = self.xor(result, previous_block, 64)

            case _:
                raise ValueError(f"Необработанная комбинация: {cipher_mode}, {action}")

        if counter % 256 == 0:
            self.statusbar.showMessage(
                f"Прогресс: {round(counter / blocks * 100)}% ({counter}/{blocks} блоков обработано)"
            )
            QApplication.processEvents()

        return result, result_used_by_mode

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
        return format(s_table[row][column], "b").zfill(4)

    def one_round(self, block, round_key, action):
        first_block = block[:32]
        second_block = block[32:64]

        match action:
            case "encrypt":
                processed_block = self.process_message_block(second_block, round_key)
                return "".join([second_block, self.xor(first_block, processed_block, 32)])
            case "decrypt":
                processed_block = self.process_message_block(first_block, round_key)
                return "".join([self.xor(processed_block, second_block, 32), first_block])
            case _:
                raise ValueError(f"Неизвестное действие: {action}")
