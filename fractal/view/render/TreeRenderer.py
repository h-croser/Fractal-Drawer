import numpy as np

from matplotlib.axes import Axes
from matplotlib.collections import LineCollection

from fractal.view.render.Line import Line
from fractal.model.tree.components.Node import Node
from fractal.model.tree.components.Point import Point

from fractal.util.constants.style_constants import LEAF_NODE_STYLE
from fractal.view.util.color.Color import Color, build_color_from_list
from fractal.view.util.color.ColorGradient import ColorGradient


class TreeRenderer:
    def __init__(self, ax: Axes):
        self.ax: Axes = ax

    def render_tree(self, root: Node, max_layers: int, branch_start_color: Color, branch_end_color: Color,
                    leaf_color: Color, branch_start_width: float, branch_end_width: float, display_leaf: bool, mirrored: bool):
        if type(root) is not Node:
            raise TypeError("root must be a Node")

        color_gradient: ColorGradient = ColorGradient(branch_start_color, branch_end_color, max_layers)

        line_ls: list[Line] = self._build_line_ls(root, color_gradient, max_layers, branch_start_width, branch_end_width)

        line_coords_ls: list[list[tuple[float, float]]] = []
        line_widths_ls: list[float] = []
        line_colors_ls: list[list[float]] = []
        for line in line_ls:
            line_coords_ls.append(line.get_line_coords_float())
            line_widths_ls.append(line.line_width)
            line_colors_ls.append(line.line_color.get_color_list())
            if mirrored:
                line_coords_ls.append(line.get_line_coords_inverted_float(invert_y=True))
                line_widths_ls.append(line.line_width)
                line_colors_ls.append(line.line_color.get_color_list())

        segments = np.array(line_coords_ls)
        line_widths = np.array(line_widths_ls)
        line_colors = np.array(line_colors_ls)

        line_collection: LineCollection = LineCollection(segments, linewidths=line_widths, colors=line_colors)
        self.ax.add_collection(line_collection)

        if display_leaf:
            leaf_point_ls: list[Point] = self._build_leaf_ls(root, mirrored)
            leaf_x_ls = np.array([point.x for point in leaf_point_ls])
            leaf_y_ls = np.array([point.y for point in leaf_point_ls])

            self.ax.plot(leaf_x_ls, leaf_y_ls, marker=LEAF_NODE_STYLE, color=leaf_color.get_color_list(), linewidth=0.0)
        else:
            self.ax.plot()

    def _build_line_ls(self, root: Node, color_gradient: ColorGradient, max_layers: int,
                       branch_start_width: float, branch_end_width: float) -> list[Line]:
        first_node: Node = root.left
        if first_node is None:
            return []

        line_ls: list[Line] = []

        queue: list[Node] = [first_node]
        while len(queue) != 0:
            node = queue.pop(0)
            line_ls.append(self._get_line_from_node(node, color_gradient, max_layers, branch_start_width, branch_end_width))

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

    def _get_line_from_node(self, node: Node, color_gradient: ColorGradient, max_layers: int,
                            branch_start_width: float, branch_end_width: float,) -> Line:
        point_a = Point(node.parent.get_x(), node.parent.get_y())
        point_b = Point(node.get_x(), node.get_y())
        line_width = self._get_line_width(node, max_layers,  branch_start_width, branch_end_width)
        line_color = color_gradient.get_layer_color(node.layer)

        return Line(point_a, point_b, line_width, line_color)

    def _get_line_width(self, node: Node, max_layers: int, branch_start_width: float, branch_end_width: float) -> float:
        if max_layers <= 1:
            return branch_start_width
        linewidth_diff: float = branch_end_width - branch_start_width
        linewidth: float = branch_start_width + ((node.layer / max_layers) * linewidth_diff)

        return linewidth
