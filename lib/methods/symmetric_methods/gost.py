import time

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon

from lib.ui import UiGost
from lib.helpers import WindowHelper, FileHelper, BlockCiphersFormatHelper, GostKeyGen


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

            processed_data, preprocessed_data, blocks, control_block, key, _, output_format, cipher_mode =\
                self.prepare_to_process(keygen=GostKeyGen)

            for counter, incoming_block in enumerate(preprocessed_data):
                pass

            self.show_result(processed_data, output_format, action, start_time)

        except Exception as error:
            self.statusbar.showMessage(f"Произошла ошибка: {str(error)}. Проверьте входные данные")

