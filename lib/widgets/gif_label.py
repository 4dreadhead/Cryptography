from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class GifLabel:
    def __init__(self, obj, filename, custom_coordinates=None, give_place_level=0):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(
            obj.window_size, custom_coordinates, give_place_level
        )

        gif_widget = QtWidgets.QLabel(obj.centralwidget)
        gif_widget.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        gif_widget.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        gif_widget.setObjectName("gif_widget")
        gif_widget.setStyleSheet(UiHelper.gif_style())
        gif = QtGui.QMovie(f"lib/media/{filename}")
        gif_widget.setMovie(gif)
        gif.start()

        self.widget = gif_widget

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, give_place_level):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        given_place = give_place_level * 40

        widget_x_pos = 30
        widget_y_pos = 30
        widget_width = round(0.625 * width)
        widget_height = round(2 * height / 3 - 160 - given_place)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
