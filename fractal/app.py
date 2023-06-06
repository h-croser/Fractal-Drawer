import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from tree.node.Point import Point
from util.constants.constants import *
from util.constants.style_constants import *
from tree.node.Node import Node


class Line:
    def __init__(self, point_a: Point, point_b: Point, line_width: float, line_color: list[float]):
        self.point_a: Point = point_a
        self.point_b: Point = point_b
        self.line_width: float = line_width
        self.line_color: list[float] = line_color

    def get_line_coords(self) -> list[tuple[float, float]]:
        return [(self.point_a.x, self.point_a.y), (self.point_b.x, self.point_b.y)]


def generate_fractal_tree(layers: int) -> Node | None:
    if layers <= 0:
        return None
    root_parent = Node()
    root = Node(0.0, 1.0, layer=1)
    root.parent = root_parent
    queue: list[Node] = [root]

    while len(queue) != 0:
        curr: Node = queue.pop(0)
        if curr.layer < layers:
            curr.set_left()
            curr.set_right()
            queue.append(curr.left)
            queue.append(curr.right)

    return root


def render_tree(root: Node):
    if root is None:
        return

    fig: plt.figure = plt.figure(figsize=(FIGURE_SIZE, FIGURE_SIZE), facecolor=BACKGROUND_COLOR)
    ax: plt.axes = fig.add_subplot()
    ax.set_aspect('equal', adjustable='box')

    line_ls: list[Line] = []
    leaf_point_ls: list[Point] = []

    queue: list[Node] = [root]
    while len(queue) != 0:
        node = queue.pop(0)
        line_ls.append(get_line_from_node(node))
        if node.is_leaf():
            leaf_point_ls.append(node.point)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    line_coords_ls: list[list[tuple[float, float]]] = []
    line_widths_ls: list[float] = []
    line_colors_ls: list[list[float]] = []
    for line in line_ls:
        line_coords_ls.append(line.get_line_coords())

        line_widths_ls.append(line.line_width)
        line_colors_ls.append(line.line_color)

    segments = np.array(line_coords_ls)
    line_widths = np.array(line_widths_ls)
    line_colors = np.array(line_colors_ls)

    line_collection: LineCollection = LineCollection(segments, linewidths=line_widths, colors=line_colors)
    ax.add_collection(line_collection)

    leaf_x_ls = np.array([point.x for point in leaf_point_ls])
    leaf_y_ls = np.array([point.y for point in leaf_point_ls])
    plt.plot(leaf_x_ls, leaf_y_ls, marker=LEAF_NODE_STYLE, color=LEAF_NODE_COLOR, linewidth=0.0)

    ax.autoscale()
    ax.axis('off')
    plt.show()


def get_line_from_node(node: Node) -> Line:
    point_a = Point(node.parent.get_x(), node.parent.get_y())
    point_b = Point(node.get_x(), node.get_y())
    line_width = get_line_width(node)
    line_color = get_line_color(node)

    return Line(point_a, point_b, line_width, line_color)


def get_line_width(node: Node) -> float:
    linewidth = 1.0
    if LINEWIDTH_STRAT == "decrease":
        linewidth *= (LAYERS - node.layer + 1)

    return linewidth


def get_line_color(node: Node) -> list[float]:
    branch_color = BRANCH_COLOR
    opacity = 1.0 - (node.layer / (LAYERS + 0.1))
    new_branch_color = branch_color[:-1] + [opacity]

    return new_branch_color


def main():
    root: Node = generate_fractal_tree(layers=LAYERS)
    render_tree(root)


if __name__ == "__main__":
    main()
