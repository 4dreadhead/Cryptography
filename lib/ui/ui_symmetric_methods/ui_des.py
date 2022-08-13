from PyQt6 import QtCore, QtGui, QtWidgets
from lib.helpers import UiHelper


class UiDes(object):
    """
    UI class of method
    """
    def setupUi(self, Des):
        Des.setObjectName("Des")
        Des.resize(1280, 720)
        Des.setMinimumSize(QtCore.QSize(1280, 720))
        Des.setMaximumSize(QtCore.QSize(1280, 720))
        Des.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Des)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Des_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Des_gif.setGeometry(QtCore.QRect(30, 30, 800, 120))
        self.label_Des_gif.setObjectName("label_des_gif")
        gif = QtGui.QMovie("lib/media/des.gif")
        self.label_Des_gif.setMovie(gif)
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
        self.label_info_iv.setObjectName("label_info_key")

        self.label_info_key_format = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key_format.setGeometry(QtCore.QRect(30, 290, 230, 30))
        self.label_info_key_format.setFont(font)
        self.label_info_key_format.setStyleSheet(UiHelper.text_area_style())
        self.label_info_key_format.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_key_format.setObjectName("label_info_key_format")

        self.label_info_in = QtWidgets.QLabel(self.centralwidget)
        self.label_info_in.setGeometry(QtCore.QRect(360, 290, 230, 30))
        self.label_info_in.setFont(font)
        self.label_info_in.setStyleSheet(UiHelper.text_area_style())
        self.label_info_in.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_in.setObjectName("label_info_in")

        self.label_info_out = QtWidgets.QLabel(self.centralwidget)
        self.label_info_out.setGeometry(QtCore.QRect(690, 290, 230, 30))
        self.label_info_out.setFont(font)
        self.label_info_out.setStyleSheet(UiHelper.text_area_style())
        self.label_info_out.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_out.setObjectName("label_info_out")

        self.combo_key = QtWidgets.QComboBox(self.centralwidget)
        self.combo_key.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_key.setFont(font)
        self.combo_key.setStyleSheet(UiHelper.combo_box_style())
        self.combo_key.setGeometry(QtCore.QRect(30, 320, 230, 30))

        self.combo_in = QtWidgets.QComboBox(self.centralwidget)
        self.combo_in.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_in.setFont(font)
        self.combo_in.setStyleSheet(UiHelper.combo_box_style())
        self.combo_in.setGeometry(QtCore.QRect(360, 320, 230, 30))

        self.combo_out = QtWidgets.QComboBox(self.centralwidget)
        self.combo_out.addItems(["TEXT", "BIN", "HEX", "DEC"])
        self.combo_out.setFont(font)
        self.combo_out.setStyleSheet(UiHelper.combo_box_style())
        self.combo_out.setGeometry(QtCore.QRect(690, 320, 230, 30))

        self.label_info_mode = QtWidgets.QLabel(self.centralwidget)
        self.label_info_mode.setGeometry(QtCore.QRect(1020, 290, 230, 30))
        self.label_info_mode.setFont(font)
        self.label_info_mode.setStyleSheet(UiHelper.text_area_style())
        self.label_info_mode.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_mode.setObjectName("label_info_out")

        self.combo_mode = QtWidgets.QComboBox(self.centralwidget)
        self.combo_mode.addItems(["ECB", "CBC", "CFB", "OFB"])
        self.combo_mode.setFont(font)
        self.combo_mode.setStyleSheet(UiHelper.combo_box_style())
        self.combo_mode.setGeometry(QtCore.QRect(1020, 320, 230, 30))

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

        font = UiHelper.set_font("Uroob", size=10, bold=True)

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

        Des.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Des)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Des.setStatusBar(self.statusbar)

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
        self.pushButton_write_out.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.retranslateUi(Des)
        QtCore.QMetaObject.connectSlotsByName(Des)

    def retranslateUi(self, Des):
        _translate = QtCore.QCoreApplication.translate
        Des.setWindowTitle(_translate("Des", "DES"))

        self.pushButton_encrypt.setText(_translate("Des", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Des", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Des", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Des", "Копировать"))
        self.pushButton_copy.setText(_translate("Des", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Des", "Очистить"))
        self.pushButton_exit.setText(_translate("Des", "Закрыть окно"))
        self.pushButton_save_in.setText(_translate("Des", "Сохранить"))
        self.pushButton_open_in.setText(_translate("Des", "Открыть"))
        self.pushButton_save_out.setText(_translate("Des", "Сохранить"))
        self.pushButton_write_out.setText(_translate("Des", "Записать"))
        self.pushButton_save_iv.setText(_translate("Des", "Сохранить IV"))
        self.pushButton_open_iv.setText(_translate("Des", "Открыть IV"))
        self.pushButton_save_key.setText(_translate("Des", "Сохранить ключ"))
        self.pushButton_open_key.setText(_translate("Des", "Открыть ключ"))

        self.textBrowser.setHtml(_translate("Des", UiHelper.text_browser_html()))
        self.label_info_key.setText(_translate("Des", "⟵ Введите ключ"))
        self.label_info_key_format.setText(_translate("Des", "Формат ключа"))
        self.label_info_in.setText(_translate("Des", "Входной формат данных"))
        self.label_info_out.setText(_translate("Des", "Выходной формат данных"))
        self.label_info_iv.setText(_translate("Des", "⟵ IV (опционально)"))
        self.label_info_mode.setText(_translate("Des", "Режим"))
        self.label_info.setText(
            _translate(
                "Des",
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
