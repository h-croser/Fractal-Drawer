from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import CheckButtons

from fractal.util.constants.style_constants import *


class DisplayLeafCheckboxWidget(CheckButtons):
    def __init__(self, ax: Axes, label: str, display_leaf_setter: Callable, display_leaf_getter: Callable):
        text_color_ls: list[float] = TEXT_COLOR.get_color_list()
        super().__init__(ax, [label], actives=[display_leaf_getter()], label_props={'color': [text_color_ls], 'fontsize': ['large']},
                         frame_props={'edgecolors': [text_color_ls], 'facecolors': [text_color_ls]})
        self.display_leaf_setter: Callable = display_leaf_setter
        self.on_clicked(self.change_state)

        ax.set_facecolor(FIGURE_BACKGROUND_COLOR.get_color_list())
        ax.spines['bottom'].set(linewidth=0.0)
        ax.spines['top'].set(linewidth=0.0)
        ax.spines['left'].set(linewidth=0.0)
        ax.spines['right'].set(linewidth=0.0)

    def change_state(self, checkbox_label: str):
        state: bool = self.get_status()[0]
        self.display_leaf_setter(state)
