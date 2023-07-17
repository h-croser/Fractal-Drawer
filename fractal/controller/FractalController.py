from time import time
from typing import Callable

from fractal.model.FractalModel import FractalModel
from fractal.view.FractalViewWrapper import FractalViewWrapper


class FractalController:
    def __init__(self):
        # Change the following to True to report generation and rendering times
        self.report_time = False

        self.model = FractalModel()
        if self.report_time:
            self.report_elapsed_time("Generating", self.model.generate_fractal_tree)
            self.view = self.report_elapsed_time("Creating view wrapper", FractalViewWrapper, self.trigger_render, self.model.set_layers, self.model.get_layers, self.model.set_radians_offset, self.model.get_radians_offset)
        else:
            self.model.generate_fractal_tree()
            self.view = FractalViewWrapper(self.trigger_render, self.model.set_layers, self.model.get_layers, self.model.set_radians_offset, self.model.get_radians_offset)

    def trigger_render(self):
        if self.report_time:
            self.report_elapsed_time("Generating tree", self.model.generate_fractal_tree)
            self.report_elapsed_time("Rendering tree", self.view.render, self.model.get_tree())
        else:
            self.model.generate_fractal_tree()
            self.view.render(self.model.get_tree())

    def report_elapsed_time(self, label: str, to_time: Callable, *args, **kwargs):
        start = time()
        to_return = to_time(*args, **kwargs)
        end = time()
        duration_seconds = (end - start)
        print(f"{label} duration: {duration_seconds:.3f} s")
        return to_return
