from PyQt5 import QtCore, QtGui, QtWidgets
from lib.helpers import UiHelper


class UiScytale(object):
    """
    UI class of method
    Describe all widgets
    """
    pushButton_exit: QtWidgets.QPushButton
    pushButton_clearOutput: QtWidgets.QPushButton
    pushButton_copy: QtWidgets.QPushButton
    pushButton_clearInput: QtWidgets.QPushButton
    pushButton_paste: QtWidgets.QPushButton
    pushButton_decrypt: QtWidgets.QPushButton
    pushButton_encrypt: QtWidgets.QPushButton
    textBrowser: QtWidgets.QTextBrowser
    plainTextEdit: QtWidgets.QPlainTextEdit
    label_info: QtWidgets.QLabel
    label_Scytale_gif: QtWidgets.QLabel
    centralwidget: QtWidgets.QWidget
    statusbar: QtWidgets.QStatusBar
    plainTextEdit_key: QtWidgets.QPlainTextEdit
    label_info_key: QtWidgets.QLabel

    def setupUi(self, Scytale):
        Scytale.setObjectName("Scytale")
        Scytale.resize(800, 600)
        Scytale.setMinimumSize(QtCore.QSize(800, 600))
        Scytale.setMaximumSize(QtCore.QSize(800, 600))
        Scytale.setStyleSheet("background-color: rgb(32, 28, 42);")

        self.centralwidget = QtWidgets.QWidget(Scytale)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Scytale_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_Scytale_gif.setGeometry(QtCore.QRect(30, 30, 431, 221))
        self.label_Scytale_gif.setObjectName("label_Scytale_gif")
        gif = QtGui.QMovie("lib/media/scytale.gif")
        self.label_Scytale_gif.setMovie(gif)
        gif.start()

        font = UiHelper.set_font(size=9)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(480, 30, 291, 221))
        self.label_info.setFont(font)
        self.label_info.setStyleSheet(UiHelper.text_area_style())
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        font = UiHelper.set_font(size=10)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 270, 739, 101))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(UiHelper.text_area_style())
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 420, 739, 101))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(UiHelper.text_area_style())
        self.textBrowser.setObjectName("textBrowser")

        font = UiHelper.set_font("Uroob", size=10, weight=75, bold=True)

        self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 380, 201, 31))
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(240, 380, 201, 31))
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setStyleSheet(UiHelper.encrypt_style())

        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(460, 380, 151, 31))
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_paste.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearInput.setGeometry(QtCore.QRect(460, 530, 151, 31))
        self.pushButton_clearInput.setFont(font)
        self.pushButton_clearInput.setObjectName("pushButton_clearInput")
        self.pushButton_clearInput.setStyleSheet(UiHelper.default_style())

        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(620, 380, 151, 31))
        self.pushButton_copy.setFont(font)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setStyleSheet(UiHelper.default_style())

        self.pushButton_clearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setGeometry(QtCore.QRect(620, 530, 151, 31))
        self.pushButton_clearOutput.setFont(font)
        self.pushButton_clearOutput.setObjectName("pushButton_clearOutput")
        self.pushButton_clearOutput.setStyleSheet(UiHelper.default_style())

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 530, 201, 31))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet(UiHelper.exit_style())

        Scytale.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Scytale)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        Scytale.setStatusBar(self.statusbar)

        self.pushButton_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.retranslateUi(Scytale)
        QtCore.QMetaObject.connectSlotsByName(Scytale)

    def retranslateUi(self, Scytale):
        _translate = QtCore.QCoreApplication.translate
        Scytale.setWindowTitle(_translate("Scytale", "SCYTALE"))

        self.pushButton_encrypt.setText(_translate("Scytale", "Зашифровать"))
        self.pushButton_decrypt.setText(_translate("Scytale", "Расшифровать"))
        self.pushButton_paste.setText(_translate("Scytale", "Вставить"))
        self.pushButton_clearInput.setText(_translate("Scytale", "Копировать"))
        self.pushButton_copy.setText(_translate("Scytale", "Очистить"))
        self.pushButton_clearOutput.setText(_translate("Scytale", "Очистить"))
        self.pushButton_exit.setText(_translate("Scytale", "Закрыть окно"))

        self.textBrowser.setHtml(_translate("Scytale", UiHelper.text_browser_html()))
        self.label_info.setText(
            _translate(
                "Scytale",
                "Размер таблицы:\nОпределяется автоматически.\n\n"
                "Символ дополнения:\n"
                "'⋆' (U-22C6).\n\n"
                "Ввод текста: верхнее поле.\nРезультат: нижнее поле"
            )
        )
