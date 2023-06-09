from math import radians
from random import random, randrange, randint

from model.tree.Tree import Tree
from util.constants.constants import MAX_LAYERS


class FractalModel:
    def __init__(self):
        # Set initial values
        rand_radians: float = radians(randint(0, 181))
        rand_layers: int = randrange(0, MAX_LAYERS)
        self.radians_offset: float = rand_radians
        self.layers: int = rand_layers

        self.tree: Tree = Tree()

        self.model_outdated: bool = True

    def generate_fractal_tree(self):
        if self.model_outdated:
            self.model_outdated = False
            self.tree.generate_fractal_tree(self.radians_offset, self.layers)

    def set_radians_offset(self, radians_offset: float):
        if self.radians_offset != radians_offset:
            self.radians_offset = radians_offset
            self.model_outdated = True

    def get_radians_offset(self) -> float:
        return self.radians_offset

    def set_layers(self, layers: int):
        if self.layers != layers:
            self.layers = layers
            self.model_outdated = True

    def get_layers(self) -> int:
        return self.layers

    def get_tree(self) -> Tree:
        return self.tree
