from math import radians, degrees
from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import TextBox


class AngleOffsetInputWidget(TextBox):
    def __init__(self, ax: Axes, label: str, radians_offset_setter: Callable, radians_offset_getter: Callable):
        super().__init__(ax, label, initial=str(degrees(radians_offset_getter())))
        self.label.set_color("white")
        self.on_submit(self.take_input)

        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter

    def take_input(self, text: str):
        if self.is_valid_input(text):
            radians_offset: float = radians(float(text) % 180)
            self.radians_offset_setter(radians_offset)
        else:
            self.set_val(str(degrees(self.radians_offset_getter())))

    def is_valid_input(self, float_text: str) -> bool:
        if type(float_text) is not str:
            return False
        try:
            float(float_text)
        except ValueError:
            return False

        return True
