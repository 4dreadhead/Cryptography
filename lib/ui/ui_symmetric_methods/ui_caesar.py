import lib.widgets as widgets


class UiCaesar(object):
    def setupUi(self):
        self.window_size = (800, 600)

        widgets.Centralwidget(self, "CAESAR")
        info_text = "Поддерживаемые алфавиты:\n⚫ Латинский\n⚫ Кириллица\n\n" + \
                    "⚠ Все символы,\nне входящие в них,\nостанутся неизменными.\n\n" + \
                    "Ввод текста: верхнее поле\nРезультат: нижнее поле"
        info_text_key = "⟵ Введите ключ"

        self.button_encrypt = widgets.ButtonEncrypt(self).widget
        self.button_decrypt = widgets.ButtonDecrypt(self).widget
        self.text_input = widgets.TextInput(self).widget
        self.text_output = widgets.TextOutput(self).widget
        self.text_label = widgets.TextLabel(self, info_text).widget
        self.button_clear_input = widgets.ButtonClear(self, self.text_input).widget
        self.button_clear_output = widgets.ButtonClear(self, self.text_output, order=1).widget
        self.button_close = widgets.ButtonClose(self).widget
        self.button_copy = widgets.ButtonPyperclipCopy(self).widget
        self.button_paste = widgets.ButtonPyperclipPaste(self).widget
        self.gif_label = widgets.GifLabel(self, "caesar.gif", give_place_level=1).widget
        self.additional_input_key = widgets.TextAdditionalInput(self, take_place_level=1).widget
        self.text_additional_label_key = widgets.TextAdditionalLabel(self, info_text_key, take_place_level=1).widget
