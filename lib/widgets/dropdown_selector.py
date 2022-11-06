from PyQt6 import QtCore, QtWidgets
from lib.helpers import UiHelper


class DropdownSelector:
    def __init__(self, obj, items, index, general_count, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates, index, general_count)

        font = UiHelper.set_font(size=10, bold=True, italic=True)

        dropdown_selector = QtWidgets.QComboBox(obj.centralwidget)
        dropdown_selector.addItems(items)
        dropdown_selector.setFont(font)
        dropdown_selector.setStyleSheet(UiHelper.combo_box_style())
        dropdown_selector.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))

        self.widget = dropdown_selector

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, index, general_count):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_width = round((width - 60 - 50 * (general_count - 1)) / general_count)
        widget_height = 30
        widget_x_pos = 30 + index * round(50 + widget_width)
        widget_y_pos = round(2 * height / 3 - 165)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
