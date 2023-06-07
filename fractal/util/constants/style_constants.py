from util.color.Gradient import Gradient
from util.color.color import hex_to_rgba

# Line styles
from util.constants.constants import LAYERS

LEAF_NODE_STYLE: str = '1'

# Colors
BACKGROUND_COLOR: list[float] = hex_to_rgba("#000000", 1.0)
LEAF_NODE_COLOR: list[float] = hex_to_rgba("#E2F9B8", 1.0)

BRANCH_START_COLOR: list[float] = hex_to_rgba("#FFFFFF", 1.0)
BRANCH_END_COLOR: list[float] = hex_to_rgba("#FFFFFF", 1.0)

BRANCH_GRADIENT_LIST: list[list[float]] = Gradient.get_color_list(BRANCH_START_COLOR, BRANCH_END_COLOR, LAYERS)
