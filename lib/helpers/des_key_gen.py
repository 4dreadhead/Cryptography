from .des_const import PC_TABLES, ROUND_SHUFFLE_TABLE
from .custom_byte import CustomByte


class DesKeyGen:
    """
    Key generator for DES algorithm
    """
    def __init__(self, key=None, key_format=None):
        """
        Initialization
        :param key:         [str] incoming key from inputs
        :param key_format:  [str] key format (TEXT or HEX or BIN or DEC)
        result:             [dict[int, str]] generated round keys
        """
        self.read_key = self.read_and_generate_key(key, key_format)

        match len(self.read_key):
            case 56:
                prepared_key = self.add_control_bits()
            case 64:
                prepared_key = self.read_key
            case _:
                raise ValueError(f"Неверный размер ключа: {len(self.read_key)} бит. Ожидалось: 56 или 64 бит.")

        self.prepared_key = self.key_pc_shuffle(prepared_key, "START")
        self.round_keys = self.generate_round_keys()

    def __repr__(self):
        return self.round_keys

    def add_control_bits(self):
        """
        Add control bits to incoming 56bit key
        :return: key_64bit: [str] key with control bits
        """
        key_64bit = ""
        control_bits = []
        key_7bit_blocks = [self.read_key[7 * i:7 * (i + 1)] for i in range(8)]

        for bits in key_7bit_blocks:
            control_bits.append(str(1 - sum(map(int, list(bits))) % 2))

        for block_7bit, control_bit in zip(key_7bit_blocks, control_bits):
            key_64bit += block_7bit + control_bit

        return key_64bit

    def generate_round_keys(self):
        """
        Generate keys for each DES round
        :return: round_keys: [dict[int, str]] generated round keys
        """
        round_key = self.prepared_key
        round_keys = {}

        for round_ in range(1, 17):
            round_key = self.key_round_shuffle(round_key, round_)
            shuffled_round_key = self.key_pc_shuffle(round_key, "END")
            round_keys[round_] = shuffled_round_key

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

        if len(result) != 56 and len(result) != 64:
            raise ValueError(f"Неверный размер ключа: {len(result)} бит. Ожидалось: 56 или 64 бит.")

        return result

    @staticmethod
    def key_pc_shuffle(key_64bit, action):
        """
        PC-shuffle of key
        :param key_64bit:   [str] prepared 64bit key
        :param action:      [str] START or END
        :return:            [str] shuffled key
        """
        return "".join([key_64bit[i - 1] for i in PC_TABLES[action]])

    @staticmethod
    def key_round_shuffle(key_56bit, round_):
        """
        Prepare key for each round
        :param key_56bit: [str] incoming 56bit key
        :param round_:    [int] number of current round
        :return:          [str] prepared key for round
        """
        first_block, second_block = key_56bit[:28], key_56bit[28:]
        result_blocks = []

        for block in (first_block, second_block):
            result_blocks.append("".join([block[(i + ROUND_SHUFFLE_TABLE[round_]) % 28] for i in range(28)]))

        return "".join(result_blocks)
