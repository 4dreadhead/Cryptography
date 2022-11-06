from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class TextInput:
    def __init__(self, obj, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        font = UiHelper.set_font(size=10)

        text_input = QtWidgets.QPlainTextEdit(obj.centralwidget)
        text_input.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_input.setFont(font)
        text_input.setStyleSheet(UiHelper.text_area_style())
        text_input.setObjectName("text_input")

        text_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.widget = text_input

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = 30
        widget_y_pos = round(4 * height / 6 - 120)
        widget_width = width - 60
        widget_height = round(height / 6)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
