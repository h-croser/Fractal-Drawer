from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import TextBox


class LineWidthInputWidget(TextBox):
    def __init__(self, ax: Axes, label: str, attribute_setter: Callable, attribute_getter: Callable):
        super().__init__(ax, label, initial=attribute_getter())
        self.on_submit(self.take_input)

        self.attribute_setter: Callable = attribute_setter
        self.attribute_getter: Callable = attribute_getter

    def take_input(self, text: str):
        if not self.is_valid_input(text):
            self.set_val(self.attribute_getter())
            return
        self.attribute_setter(float(text))

    def is_valid_input(self, float_text: str) -> bool:
        if type(float_text) is not str:
            return False
        try:
            return float(float_text) >= 0.0
        except ValueError:
            return False
