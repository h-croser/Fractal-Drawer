from decimal import Decimal

from fractal.model.tree.components.Point import Point
from fractal.view.util.color.Color import Color


class Line:
    def __init__(self, point_a: Point, point_b: Point, line_width: float, line_color: Color):
        self.point_a: Point = point_a
        self.point_b: Point = point_b
        self.line_width: float = line_width
        self.line_color: Color = line_color

    def get_line_coords(self) -> list[tuple[Decimal, Decimal]]:
        return [self.point_a.get_coords(), self.point_b.get_coords()]

    def get_line_coords_inverted(self, invert_x: bool = False, invert_y: bool = False) -> list[tuple[Decimal, Decimal]]:
        return [self.point_a.get_coords_inverted(invert_x=invert_x, invert_y=invert_y),
                self.point_b.get_coords_inverted(invert_x=invert_x, invert_y=invert_y)]

    def get_line_coords_float(self) -> list[tuple[float, float]]:
        return [self.point_a.get_coords_float(), self.point_b.get_coords_float()]

    def get_line_coords_inverted_float(self, invert_x: bool = False, invert_y: bool = False) -> list[tuple[float, float]]:
        return [self.point_a.get_coords_inverted_float(invert_x=invert_x, invert_y=invert_y),
                self.point_b.get_coords_inverted_float(invert_x=invert_x, invert_y=invert_y)]
