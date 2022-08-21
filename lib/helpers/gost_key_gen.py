import random
import string

from .custom_byte import CustomByte


class GostKeyGen:
    """
    Key generator for GOST algorithm
    """
    def __init__(self, key=None, key_format=None, key_field=None):
        """
        Initialization
        :param key:         [str] incoming key from inputs
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        :param key_field:   [QtWidgets.QPlainTextEdit] input field for key
        result:             [dict[int, str]] generated round keys
        """
        self.read_key = self.read_and_generate_key(key, key_format, key_field)
        self.round_keys = self.generate_round_keys()

    def __repr__(self):
        return self.round_keys

    def generate_round_keys(self, block_size=32):
        """
        Generate keys for each GOST round
        :return: round_keys: [dict[str, list[str]]] generated round keys
        """
        key_blocks = [self.read_key[i:i + block_size] for i in range(0, len(self.read_key), block_size)]

        round_keys = {
            "encrypt": key_blocks * 3 + list(reversed(key_blocks)),
            "decrypt": key_blocks + list(reversed(key_blocks)) * 3
        }

        return round_keys

    def read_and_generate_key(self, key, key_format, key_field):
        """
        Read data from incoming key with passed format
        :param key:         [str] incoming key
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        :param key_field:   [QtWidgets.QPlainTextEdit] input field for key
        :return: result:    [str] formatted key as binary string
        """
        if not key:
            key = self.generate_random_key(key_format, key_field)

        result = CustomByte.read_bytes(key, key_format)

        if len(result) != 256:
            raise ValueError(f"Неверный размер ключа: {len(result)} бит. Ожидалось: 256 бит.")

        return result

    @staticmethod
    def generate_random_key(key_format, key_field, size=32):
        """
        Generate random key for GOST algorithm
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        :param key_field:   [QtWidgets.QPlainTextEdit] input field for key
        :param size:        [int] key size (bytes)
        :return: result:    [str] generated key
        """
        match key_format:
            case "DEC":
                result = " ".join([format(byte, "d") for byte in random.randbytes(size)])
            case "HEX":
                result = " ".join([format(byte, "x").zfill(2) for byte in random.randbytes(size)])
            case "BIN":
                result = " ".join([format(byte, "b").zfill(8) for byte in random.randbytes(size)])
            case "TEXT":
                result = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size))
            case _:
                raise ValueError(f"Неизвестный формат ключа: {key_format}")

        key_field.setPlainText(result)
        return result
