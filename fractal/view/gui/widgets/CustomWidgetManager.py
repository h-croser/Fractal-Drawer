from typing import Callable

from matplotlib import pyplot as plt
from matplotlib.axes import Axes

from view.gui.widgets.AngleSliderWidget import AngleSliderWidget
from view.gui.widgets.LayerSliderWidget import LayerSliderWidget
from view.gui.widgets.MirrorCheckboxWidget import MirrorCheckboxWidget
from view.gui.widgets.DisplayLeafCheckboxWidget import DisplayLeafCheckboxWidget


class CustomWidgetManager:
    def __init__(self,
                 layer_setter: Callable, layer_getter: Callable,
                 radians_offset_setter: Callable, radians_offset_getter: Callable,
                 mirror_setter: Callable, mirror_getter: Callable,
                 display_leaf_setter: Callable, display_leaf_getter: Callable):
        self.layer_setter: Callable = layer_setter
        self.layer_getter: Callable = layer_getter
        self.radians_offset_setter: Callable = radians_offset_setter
        self.radians_offset_getter: Callable = radians_offset_getter
        self.mirror_setter: Callable = mirror_setter
        self.mirror_getter: Callable = mirror_getter
        self.display_leaf_setter: Callable = display_leaf_setter
        self.display_leaf_getter: Callable = display_leaf_getter

        self.layer_slider_widget: LayerSliderWidget = None
        self.angles_slider_widget: AngleSliderWidget = None
        self.mirror_checkbox_widget: MirrorCheckboxWidget = None
        self.display_leaf_checkbox_widget: DisplayLeafCheckboxWidget = None

    def attach_widgets(self):
        layer_slider_ax: Axes = plt.axes([0.2, 0.09, 0.7, 0.03])
        angle_slider_ax: Axes = plt.axes([0.2, 0.03, 0.7, 0.03])
        mirror_checkbox_ax: Axes = plt.axes([0.15, 0.12, 0.06, 0.03])
        display_leaf_ax: Axes = plt.axes([0.15, 0.15, 0.06, 0.03])

        self.layer_slider_widget = LayerSliderWidget(layer_slider_ax, "Layers: ", self.layer_setter, self.layer_getter)
        self.angles_slider_widget = AngleSliderWidget(angle_slider_ax, "Angle offset: ", self.radians_offset_setter, self.radians_offset_getter)
        self.mirror_checkbox_widget = MirrorCheckboxWidget(mirror_checkbox_ax, "Mirror", self.mirror_setter, self.mirror_getter)
        self.display_leaf_checkbox_widget = DisplayLeafCheckboxWidget(display_leaf_ax, "Show leaves", self.display_leaf_setter, self.display_leaf_getter)
