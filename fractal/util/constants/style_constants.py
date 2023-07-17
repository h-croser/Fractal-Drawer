from fractal.view.util.color.Color import Color, build_color_from_hex_str

# Line styles

LEAF_NODE_STYLE: str = '1'
BRANCH_WIDTH_START: float = 0.7
BRANCH_WIDTH_END: float = 0.2

# Colors
FIGURE_BACKGROUND_COLOR: Color = build_color_from_hex_str("#1A1D21", 1.0)
AXES_BACKGROUND_COLOR: Color = build_color_from_hex_str("#121016", 1.0)
LEAF_NODE_COLOR: Color = build_color_from_hex_str("#E2F9B8", 1.0)

BRANCH_START_COLOR: Color = build_color_from_hex_str("#AD343E", 1.0)
BRANCH_END_COLOR: Color = build_color_from_hex_str("#42D9C8", 1.0)

TEXT_COLOR: Color = build_color_from_hex_str("a3814b", 1.0)
SLIDER_TRACK_COLOR: Color = build_color_from_hex_str("fed37d", 1.0)
SLIDER_HANDLE_COLOR: Color = build_color_from_hex_str("691c1d", 1.0)
