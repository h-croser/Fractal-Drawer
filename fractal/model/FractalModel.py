import decimal
from decimal import Decimal
from math import radians
from random import randrange, randint

from fractal.model.tree.Tree import Tree
from fractal.util.constants.constants import MAX_LAYERS


class FractalModel:
    def __init__(self):
        decimal.getcontext().prec = 100

        # Set initial values
        rand_radians: Decimal = Decimal(radians(randint(0, 181)))
        rand_layers: int = randrange(1, MAX_LAYERS//2)
        self.radians_offset: Decimal = rand_radians
        self.layers: int = rand_layers
        self.tree: Tree = Tree()

        self.model_outdated: bool = True

    def generate_fractal_tree(self):
        if self.model_outdated:
            self.model_outdated = False
            self.tree.generate_fractal_tree(self.radians_offset, self.layers)

    def set_radians_offset(self, radians_offset: Decimal | float):
        if type(radians_offset) is float:
            radians_offset = Decimal(radians_offset)
        if self.radians_offset != radians_offset:
            self.radians_offset = radians_offset
            self.model_outdated = True

    def get_radians_offset(self) -> Decimal:
        return self.radians_offset

    def set_layers(self, layers: int):
        if self.layers != layers:
            self.layers = layers
            self.model_outdated = True

    def get_layers(self) -> int:
        return self.layers

    def get_tree(self) -> Tree:
        return self.tree
