from PyQt6 import QtCore, QtGui, QtWidgets
from lib.helpers import UiHelper


class UiGost(object):
    """
    UI class of method
    """
    def setupUi(self, Gost):
        Gost.setObjectName("Gost")
        Gost.resize(1280, 720)
        Gost.setMinimumSize(QtCore.QSize(1280, 720))
        Gost.setMaximumSize(QtCore.QSize(1280, 720))
        Gost.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Gost)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Gost_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Gost_gif.setGeometry(QtCore.QRect(30, 30, 800, 120))
        self.label_Gost_gif.setObjectName("label_gost_gif")
        gif = QtGui.QMovie("lib/media/gost.gif")
        self.label_Gost_gif.setMovie(gif)
        gif.start()

        font = UiHelper.set_font(size=9)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(850, 30, 400, 240))
        self.label_info.setFont(font)
        self.label_info.setStyleSheet(UiHelper.text_area_style())
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")

        font = UiHelper.set_font(size=10, bold=True, italic=True)

        self.label_info_key = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key.setGeometry(QtCore.QRect(630, 200, 200, 30))
        self.label_info_key.setFont(font)
        self.label_info_key.setStyleSheet(UiHelper.text_area_style())
        self.label_info_key.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_key.setObjectName("label_info_key")

        self.label_info_iv = QtWidgets.QLabel(self.centralwidget)
        self.label_info_iv.setGeometry(QtCore.QRect(630, 240, 200, 30))
        self.label_info_iv.setFont(font)
        self.label_info_iv.setStyleSheet(UiHelper.text_area_style())
        self.label_info_iv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_iv.setObjectName("label_info_iv")

        self.label_info_key_format = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key_format.setGeometry(QtCore.QRect(30, 290, 220, 30))
        self.label_info_key_format.setFont(font)
        self.label_info_key_format.setStyleSheet(UiHelper.text_area_style())
        self.label_info_key_format.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_key_format.setObjectName("label_info_key_format")

        self.label_info_in = QtWidgets.QLabel(self.centralwidget)
        self.label_info_in.setGeometry(QtCore.QRect(530, 290, 220, 30))
        self.label_info_in.setFont(font)
        self.label_info_in.setStyleSheet(UiHelper.text_area_style())
        self.label_info_in.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_in.setObjectName("label_info_in")

        self.label_info_out = QtWidgets.QLabel(self.centralwidget)
        self.label_info_out.setGeometry(QtCore.QRect(780, 290, 220, 30))
        self.label_info_out.setFont(font)
        self.label_info_out.setStyleSheet(UiHelper.text_area_style())
        self.label_info_out.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_out.setObjectName("label_info_out")

        self.label_info_combo_iv = QtWidgets.QLabel(self.centralwidget)
        self.label_info_combo_iv.setGeometry(QtCore.QRect(280, 290, 220, 30))
        self.label_info_combo_iv.setFont(font)
        self.label_info_combo_iv.setStyleSheet(UiHelper.text_area_style())
        self.label_info_combo_iv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_combo_iv.setObjectName("label_info_combo_iv")

        self.combo_key = QtWidgets.QComboBox(self.centralwidget)
        self.combo_key.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_key.setFont(font)
        self.combo_key.setStyleSheet(UiHelper.combo_box_style())
        self.combo_key.setGeometry(QtCore.QRect(30, 320, 220, 30))

        self.combo_iv = QtWidgets.QComboBox(self.centralwidget)
        self.combo_iv.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_iv.setFont(font)
        self.combo_iv.setStyleSheet(UiHelper.combo_box_style())
        self.combo_iv.setGeometry(QtCore.QRect(280, 320, 220, 30))

        self.combo_in = QtWidgets.QComboBox(self.centralwidget)
        self.combo_in.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_in.setFont(font)
        self.combo_in.setStyleSheet(UiHelper.combo_box_style())
        self.combo_in.setGeometry(QtCore.QRect(530, 320, 220, 30))

        self.combo_out = QtWidgets.QComboBox(self.centralwidget)
        self.combo_out.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_out.setFont(font)
        self.combo_out.setStyleSheet(UiHelper.combo_box_style())
        self.combo_out.setGeometry(QtCore.QRect(780, 320, 220, 30))

        self.label_info_mode = QtWidgets.QLabel(self.centralwidget)
        self.label_info_mode.setGeometry(QtCore.QRect(1030, 290, 220, 30))
        self.label_info_mode.setFont(font)
        self.label_info_mode.setStyleSheet(UiHelper.text_area_style())
        self.label_info_mode.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_mode.setObjectName("label_info_mode")

        self.combo_mode = QtWidgets.QComboBox(self.centralwidget)
        self.combo_mode.addItems(["ECB", "CFB"])
        self.combo_mode.setFont(font)
        self.combo_mode.setStyleSheet(UiHelper.combo_box_style())
        self.combo_mode.setGeometry(QtCore.QRect(1030, 320, 220, 30))

        self.with_control_bits_box = QtWidgets.QCheckBox(self.centralwidget)
        self.with_control_bits_box.setGeometry(QtCore.QRect(450, 650, 30, 30))
        self.with_control_bits_box.setFont(font)
        self.with_control_bits_box.setStyleSheet(UiHelper.trash_box_style())
        self.with_control_bits_box.setObjectName("with_control_bits_box")

        self.label_info_control_bits = QtWidgets.QLabel(self.centralwidget)
        self.label_info_control_bits.setGeometry(QtCore.QRect(240, 650, 200, 30))
        self.label_info_control_bits.setFont(font)
        self.label_info_control_bits.setStyleSheet(UiHelper.text_area_style())
        self.label_info_control_bits.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_control_bits.setObjectName("label_info_mode")

        font = UiHelper.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 370, 1220, 110))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_key.setGeometry(QtCore.QRect(30, 200, 590, 30))
        self.plainTextEdit_key.setFont(font)
        self.plainTextEdit_key.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit_key.setObjectName("plainTextEdit")

        self.plainTextEdit_iv = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_iv.setGeometry(QtCore.QRect(30, 240, 590, 30))
        self.plainTextEdit_iv.setFont(font)
        self.plainTextEdit_iv.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit_iv.setObjectName("plainTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 530, 1220, 110))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(UiHelper.text_area_style())
        self.textBrowser.setObjectName("textBrowser")

        font = UiHelper.set_font("Droid Sans Mono", size=10, bold=True)

        self.pushButton_open_key = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_key.setGeometry(QtCore.QRect(30, 160, 170, 30))
        self.pushButton_open_key.setFont(font)
        self.pushButton_open_key.setObjectName("pushButton_encrypt")
        self.pushButton_open_key.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_open_iv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_iv.setGeometry(QtCore.QRect(480, 160, 170, 30))
        self.pushButton_open_iv.setFont(font)
        self.pushButton_open_iv.setObjectName("pushButton_encrypt")
        self.pushButton_open_iv.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_open_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_in.setGeometry(QtCore.QRect(490, 490, 200, 30))
        self.pushButton_open_in.setFont(font)
        self.pushButton_open_in.setObjectName("pushButton_encrypt")
        self.pushButton_open_in.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_save_key = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_key.setGeometry(QtCore.QRect(210, 160, 170, 30))
        self.pushButton_save_key.setFont(font)
        self.pushButton_save_key.setObjectName("pushButton_encrypt")
        self.pushButton_save_key.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_save_iv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_iv.setGeometry(QtCore.QRect(660, 160, 170, 30))
        self.pushButton_save_iv.setFont(font)
        self.pushButton_save_iv.setObjectName("pushButton_encrypt")
        self.pushButton_save_iv.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_save_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_in.setGeometry(QtCore.QRect(700, 490, 200, 30))
        self.pushButton_save_in.setFont(font)
        self.pushButton_save_in.setObjectName("pushButton_encrypt")
        self.pushButton_save_in.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_write_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_write_out.setGeometry(QtCore.QRect(490, 650, 200, 30))
        self.pushButton_write_out.setFont(font)
        self.pushButton_write_out.setObjectName("pushButton_encrypt")
        self.pushButton_write_out.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_save_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_out.setGeometry(QtCore.QRect(700, 650, 200, 30))
        self.pushButton_save_out.setFont(font)
        self.pushButton_save_out.setObjectName("pushButton_encrypt")
        self.pushButton_save_out.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 490, 200, 30))
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(240, 490, 200, 30))
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(940, 490, 150, 30))
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_paste.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearInput.setGeometry(QtCore.QRect(940, 650, 150, 30))
        self.pushButton_clearInput.setFont(font)
        self.pushButton_clearInput.setObjectName("pushButton_clearInput")
        self.pushButton_clearInput.setStyleSheet(UiHelper.default_style())

        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(1100, 490, 150, 30))
        self.pushButton_copy.setFont(font)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setGeometry(QtCore.QRect(1100, 650, 150, 30))
        self.pushButton_clearOutput.setFont(font)
        self.pushButton_clearOutput.setObjectName("pushButton_clearOutput")
        self.pushButton_clearOutput.setStyleSheet(UiHelper.default_style())

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 650, 200, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet(UiHelper.exit_style())

        Gost.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Gost)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Gost.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_open_in.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_open_iv.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_open_key.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_in.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_out.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_iv.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_key.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.combo_in.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.combo_key.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.combo_mode.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.combo_out.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.with_control_bits_box.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_write_out.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.retranslateUi(Gost)
        QtCore.QMetaObject.connectSlotsByName(Gost)

    def retranslateUi(self, Gost):
        _translate = QtCore.QCoreApplication.translate
        Gost.setWindowTitle(_translate("Gost", "DES"))

        self.pushButton_encrypt.setText(_translate("Gost", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Gost", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Gost", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Gost", "Копировать"))
        self.pushButton_copy.setText(_translate("Gost", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Gost", "Очистить"))
        self.pushButton_exit.setText(_translate("Gost", "Закрыть окно"))
        self.pushButton_save_in.setText(_translate("Gost", "Сохранить"))
        self.pushButton_open_in.setText(_translate("Gost", "Открыть"))
        self.pushButton_save_out.setText(_translate("Gost", "Сохранить"))
        self.pushButton_write_out.setText(_translate("Gost", "Записать"))
        self.pushButton_save_iv.setText(_translate("Gost", "Сохранить IV"))
        self.pushButton_open_iv.setText(_translate("Gost", "Открыть IV"))
        self.pushButton_save_key.setText(_translate("Gost", "Сохранить ключ"))
        self.pushButton_open_key.setText(_translate("Gost", "Открыть ключ"))

        self.textBrowser.setHtml(_translate("Gost", UiHelper.text_browser_html()))
        self.label_info_key.setText(_translate("Gost", "⟵ Введите ключ"))
        self.label_info_key_format.setText(_translate("Gost", "Формат ключа"))
        self.label_info_in.setText(_translate("Gost", "Входной формат данных"))
        self.label_info_out.setText(_translate("Gost", "Выходной формат данных"))
        self.label_info_iv.setText(_translate("Gost", "⟵ IV (опционально)"))
        self.label_info_mode.setText(_translate("Gost", "Режим"))
        self.label_info_control_bits.setText(_translate("Gost", "Контрольный блок ⟶"))
        self.label_info_combo_iv.setText((_translate("Gost", "Формат IV")))
        self.label_info.setText(
            _translate(
                "Gost",
                "Доступный формат входных/выходных данных:\n\n"
                "✓ Текстовый (utf-8)\n"
                "✓ Десятеричный\n"
                "✓ Восьмиричный\n"
                "✓ Двоичный\n\n"
                "Доступные методы работы с файлами:\n\n"
                "✓ Чтение (любое из полей ввода)\n"
                "✓ Запись (любое из полей)\n"
                "✓ Чтение байтов (входное сообщение)\n"
                "✓ Запись байтов (результат шифрования)"
            )
        )
