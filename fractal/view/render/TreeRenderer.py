import numpy as np
from matplotlib import pyplot as plt

from matplotlib.axes import Axes
from matplotlib.collections import LineCollection

from model.tree.components.Line import Line
from model.tree.components.Node import Node
from model.tree.components.Point import Point
from util.color.Gradient import Gradient
from util.constants.style_constants import LEAF_NODE_STYLE


class TreeRenderer:
    def __init__(self, ax: Axes):
        self.axes: Axes = ax

    def render_tree(self,
                    root: Node,
                    max_layers: int,
                    branch_start_color: list[float],
                    branch_end_color: list[float],
                    leaf_color: list[float],
                    branch_start_width: float,
                    branch_end_width: float,
                    display_leaf: bool,
                    mirrored: bool):
        if type(root) is not Node:
            raise TypeError("root must be a Node")

        line_ls: list[Line] = self._build_line_ls(root, max_layers, branch_start_width, branch_end_width,
                                                  branch_start_color, branch_end_color)

        line_coords_ls: list[list[tuple[float, float]]] = []
        line_widths_ls: list[float] = []
        line_colors_ls: list[list[float]] = []
        for line in line_ls:
            line_coords_ls.append(line.get_line_coords())
            line_widths_ls.append(line.line_width)
            line_colors_ls.append(line.line_color)
            if mirrored:
                line_coords_ls.append(line.get_line_coords_inverted(invert_y=True))
                line_widths_ls.append(line.line_width)
                line_colors_ls.append(line.line_color)


        segments = np.array(line_coords_ls)
        line_widths = np.array(line_widths_ls)
        line_colors = np.array(line_colors_ls)

        line_collection: LineCollection = LineCollection(segments, linewidths=line_widths, colors=line_colors)
        self.axes.add_collection(line_collection)

        if display_leaf:
            leaf_point_ls: list[Point] = self._build_leaf_ls(root, mirrored)
            leaf_x_ls = np.array([point.x for point in leaf_point_ls])
            leaf_y_ls = np.array([point.y for point in leaf_point_ls])

            self.axes.plot(leaf_x_ls, leaf_y_ls, marker=LEAF_NODE_STYLE, color=leaf_color, linewidth=0.0)
        else:
            self.axes.plot()

    def _build_line_ls(self, root: Node,
                       max_layers: int,
                       branch_start_width: float,
                       branch_end_width: float,
                       branch_start_color: list[float],
                       branch_end_color: list[float]) -> list[Line]:
        first_node: Node = root.left
        if first_node is None:
            return []

        line_ls: list[Line] = []

        queue: list[Node] = [first_node]
        while len(queue) != 0:
            node = queue.pop(0)
            line_ls.append(self._get_line_from_node(node, max_layers, branch_start_width, branch_end_width,
                                                    branch_start_color, branch_end_color))

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return line_ls

    def _build_leaf_ls(self, root: Node, mirrored: bool) -> list[Point]:
        leaf_point_ls: list[Point] = []

        queue: list[Node] = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.is_leaf():
                leaf_point_ls.append(node.point)
                if mirrored:
                    mirrored_x, mirrored_y = node.get_line_coords_inverted(invert_y=True)
                    leaf_point_ls.append(Point(mirrored_x, mirrored_y))

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return leaf_point_ls

    def _get_line_from_node(self, node: Node,
                            max_layers: int,
                            branch_start_width: float,
                            branch_end_width: float,
                            branch_start_color: list[float],
                            branch_end_color: list[float]) -> Line:
        point_a = Point(node.parent.get_x(), node.parent.get_y())
        point_b = Point(node.get_x(), node.get_y())
        line_width = self._get_line_width(node, max_layers,  branch_start_width, branch_end_width)
        line_color = self._get_line_color(node, max_layers, branch_start_color, branch_end_color)

        return Line(point_a, point_b, line_width, line_color)

    def _get_line_width(self, node: Node, max_layers: int, branch_start_width: float, branch_end_width: float) -> float:
        if max_layers < 1:
            return branch_start_width
        linewidth_diff: float = branch_end_width - branch_start_width
        linewidth: float = branch_start_width + ((node.layer / max_layers) * linewidth_diff)

        return linewidth

    def _get_line_color(self, node: Node, max_layers: int, branch_start_color: list[float], branch_end_color: list[float]) -> list[float]:
        return Gradient.get_color_list(branch_start_color, branch_end_color, max_layers)[node.layer - 1]
