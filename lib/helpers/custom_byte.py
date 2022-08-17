class CustomByte:
    """
    Class of custom byte to easy-use:
        - returning to  BIN|HEX|DEC format
        - creating from BIN|HEX|DEC format
        - formatting from inputs to binary string
    """
    def __init__(self, incoming_byte):
        """
        Initialization
        :param incoming_byte: [int] decimal presentation of incoming byte
        """
        self.decimal = int(incoming_byte, 2)
        self.hex = format(self.decimal, "x").zfill(2)
        self.binary = format(self.decimal, "b").zfill(8)

    def to_bin(self):
        """
        :return: [str] binary presentation of [self]
        """
        return self.binary

    def to_hex(self):
        """
        :return: [str] hexadecimal presentation of [self]
        """
        return self.hex

    def to_dec(self):
        """
        :return: [int] decimal presentation of [self]
        """
        return self.decimal

    @staticmethod
    def load_from_bin(binary_byte):
        """
        Creating [self] from byte in binary presentation
        :param binary_byte: [str]  incoming byte
        :return:            [self] instance
        """
        return CustomByte(binary_byte)

    @staticmethod
    def load_from_dec(decimal_byte):
        """
        Creating [self] from byte in decimal presentation
        :param decimal_byte:    [str]  incoming byte
        :return:                [self] instance
        """
        return CustomByte(format(int(decimal_byte), "b").zfill(8))

    @staticmethod
    def load_from_hex(hex_byte):
        """
        Creating [self] from byte in hexadecimal presentation
        :param hex_byte:    [str]  incoming byte
        :return:            [self] instance
        """
        return CustomByte(format(int(hex_byte, 16), "b").zfill(8))

    @staticmethod
    def read_bytes(data, data_format):
        """
        Read bytes from incoming data and create binary string
        :param data:                [str] incoming data
        :param data_format:         [str] data format (TEXT or HEX or BIN or DEC)
        :return: formatted_data:    [str] binary string
        """
        match data_format:
            case "BIN":
                formatted_data = data.replace(" ", "").replace("\n", "")
            case "HEX":
                formatted_data = data.replace(" ", "").replace("\n", "")
                formatted_data = "".join([
                    CustomByte.load_from_hex(
                        formatted_data[2 * i:2 * (i + 1)]
                    ).to_bin() for i in range(len(formatted_data) // 2)
                ])
            case "DEC":
                preparing_data = data.split(" ")
                formatted_data = []
                for byte in preparing_data:
                    if not 0 <= int(byte) < 256:
                        raise ValueError(f"Incorrect byte value: {byte}.")
                    formatted_data.append(CustomByte.load_from_dec(byte).to_bin())
                formatted_data = "".join(formatted_data)

            case "TEXT":
                formatted_data = "".join(
                    [
                        CustomByte.load_from_dec(byte).to_bin() for byte in bytearray(
                            data, "utf-8"
                        )
                    ]
                )
            case _:
                raise ValueError(f"Неизвестный тип данных: {data_format}")
        return formatted_data
