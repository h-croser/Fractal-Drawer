from math import degrees, radians
from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import Slider


class AngleSliderWidget(Slider):
    def __init__(self, ax: Axes, radians_offset_setter: Callable, radians_offset_getter: Callable):
        super().__init__(ax, '', valmin=0.0, valmax=180.0, valinit=0.0, valstep=0.1, initcolor='none')
        self.label.set_color("white")
        self.on_changed(self.take_input)

        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter

    def take_input(self, angle_val: float):
        if type(angle_val) is not float:
            raise TypeError("angle_val must be a float")
        radians_offset: float = radians(angle_val % 180)
        self.radians_offset_setter(radians_offset)
