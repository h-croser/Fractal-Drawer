from math import sin, cos

from model.tree.components.Point import Point


class Node:
    def __init__(self, x: float = 0.0, y: float = 0.0, layer: int = 0, radians_offset: float = 0):
        self.point = Point(x, y)
        self.radians_offset = radians_offset
        self.layer = layer
        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None

    def set_x(self, x: float):
        self.point.x = x

    def set_y(self, y: float):
        self.point.y = y

    def get_x(self) -> float:
        return self.point.x

    def get_y(self) -> float:
        return self.point.y

    def get_line_coords_inverted(self, invert_x: bool = False, invert_y: bool = False) -> tuple[float, float]:
        return self.point.get_coords_inverted(invert_x=invert_x, invert_y=invert_y)

    def is_leaf(self) -> bool:
        return (self.left is None) and (self.right is None)

    def set_left(self, offset: float):
        self.left = Node()
        self.left.parent = self
        self.left.layer = self.layer + 1
        radians_offset_change: float = self.radians_offset + offset
        self.left.radians_offset = radians_offset_change
        self.left.set_x(self.get_x() + sin(radians_offset_change))
        self.left.set_y(self.get_y() + cos(radians_offset_change))

    def set_right(self, offset: float):
        self.right = Node()
        self.right.parent = self
        self.right.layer = self.layer + 1
        radians_offset_change: float = self.radians_offset - offset
        self.right.radians_offset = radians_offset_change
        self.right.set_x(self.get_x() + sin(radians_offset_change))
        self.right.set_y(self.get_y() + cos(radians_offset_change))

    def __str__(self) -> str:
        return f"Layer: {self.layer}\t\tx: {self.point.x}, y: {self.point.y}"
