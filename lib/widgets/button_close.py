from PyQt6 import QtCore, QtWidgets, QtGui
from lib.helpers import UiHelper


class ButtonClose:
    def __init__(self, obj, custom_coordinates=None):
        x_pos, y_pos, width, height = self.__class__.get_coordinates(obj.window_size, custom_coordinates)

        translate = QtCore.QCoreApplication.translate
        font = UiHelper.set_font("Droid Sans Mono", size=10, bold=True)

        button = QtWidgets.QPushButton(obj.centralwidget)
        button.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        button.setFont(font)
        button.setObjectName("button_close")
        button.setStyleSheet(UiHelper.exit_style())

        button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setText(translate("Object", "Закрыть окно"))

        button.clicked.connect(obj.close)

        self.widget = button

    @staticmethod
    def get_coordinates(object_size, custom_coordinates):
        if custom_coordinates:
            return custom_coordinates

        width, height = object_size

        widget_x_pos = 30
        widget_y_pos = height - 60
        widget_width = 200
        widget_height = 30

        return widget_x_pos, widget_y_pos, widget_width, widget_height
