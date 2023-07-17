class Color:
    def __init__(self, red: float, green: float, blue: float, opacity: float = 1.0):
        for argument in [red, green, blue, opacity]:
            if type(argument) is not float:
                raise TypeError("arguments must be floats")
            if (argument < 0.0) or (argument > 1.0):
                raise ValueError("arguments must be between 0.0 and 1.0")
        self.red: float = red
        self.green: float = green
        self.blue: float = blue
        self.opacity: float = opacity

    def get_color_hex_str(self) -> str:
        hex_str: str = '#'
        hex_str += hex(int(self.red * 255))[2:]
        hex_str += hex(int(self.green * 255))[2:]
        hex_str += hex(int(self.blue * 255))[2:]

        return hex_str

    def get_color_list(self) -> list[float]:
        return [self.red, self.green, self.blue, self.opacity]

    def __repr__(self) -> str:
        return self.get_color_hex_str()

    def __str__(self) -> str:
        return f"r: {self.red} g: {self.green} b: {self.blue} a: {self.opacity}"


def build_color_from_hex_str(hex_str: str, opacity: float = 1.0) -> Color:
    if type(hex_str) is not str:
        raise TypeError("hex must be a string")
    if type(opacity) is not float:
        raise TypeError("opacity must be a float")

    if (opacity < 0.0) or (opacity > 1.0):
        raise ValueError("opacity must be between 0.0 and 1.0")
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError("hex must be of length 6 (excepting #)")

    # Each set of 2 characters is cast to decimal from base 16, and then divides by 255 to get a value 0 - 1
    red: float = int(hex_str[0:2], 16) / 255
    green: float = int(hex_str[2:4], 16) / 255
    blue: float = int(hex_str[4:6], 16) / 255

    return Color(red, green, blue, opacity)


def build_color_from_list(val_ls: list[float]) -> Color:
    if type(val_ls) is not list:
        raise TypeError("val_ls must be a list")
    for elem in val_ls:
        if type(elem) is not float:
            raise TypeError("val_ls must only contain floats")
    if len(val_ls) != 4:
        raise ValueError("val_ls must contain exactly four elements")

    return Color(*val_ls)
