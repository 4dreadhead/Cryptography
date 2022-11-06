from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class TextOutput:
    def __init__(self, obj, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font(size=10)

        text_output = QtWidgets.QTextBrowser(obj.centralwidget)
        text_output.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        text_output.setFont(font)
        text_output.setStyleSheet(UiHelper.text_area_style())
        text_output.setObjectName("text_output")

        text_output.setHtml(translate("Object", UiHelper.text_browser_html()))
        text_output.viewport().setProperty("Object", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))

        self.widget = text_output

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = 30
        widget_y_pos = round(5 * height / 6 - 70)
        widget_width = width - 60
        widget_height = round(height / 6)

        return widget_x_pos, widget_y_pos, widget_width, widget_height
