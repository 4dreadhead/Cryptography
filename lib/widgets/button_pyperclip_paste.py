import pyperclip
from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class ButtonPyperclipPaste:
    def __init__(self, obj, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font("Droid Sans Mono", size=10, bold=True)

        button = QtWidgets.QPushButton(obj.centralwidget)
        button.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        button.setFont(font)
        button.setObjectName("button_pyperclip_paste")
        button.setStyleSheet(UiHelper.default_style())

        button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setText(translate("Object", "Вставить"))

        button.clicked.connect(lambda: self.paste(obj))

        self.widget = button

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = width - 340
        widget_y_pos = round(5 * height / 6 - 110)
        widget_width = 150
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height

    @staticmethod
    def paste(obj):
        obj.text_input.setPlainText(pyperclip.paste())
        obj.statusbar.showMessage("Текст вставлен из буффера обмена.")
