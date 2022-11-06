from PyQt6 import QtCore, QtWidgets
from lib.helpers import UiHelper


class CheckboxLabel:
    def __init__(self, obj, text, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font(size=10, bold=True, italic=True)

        text_label = QtWidgets.QLabel(obj.centralwidget)
        text_label.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_label.setFont(font)
        text_label.setStyleSheet(UiHelper.text_area_style())
        text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        text_label.setObjectName("checkbox_label")

        text_label.setText(translate("Object", text))

        self.widget = text_label

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = 240
        widget_y_pos = height - 60
        widget_width = 170
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height
