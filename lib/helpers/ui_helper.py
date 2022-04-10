from PyQt5.QtGui import QFont


class UiHelper:
    """
    This class contains common styles, methods, e.t.c for all UI classes
    """
    @staticmethod
    def set_font(family=None, size=12, weight=None, bold=False, italic=False):
        """
        This function sets the font with specified parameters
        :param family: str: font family
        :param size: int: font size
        :param weight: int: font weight
        :param bold: bool: is bold
        :param italic: bool: is italic
        :return: QFont: font
        """
        font = QFont()
        if family:
            font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        if weight:
            font.setWeight(weight)
        return font

    @staticmethod
    def text_browser_html():
        """
        This function returns html code for setting style of QtWidgets.QTextBrowser
        :return: str: html style
        """
        style = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"" +\
                "http://www.w3.org/TR/REC-html40/strict.dtd\">\n" +\
                "<html><head><meta name=\"qrichtext\" content=\"1\" />" +\
                "<style type=\"text/css\">\n" +\
                "p, li { white-space: pre-wrap; }\n" +\
                "</style></head><body style=\" font-family:\'Ubuntu\'; " +\
                "font-size:12pt; font-weight:400; font-style:normal;\">\n" +\
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; " +\
                "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;" +\
                "\"><br /></p></body></html>"
        return style

    # All methods bellow
    # Returns CSS styles for widgets

    @staticmethod
    def text_area_style():
        style = "background-color: rgb(48, 42, 61);\ncolor: rgb(238, 238, 236);"
        return style

    @staticmethod
    def default_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                           color: rgb(14,149,226); }
                       QPushButton:!hover { background-color: rgb(48, 42, 61);
                                            color: rgb(14,149,226); }
                       QPushButton:pressed { background-color: rgb(24, 21, 30);
                                             color: rgb(14,149,226); }"""
        return style

    @staticmethod
    def encrypt_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                           color: rgb(28,180,230); }
                       QPushButton:!hover { background-color: rgb(48, 42, 61);
                                            color: rgb(28,180,230); }
                       QPushButton:pressed { background-color: rgb(24, 21, 30);
                                             color: rgb(28,180,230); }"""
        return style

    @staticmethod
    def exit_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                           color: rgb(255,65,100); }
                       QPushButton:!hover { background-color: rgb(48, 42, 61);
                                            color: rgb(255,65,100); }
                       QPushButton:pressed { background-color: rgb(24, 21, 30);
                                             color: rgb(255,65,100); }"""
        return style

    @staticmethod
    def in_development_style():
        style = """QPushButton:hover { background-color: rgb(64, 56, 84);
                                           color: rgb(201,44,123); }
                       QPushButton:!hover { background-color: rgb(48, 42, 61);
                                            color: rgb(201,44,123); }
                       QPushButton:pressed { background-color: rgb(24, 21, 30);
                                            color: rgb(201,44,123); }"""
        return style

    @staticmethod
    def trash_box_style():
        style = """ 
                QCheckBox {
                    color: white;
                    spacing: 9px;
                    width: 19px;
                    height: 19px;
                }
                QCheckBox::indicator {
                    width: 19px;
                    height: 19px;
                }
            """
        return style
