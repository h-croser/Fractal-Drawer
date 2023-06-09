from model.tree.components.Point import Point


class Line:
    def __init__(self, point_a: Point, point_b: Point, line_width: float, line_color: list[float]):
        self.point_a: Point = point_a
        self.point_b: Point = point_b
        self.line_width: float = line_width
        self.line_color: list[float] = line_color

    def get_line_coords(self) -> list[tuple[float, float]]:
        return [(self.point_a.x, self.point_a.y), (self.point_b.x, self.point_b.y)]

    def get_line_coords_inverted(self, invert_x: bool = False, invert_y: bool = False) -> list[tuple[float, float]]:
        return [self.point_a.get_coords_inverted(invert_x=invert_x, invert_y=invert_y),
                self.point_b.get_coords_inverted(invert_x=invert_x, invert_y=invert_y)]
