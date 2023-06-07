import numpy as np

from matplotlib.axes import Axes
from matplotlib.collections import LineCollection

from tree.components.Line import Line
from tree.components.Node import Node
from tree.components.Point import Point
from util.constants.constants import LINEWIDTH_STRAT, LAYERS
from util.constants.style_constants import LEAF_NODE_STYLE, LEAF_NODE_COLOR, BRANCH_GRADIENT_LIST


class TreeRenderer:
    def __init__(self, root: Node, ax: Axes):
        if type(root) is not Node:
            raise TypeError("root must be a Node")
        self.root: Node = root
        self.axes: Axes = ax

        self.axes.set_aspect('equal', adjustable='box')
        self.axes.autoscale()
        self.axes.axis('off')

    def render_tree(self, inverted=False):
        line_ls: list[Line] = self._build_line_ls()
        leaf_point_ls: list[Point] = self._build_leaf_ls()

        line_coords_ls: list[list[tuple[float, float]]] = []
        line_widths_ls: list[float] = []
        line_colors_ls: list[list[float]] = []
        for line in line_ls:
            line_coords_ls.append(line.get_line_coords())
            if inverted:
                line_coords_ls.append(line.get_inverted_line_y_coords())

            line_widths_ls.append(line.line_width)
            line_colors_ls.append(line.line_color)

        segments = np.array(line_coords_ls)
        line_widths = np.array(line_widths_ls)
        line_colors = np.array(line_colors_ls)

        line_collection: LineCollection = LineCollection(segments, linewidths=line_widths, colors=line_colors)
        self.axes.add_collection(line_collection)

        leaf_x_ls = np.array([point.x for point in leaf_point_ls])
        leaf_y_ls = np.array([point.y for point in leaf_point_ls])

        self.axes.plot(leaf_x_ls, leaf_y_ls, marker=LEAF_NODE_STYLE, color=LEAF_NODE_COLOR, linewidth=0.0)

    def _build_line_ls(self) -> list[Line]:
        first_node: Node = self.root.left
        if first_node is None:
            return []

        line_ls: list[Line] = []

        queue: list[Node] = [first_node]
        while len(queue) != 0:
            node = queue.pop(0)
            line_ls.append(self._get_line_from_node(node))

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return line_ls

    def _build_leaf_ls(self) -> list[Point]:
        leaf_point_ls: list[Point] = []

        queue: list[Node] = [self.root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.is_leaf():
                leaf_point_ls.append(node.point)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return leaf_point_ls

    def _get_line_from_node(self, node: Node) -> Line:
        point_a = Point(node.parent.get_x(), node.parent.get_y())
        point_b = Point(node.get_x(), node.get_y())
        line_width = self._get_line_width(node)
        line_color = self._get_line_color(node)

        return Line(point_a, point_b, line_width, line_color)

    def _get_line_width(self, node: Node) -> float:
        linewidth = 0.5
        if LINEWIDTH_STRAT == "decrease":
            linewidth *= 1 + ((1 - (node.layer - 1)) / LAYERS)
        elif LINEWIDTH_STRAT == "increase":
            linewidth *= 1 + (node.layer / LAYERS)

        return linewidth

    def _get_line_color(self, node: Node) -> list[float]:
        return BRANCH_GRADIENT_LIST[node.layer - 1]
