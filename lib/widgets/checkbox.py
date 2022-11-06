from PyQt6 import QtCore, QtWidgets
from lib.helpers import UiHelper


class Checkbox:
    def __init__(self, obj, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        checkbox = QtWidgets.QCheckBox(obj.centralwidget)
        checkbox.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        checkbox.setStyleSheet(UiHelper.trash_box_style())
        checkbox.setObjectName("with_control_bits_box")

        self.widget = checkbox

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = 410
        widget_y_pos = height - 60
        widget_width = 30
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height
