from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import CheckButtons

from util.constants.style_constants import *


class MirrorCheckboxWidget(CheckButtons):
    def __init__(self, ax: Axes, label: str, mirror_setter: Callable, mirror_getter: Callable):
        super().__init__(ax, [label], actives=[mirror_getter()], label_props={'color': [TEXT_COLOR], 'fontsize': ['large']},
                         frame_props={'edgecolors': [TEXT_COLOR], 'facecolors': [TEXT_COLOR]})
        self.mirror_setter: Callable = mirror_setter
        self.on_clicked(self.change_state)

        ax.set_facecolor(FIGURE_BACKGROUND_COLOR)
        ax.spines['bottom'].set(linewidth=0.0)
        ax.spines['top'].set(linewidth=0.0)
        ax.spines['left'].set(linewidth=0.0)
        ax.spines['right'].set(linewidth=0.0)

    def change_state(self, checkbox_label: str):
        state: bool = self.get_status()[0]
        self.mirror_setter(state)
