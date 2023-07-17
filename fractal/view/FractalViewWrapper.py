from typing import Callable

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure, SubFigure
from matplotlib.gridspec import GridSpec

from fractal.model.tree.Tree import Tree
from fractal.util.constants.constants import FIGURE_SIZE
from fractal.util.constants.style_constants import *
from fractal.view.gui.widgets.CustomWidgetManager import CustomWidgetManager
from fractal.view.render.TreeRenderer import TreeRenderer


class FractalViewWrapper:
    def __init__(self, render_trigger: Callable, layer_setter: Callable, layer_getter: Callable,
                 radians_offset_setter: Callable, radians_offset_getter: Callable):
        self.render_trigger: Callable = render_trigger

        # Set defaults
        self.figure_background_color: Color = FIGURE_BACKGROUND_COLOR
        self.axes_background_color: Color = AXES_BACKGROUND_COLOR
        self.branch_start_color: Color = BRANCH_START_COLOR
        self.branch_end_color: Color = BRANCH_END_COLOR
        self.leaf_color: Color = LEAF_NODE_COLOR

        self.branch_width_start: float = BRANCH_WIDTH_START
        self.branch_width_end: float = BRANCH_WIDTH_END

        self.display_leaf: bool = False
        self.mirrored: bool = False

        # Bind attribute setters
        self.layer_setter: Callable = layer_setter
        self.layer_getter: Callable = layer_getter

        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter

        # Set figure
        self.parent_fig: Figure = plt.figure(figsize=(FIGURE_SIZE, FIGURE_SIZE), facecolor=self.figure_background_color.get_color_list())
        gs: GridSpec = GridSpec(2, 1, height_ratios=[3, 1])
        self.plot_fig: SubFigure = self.parent_fig.add_subfigure(gs[0], facecolor=self.axes_background_color.get_color_list())

        self.ax: Axes = self.plot_fig.add_subplot()
        self.ax.set_anchor('N')
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.autoscale()
        self.ax.set_axis_off()

        self.renderer: TreeRenderer = TreeRenderer(self.ax)

        # Handle widgets
        self.widget_manager: CustomWidgetManager = CustomWidgetManager(self.set_layers, self.layer_getter,
                                                                       self.set_radians_offset, self.radians_offset_getter,
                                                                       self.set_mirror_state, self.get_mirror_state,
                                                                       self.set_display_leaf, self.get_display_leaf)
        self.widget_manager.attach_widgets()

    def render(self, tree: Tree):
        self.ax.set_facecolor(self.axes_background_color.get_color_list())
        self.ax.cla()
        self.renderer.render_tree(tree.get_root(), self.layer_getter(), self.branch_start_color, self.branch_end_color, self.leaf_color,
                                  self.branch_width_start, self.branch_width_end, self.display_leaf, self.mirrored)
        self.ax.set_axis_off()
        plt.show()

    def set_branch_start_width(self, branch_width_start: float):
        self.branch_width_start = branch_width_start

    def set_branch_end_width(self, branch_width_end: float):
        self.branch_width_end = branch_width_end

    def get_branch_start_width(self) -> float:
        return self.branch_width_start

    def get_branch_end_width(self) -> float:
        return self.branch_width_end

    def set_radians_offset(self, radians_offset: float):
        self.radians_offset_setter(radians_offset)
        self.render_trigger()

    def set_layers(self, layers: int):
        self.layer_setter(layers)
        self.render_trigger()

    def set_mirror_state(self, mirror_state: bool):
        self.mirrored = mirror_state
        self.render_trigger()

    def get_mirror_state(self) -> bool:
        return self.mirrored

    def set_display_leaf(self, display_leaf: bool):
        self.display_leaf = display_leaf
        self.render_trigger()

    def get_display_leaf(self) -> bool:
        return self.display_leaf
