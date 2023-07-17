from math import radians, degrees
from typing import Callable

import numpy as np
from matplotlib.axes import Axes
from matplotlib.widgets import Slider

from fractal.util.constants.style_constants import *


class AngleSliderWidget(Slider):
    def __init__(self, ax: Axes, label: str, radians_offset_setter: Callable, radians_offset_getter: Callable):
        text_color_ls: list[float] = TEXT_COLOR.get_color_list()
        handle_style = {'facecolor': SLIDER_HANDLE_COLOR.get_color_list(), 'edgecolor': '1.0', 'edgewidth': '0.8', 'size': 18}
        super().__init__(ax, label, valmin=0.0, valmax=180.0, valinit=degrees(radians_offset_getter()), valstep=0.1, initcolor='none',
                         handle_style=handle_style, track_color=SLIDER_TRACK_COLOR.get_color_list(), color=SLIDER_TRACK_COLOR.get_color_list())
        self.label.set_color(text_color_ls)
        self.valtext.set_color(text_color_ls)
        self.on_changed(self.take_input)

        ax.set_axis_on()
        ax.xaxis.set_visible(True)
        ax.yaxis.set_visible(False)
        ax.set_xticks(np.arange(self.valmin, self.valmax+0.1, 20.0))
        ax.set_facecolor(FIGURE_BACKGROUND_COLOR.get_color_list())
        ax.tick_params(axis='x', colors=text_color_ls)
        ax.spines['bottom'].set_color(text_color_ls)
        ax.spines['top'].set(linewidth=0.0)
        ax.spines['left'].set(linewidth=0.0)
        ax.spines['right'].set(linewidth=0.0)

        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter

    def take_input(self, angle_val: float):
        if type(angle_val) is not float:
            raise TypeError("angle_val must be a float")
        # Round to one decimal place to avoid floating point errors
        rounded_angle: float = round(angle_val, 1)
        # Set text representation manually to avoid a bug with off by 0.1
        self.valtext.set_text(str(rounded_angle))
        radians_offset: float = radians(angle_val % 180)
        self.radians_offset_setter(radians_offset)
