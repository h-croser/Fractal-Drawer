from typing import Callable

from matplotlib.axes import Axes
from matplotlib.widgets import TextBox


class LayersInputWidget(TextBox):
    def __init__(self, ax: Axes, label: str, layer_setter: Callable, layer_getter: Callable):
        super().__init__(ax, label, initial=layer_getter())
        self.label.set_color("white")
        self.on_submit(self.take_input)

        self.layer_setter: Callable = layer_setter
        self.layer_getter: Callable = layer_getter

    def take_input(self, text: str):
        if self.is_valid_input(text):
            self.layer_setter(int(text))
        else:
            self.set_val(self.layer_getter())

    def is_valid_input(self, int_text: str) -> bool:
        if type(int_text) is not str:
            return False
        try:
            return int(int_text) >= 0
        except ValueError:
            return False
