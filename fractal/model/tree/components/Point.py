from decimal import Decimal


class Point:
    x: Decimal
    y: Decimal

    def __init__(self, x: Decimal = Decimal(0), y: Decimal = Decimal(0)):
        self.x = x
        self.y = y

    def get_coords(self) -> tuple[Decimal, Decimal]:
        return self.x, self.y

    def get_coords_inverted(self, invert_x: bool = False, invert_y: bool = False) -> tuple[Decimal, Decimal]:
        new_x: Decimal = self.x
        new_y: Decimal = self.y
        if invert_x:
            new_x = -new_x
        if invert_y:
            new_y = -new_y

        return new_x, new_y

    def get_coords_float(self) -> tuple[float, float]:
        return float(self.x), float(self.y)

    def get_coords_inverted_float(self, invert_x: bool = False, invert_y: bool = False) -> tuple[float, float]:
        new_x: Decimal = self.x
        new_y: Decimal = self.y
        if invert_x:
            new_x = -new_x
        if invert_y:
            new_y = -new_y

        return float(new_x), float(new_y)
