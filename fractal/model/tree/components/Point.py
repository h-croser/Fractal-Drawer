class Point:
    x: float
    y: float
    x: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def get_coords(self) -> tuple[float, float]:
        return self.x, self.y

    def get_coords_inverted(self, invert_x: bool = False, invert_y: bool = False):
        new_x: float = self.x
        new_y: float = self.y
        if invert_x:
            new_x = -new_x
        if invert_y:
            new_y = -new_y

        return new_x, new_y
