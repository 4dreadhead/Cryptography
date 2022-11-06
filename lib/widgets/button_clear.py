from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class ButtonClear:
    def __init__(self, obj, to_clear, custom_coordinates=None, order=0):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates, order)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font("Droid Sans Mono", size=10, bold=True)

        button = QtWidgets.QPushButton(obj.centralwidget)
        button.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        button.setFont(font)
        button.setObjectName("button_clear")
        button.setStyleSheet(UiHelper.default_style())

        button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setText(translate("Object", "Очистить"))

        button.clicked.connect(lambda: self.clear(obj, to_clear))

        self.widget = button

    @staticmethod
    def get_coordinates(object_size, custom_coordinates, order):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = width - 180
        widget_y_pos = round(5 * height / 6 - 110) if order == 0 else height - 60
        widget_width = 150
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height

    @staticmethod
    def clear(obj, to_clear):
        to_clear.clear()
        obj.statusbar.showMessage("Поле очищено.")
