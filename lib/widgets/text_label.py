from PyQt6 import QtCore, QtWidgets
from lib.helpers import UiHelper


class TextLabel:
    def __init__(self, obj, text, custom_coordinates=None, give_place_level=0):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates, give_place_level)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font(size=9)

        text_label = QtWidgets.QLabel(obj.centralwidget)
        text_label.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_label.setFont(font)
        text_label.setStyleSheet(UiHelper.text_area_style())
        text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        text_label.setObjectName("text_label")

        text_label.setText(translate("Object", text))

        self.widget = text_label

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, give_place_level):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        given_place = give_place_level * 40

        widget_x_pos = 40 + round(0.625 * width)
        widget_y_pos = 30
        widget_width = width - widget_x_pos - 30
        widget_height = round(2 * height / 3 - 160 - given_place)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
