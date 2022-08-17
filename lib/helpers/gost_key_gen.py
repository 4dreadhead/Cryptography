from .des_const import PC_TABLES, ROUND_SHUFFLE_TABLE
from .custom_byte import CustomByte


class GostKeyGen:
    """
    Key generator for GOST algorithm
    """
    def __init__(self, key=None, key_format=None):
        """
        Initialization
        :param key:         [str] incoming key from inputs
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        result:             [dict[int, str]] generated round keys
        """
        self.read_key = self.read_and_generate_key(key, key_format)
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

    @staticmethod
    def read_and_generate_key(key=None, key_format=None):
        """
        Read data from incoming key with passed format
        :param key:         [str] incoming key
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        :return: result:    [str] formatted key as binary string
        """
        if not key:
            raise ValueError("Не задан ключ.")

        result = CustomByte.read_bytes(key, key_format)

        if len(result) != 256:
            raise ValueError(f"Неверный размер ключа: {len(result)} бит. Ожидалось: 256 бит.")

        return result
