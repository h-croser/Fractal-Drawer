from typing import Callable

import numpy as np
from matplotlib.axes import Axes
from matplotlib.widgets import Slider

from fractal.util.constants.constants import MAX_LAYERS
from fractal.util.constants.style_constants import *


class LayerSliderWidget(Slider):
    def __init__(self, ax: Axes, label: str, layer_setter: Callable, layer_getter: Callable):
        text_color_ls: list[float] = TEXT_COLOR.get_color_list()
        handle_style = {'facecolor': SLIDER_HANDLE_COLOR.get_color_list(), 'edgecolor': '1.0', 'edgewidth': '0.8', 'size': 18}
        super().__init__(ax, label, valmin=0, valmax=MAX_LAYERS, valinit=layer_getter(), valstep=1, initcolor='none',
                         handle_style=handle_style, track_color=SLIDER_TRACK_COLOR.get_color_list(), color=SLIDER_TRACK_COLOR.get_color_list())
        self.label.set_color(text_color_ls)
        self.valtext.set_color(text_color_ls)
        self.on_changed(self.take_input)

        ax.set_axis_on()
        ax.xaxis.set_visible(True)
        ax.yaxis.set_visible(False)
        ax.set_xticks(np.arange(self.valmin, self.valmax+1, 1))
        ax.set_facecolor(FIGURE_BACKGROUND_COLOR.get_color_list())
        ax.tick_params(axis='x', colors=text_color_ls)
        ax.spines['bottom'].set_color(text_color_ls)
        ax.spines['top'].set(linewidth=0.0)
        ax.spines['left'].set(linewidth=0.0)
        ax.spines['right'].set(linewidth=0.0)

        self.layer_setter: Callable = layer_setter
        self.layer_getter: Callable = layer_getter

    def take_input(self, layer_val: int):
        if type(layer_val) is not int:
            raise TypeError("layer_val must be a int")
        self.layer_setter(layer_val)
