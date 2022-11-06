from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class TextAdditionalInput:
    def __init__(self, obj, custom_coordinates=None, take_place_level=0):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(
            obj.window_size, custom_coordinates, take_place_level
        )

        font = UiHelper.set_font(size=10)

        text_input = QtWidgets.QPlainTextEdit(obj.centralwidget)
        text_input.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_input.setFont(font)
        text_input.setStyleSheet(UiHelper.text_area_style())
        text_input.setObjectName("text_additional_input")

        text_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.widget = text_input

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, take_place_level):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        given_place = 40 * take_place_level

        widget_x_pos = 30
        widget_y_pos = round(2 * height / 3 - 120 - given_place)
        widget_width = round(width * 0.425)
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height
