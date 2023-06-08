from model.FractalModel import FractalModel
from view.FractalViewWrapper import FractalViewWrapper


class FractalController:
    def __init__(self):
        self.model = FractalModel()
        self.view = FractalViewWrapper(self.trigger_render, self.model.set_layers, self.model.get_layers, self.model.set_radians_offset, self.model.get_radians_offset)

    def trigger_render(self):
        self.model.generate_fractal_tree()
        self.view.render(self.model.get_tree())
