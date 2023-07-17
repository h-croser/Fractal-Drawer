from fractal.view.util.color.Color import Color, build_color_from_list


class ColorGradient:
    def __init__(self, start_color: Color, end_color: Color, layers: int):
        if layers < 0:
            raise ValueError("num_increments must be 0 or greater")

        self.gradient_map: dict[int, Color] = dict()
        if layers == 0:
            return
        if layers == 1:
            self.gradient_map[1] = start_color
            return

        base_vals: list[float] = start_color.get_color_list()
        end_vals: list[float] = end_color.get_color_list()
        diffs: list[float] = [(end_vals[i] - base_vals[i]) for i in range(len(base_vals))]
        portion_of_diff: float = 1.0
        # The last layer has half of the total nodes, and so is assigned the end color with a difference of 50% to the next color
        for layer in range(layers, 0, -1):
            new_color_ls: list[float] = []
            for i in range(len(base_vals)):
                new_color_ls.append(base_vals[i] + (diffs[i] * portion_of_diff))
            self.gradient_map[layer] = build_color_from_list(new_color_ls)
            portion_of_diff *= 0.5

    def get_layer_color(self, layer: int) -> Color:
        return self.gradient_map[layer]
