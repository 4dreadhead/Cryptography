from PyQt6 import QtCore, QtWidgets, QtGui


class Centralwidget:
    def __init__(self, obj, window_title):
        width, height = obj.window_size

        obj.setObjectName("Object")
        obj.resize(width, height)
        obj.setMinimumSize(width, height)
        obj.setMaximumSize(width, height)
        obj.setStyleSheet("background-color: rgb(32, 28, 42);")

        obj.centralwidget = QtWidgets.QWidget(obj)
        obj.centralwidget.setObjectName("centralwidget")

        obj.setCentralWidget(obj.centralwidget)
        obj.statusbar = QtWidgets.QStatusBar(obj)
        obj.statusbar.setObjectName("statusbar")
        obj.statusbar.setStyleSheet("color: rgb(238, 238, 236);")
        obj.setStatusBar(obj.statusbar)

        translate = QtCore.QCoreApplication.translate
        obj.setWindowTitle(translate("Object", window_title))
        obj.setWindowIcon(QtGui.QIcon('lib/media/icon.png'))
