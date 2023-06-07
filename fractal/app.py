import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from view.render.TreeRenderer import TreeRenderer
from tree.Tree import Tree
from util.constants.constants import *
from util.constants.style_constants import *

# def on_click(event, fig):
#     global ANGLE_OFFSET
#     if event.inaxes is not None:
#         ANGLE_OFFSET = event.xdata % 90


def main():
    fig: Figure = plt.figure(figsize=(FIGURE_SIZE, FIGURE_SIZE), facecolor=BACKGROUND_COLOR)

    ax: Axes = fig.add_subplot()
    ax.set_facecolor(BACKGROUND_COLOR)

    tree: Tree = Tree(RADIANS_OFFSET, LAYERS)
    renderer: TreeRenderer = TreeRenderer(tree.get_fractal_tree(), ax)

    renderer.render_tree(inverted=INVERTED)
    plt.show()
    # for i in range(3):
    #     tree.set_num_layers(LAYERS)
    #     tree.set_base_offset_radians(RADIANS_OFFSET)
    #     tree.generate_fractal_tree()
    #     plt.cla()
    #     renderer.render_tree(inverted=INVERTED)


if __name__ == "__main__":
    main()
