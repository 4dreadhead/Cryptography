from PyQt6 import QtCore, QtWidgets
from lib.helpers import UiHelper


class DropdownSelectorLabel:
    def __init__(self, obj, text, index, general_count, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(
            obj.window_size, custom_coordinates, index, general_count
        )

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font(size=10, bold=True, italic=True)

        text_label = QtWidgets.QLabel(obj.centralwidget)
        text_label.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_label.setFont(font)
        text_label.setStyleSheet(UiHelper.text_area_style())
        text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        text_label.setObjectName("dropdown_selector_label")

        text_label.setText(translate("Object", text))

        self.widget = text_label

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, index, general_count):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_width = round((width - 60 - 50 * (general_count - 1)) / general_count)
        widget_height = 30
        widget_x_pos = 30 + index * round(50 + widget_width)
        widget_y_pos = round(2 * height / 3 - 195)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
