import random
from .des_const import PC_TABLES, ROUND_SHUFFLE_TABLE


class Byte:
    def __init__(self, incoming_byte):
        self.decimal = int(incoming_byte, 2)
        self.hex = hex(self.decimal)[2:].zfill(2)
        self.binary = bin(self.decimal)[2:].zfill(8)

    def to_bin(self):
        return self.binary

    def to_hex(self):
        return self.hex

    def to_dec(self):
        return self.decimal

    @staticmethod
    def load_from_bin(binary_byte):
        return Byte(binary_byte)

    @staticmethod
    def load_from_dec(decimal_byte):
        return Byte(bin(int(decimal_byte))[2:].zfill(8))

    @staticmethod
    def load_from_hex(hex_byte):
        return Byte(bin(int(hex_byte, 16))[2:].zfill(8))


class KeyGen:
    def __init__(self, key=None, key_format=None):
        self.read_key = self.generate_56bit_key(key, key_format)
        self.prepared_key = self.key_pc_shuffle(self.add_control_bits(), "START")
        self.round_keys = self.generate_round_keys()

    def __repr__(self):
        return self.round_keys

    def add_control_bits(self):
        key_64bit = ""
        control_bits = []
        key_7bit_blocks = [self.read_key[7 * i:7 * (i + 1)] for i in range(8)]

        for bits in key_7bit_blocks:
            control_bits.append(str(1 - sum(map(int, list(bits))) % 2))

        for block_7bit, control_bit in zip(key_7bit_blocks, control_bits):
            key_64bit += block_7bit + control_bit

        return key_64bit

    def generate_round_keys(self):
        round_key = self.prepared_key
        round_keys = {}

        for round_ in range(1, 17):
            round_key = self.key_round_shuffle(round_key, round_)
            shuffled_round_key = self.key_pc_shuffle(round_key, "END")
            round_keys[round_] = shuffled_round_key

        return round_keys

    @staticmethod
    def generate_56bit_key(key=None, key_format=None):
        if not key:
            raise ValueError("Given empty key.")

        match key_format:
            case "BIN":
                result = key.replace(" ", "").replace("\n", "")
            case "HEX":
                result = key.replace(" ", "").replace("\n", "")
                result = "".join([
                    Byte.load_from_hex(
                        result[2 * i:2 * (i + 1)]
                    ).to_bin() for i in range(len(result) // 2)
                ])
            case "DEC":
                preparing_data = key.split(" ")
                result = []
                for byte in preparing_data:
                    if not 0 <= int(byte) < 256:
                        raise ValueError(f"Incorrect byte value: {byte}.")
                    result.append(Byte.load_from_dec(byte).to_bin())
                result = "".join(result)

            case "TEXT":
                result = "".join(
                    [
                        Byte.load_from_dec(byte).to_bin() for byte in bytearray(
                            key, "utf-8"
                        )
                    ]
                )
            case _:
                raise ValueError("Unknown data type")

        if len(result) != 56:
            raise ValueError(f"Wrong key size: {len(result)}. Expected: 56")

        return result

    @staticmethod
    def key_pc_shuffle(key_64bit, action):
        return "".join([key_64bit[i - 1] for i in PC_TABLES[action]])

    @staticmethod
    def key_round_shuffle(key_56bit, round_):
        first_block, second_block = key_56bit[:28], key_56bit[28:]
        result_blocks = []

        for block in (first_block, second_block):
            result_blocks.append("".join([block[(i + ROUND_SHUFFLE_TABLE[round_]) % 28] for i in range(28)]))

        return "".join(result_blocks)
