from PyQt6 import QtCore, QtGui, QtWidgets
from lib.helpers import UiHelper


class UiAlberti(object):
    """
    UI class of method
    Describe all widgets
    """
    pushButton_exit: QtWidgets.QPushButton
    label_info_key: QtWidgets.QLabel
    pushButton_clearOutput: QtWidgets.QPushButton
    pushButton_copy: QtWidgets.QPushButton
    pushButton_clearInput: QtWidgets.QPushButton
    pushButton_paste: QtWidgets.QPushButton
    pushButton_decrypt: QtWidgets.QPushButton
    pushButton_encrypt: QtWidgets.QPushButton
    textBrowser: QtWidgets.QTextBrowser
    plainTextEdit_key: QtWidgets.QPlainTextEdit
    plainTextEdit: QtWidgets.QPlainTextEdit
    label_info: QtWidgets.QLabel
    label_Alberti_gif: QtWidgets.QLabel
    centralwidget: QtWidgets.QWidget
    statusbar: QtWidgets.QStatusBar

    def setupUi(self, Alberti):
        Alberti.setObjectName("Alberti")
        Alberti.resize(800, 650)
        Alberti.setMinimumSize(QtCore.QSize(800, 650))
        Alberti.setMaximumSize(QtCore.QSize(800, 650))
        Alberti.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Alberti)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Alberti_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Alberti_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_Alberti_gif.setObjectName("label_alberti_gif")
        gif = QtGui.QMovie("lib/media/alberti.gif")
        self.label_Alberti_gif.setMovie(gif)
        gif.start()

        font = UiHelper.set_font(size=9)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(480, 30, 289, 279))
        self.label_info.setFont(font)
        self.label_info.setStyleSheet(UiHelper.text_area_style())
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")

        font = UiHelper.set_font(size=10, bold=True, italic=True)

        self.label_info_key = QtWidgets.QLabel(self.centralwidget)
        self.label_info_key.setGeometry(QtCore.QRect(201, 278, 260, 31))
        self.label_info_key.setFont(font)
        self.label_info_key.setStyleSheet(UiHelper.text_area_style())
        self.label_info_key.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_key.setObjectName("label_info")

        font = UiHelper.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 320, 739, 101))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_key.setGeometry(QtCore.QRect(30, 278, 150, 31))
        self.plainTextEdit_key.setFont(font)
        self.plainTextEdit_key.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit_key.setObjectName("plainTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 470, 739, 101))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(UiHelper.text_area_style())
        self.textBrowser.setObjectName("textBrowser")

        font = UiHelper.set_font("Droid Sans Mono", size=10, bold=True)

        self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 430, 201, 31))
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(240, 430, 201, 31))
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(460, 430, 151, 31))
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_paste.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearInput.setGeometry(QtCore.QRect(460, 580, 151, 31))
        self.pushButton_clearInput.setFont(font)
        self.pushButton_clearInput.setObjectName("pushButton_clearInput")
        self.pushButton_clearInput.setStyleSheet(UiHelper.default_style())

        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(620, 430, 151, 31))
        self.pushButton_copy.setFont(font)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setGeometry(QtCore.QRect(620, 580, 151, 31))
        self.pushButton_clearOutput.setFont(font)
        self.pushButton_clearOutput.setObjectName("pushButton_clearOutput")
        self.pushButton_clearOutput.setStyleSheet(UiHelper.default_style())

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 580, 201, 31))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet(UiHelper.exit_style())

        Alberti.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Alberti)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Alberti.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.retranslateUi(Alberti)
        QtCore.QMetaObject.connectSlotsByName(Alberti)

    def retranslateUi(self, Alberti):
        _translate = QtCore.QCoreApplication.translate
        Alberti.setWindowTitle(_translate("Alberti", "ALBERTI"))

        self.pushButton_encrypt.setText(_translate("Alberti", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Alberti", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Alberti", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Alberti", "Копировать"))
        self.pushButton_copy.setText(_translate("Alberti", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Alberti", "Очистить"))
        self.pushButton_exit.setText(_translate("Alberti", "Закрыть окно"))

        self.label_info_key.setText(_translate("Alberti", "⟵ Введите ключ."))
        self.textBrowser.setHtml(_translate("Alberti", UiHelper.text_browser_html()))
        self.label_info.setText(
            _translate(
                "Alberti",
                "Поддерживаемые алфавиты:\n⚫ Латинский\n⚫ Кириллица\n\n"
                "⚠ Все символы,\nне входящие в них,\nостанутся неизменными.\n\n"
                "Ввод текста: верхнее поле\nРезультат: нижнее поле"
            )
        )
