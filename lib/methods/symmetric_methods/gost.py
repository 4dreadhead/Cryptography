import time

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon

from lib.ui import UiGost
from lib.helpers import WindowHelper, FileHelper, BlockCiphersFormatHelper, GostKeyGen
from lib.helpers.gost_const import S_TABLES, MOD_CONST_2_DEGREE_32


class GostWindow(QMainWindow, UiGost, WindowHelper, FileHelper, BlockCiphersFormatHelper):
    """
    Window class with method logic
    """
    def __init__(self):
        super().__init__()
        # Window initialization area
        self.setupUi(self)
        self.setWindowIcon(QIcon('lib/media/icon.png'))
        self.pushButton_encrypt.clicked.connect(lambda: self.let_gost_algorithm(action="encrypt"))
        self.pushButton_decrypt.clicked.connect(lambda: self.let_gost_algorithm(action="decrypt"))
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
        self.file_data = None
        self.file_size = None
        self.full_result = None
        self.size = None

    def let_gost_algorithm(self, action=None):
        try:
            start_time = time.time()

            processed_data, preprocessed_data, blocks, control_block, key, previous_block, output_format, cipher_mode =\
                self.prepare_to_process(keygen=GostKeyGen)

            for counter, incoming_block in enumerate(preprocessed_data):
                if control_block and action == "encrypt":
                    result, previous_block = self.process_block(format(self.size, "b").zfill(64),
                                                                key.round_keys, action, previous_block, cipher_mode)
                    processed_data.append(result)
                    control_block = False

                result, previous_block = self.process_block(incoming_block,
                                                            key.round_keys, action, previous_block, cipher_mode)
                processed_data.append(result)

                if control_block and action == "decrypt":
                    self.size = int(processed_data.pop(), 2)
                    control_block = False

                if counter % 256 == 0:
                    self.statusbar.showMessage(
                        f"Прогресс: {round(counter / blocks * 100)}% ({counter}/{blocks} блоков обработано)"
                    )
                    QApplication.processEvents()

            self.show_result(processed_data, output_format, action, start_time)

        except Exception as error:
            self.statusbar.showMessage(f"Произошла ошибка: '{str(error)}'. Проверьте входные данные.")

    def process_block(self, block, key, action, previous_block, cipher_mode):
        result_used_by_mode = None
        match cipher_mode, action:
            case ("ECB", _):
                result_used_by_mode = None
            case ("CFB", "encrypt"):
                block, previous_block = previous_block, block
            case ("CFB", "decrypt"):
                action = "encrypt"
                block, previous_block = previous_block, block
                result_used_by_mode = previous_block
            case _:
                raise ValueError(f"Неизвестная комбинация: {cipher_mode}, #{action}.")

        for round_ in range(32):
            block = self.one_round(block, key[action][round_])

        result = block[32:] + block[:32]

        match cipher_mode:
            case "ECB":
                pass
            case "CFB":
                result = self.xor(block, previous_block, 64)
                result_used_by_mode = result_used_by_mode if result_used_by_mode else result
            case _:
                raise ValueError(f"Неизвестный режим шифрования: {cipher_mode}.")

        return result, result_used_by_mode

    def one_round(self, block, key):
        block_left = block[:32]
        block_right = block[32:]

        amount_mod = format((int(block_right, 2) + int(key, 2)) % MOD_CONST_2_DEGREE_32, "b").zfill(32)
        _4_bit_blocks = [int(amount_mod[i:i + 4], 2) for i in range(0, 32, 4)]
        s_shuffled_blocks = "".join([self.s_shuffle(i, part) for i, part in enumerate(_4_bit_blocks)])

        block_processed = s_shuffled_blocks[11:] + s_shuffled_blocks[:11]

        return block_right + self.xor(block_left, block_processed, 32)

    @staticmethod
    def s_shuffle(index, _4_bit_block):
        return format(S_TABLES[index][_4_bit_block], "b").zfill(4)

    @staticmethod
    def xor(x, y, length):
        x, y = int(x, 2), int(y, 2)
        return bin(x ^ y)[2:].zfill(length)
