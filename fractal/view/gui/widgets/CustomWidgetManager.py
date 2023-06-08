from typing import Callable

from matplotlib import pyplot as plt
from matplotlib.axes import Axes

from view.gui.widgets.AngleOffsetInputWidget import AngleOffsetInputWidget
from view.gui.widgets.AngleSliderWidget import AngleSliderWidget
from view.gui.widgets.LayersInputWidget import LayersInputWidget


class CustomWidgetManager:
    def __init__(self, layer_setter: Callable, layer_getter: Callable, radians_offset_setter: Callable, radians_offset_getter: Callable):
        self.layer_setter: Callable = layer_setter
        self.layer_getter: Callable = layer_getter
        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter

        self.layers_widget: LayersInputWidget = None
        self.angles_widget: AngleOffsetInputWidget = None
        self.angles_slider_widget: AngleSliderWidget = None

    def attach_widgets(self):
        layer_ax: Axes = plt.axes([0.1, 0.1, 0.1, 0.03])
        angle_ax: Axes = plt.axes([0.1, 0.05, 0.1, 0.03])
        angle_slider_ax: Axes = plt.axes([0.3, 0.05, 0.5, 0.03])

        self.layers_widget = LayersInputWidget(layer_ax, "Layers: ", self.layer_setter, self.layer_getter)
        self.angles_widget = AngleOffsetInputWidget(angle_ax, "Angle offset: ", self.radians_offset_setter, self.radians_offset_getter)
        self.angles_slider_widget = AngleSliderWidget(angle_slider_ax, self.radians_offset_setter, self.radians_offset_getter)
