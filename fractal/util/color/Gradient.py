class Gradient:
    @staticmethod
    def get_color_list(start_color: list[float], end_color: list[float], num_increments: int) -> list[list[float]]:
        if len(start_color) != len(end_color):
            raise ValueError("color lists must be the same size")
        if num_increments < 0:
            raise ValueError("num_increments must be 0 or greater")

        if num_increments == 1:
            return [start_color, end_color]
        elif num_increments == 0:
            return [start_color]

        increments: list[float] = [(end_color[i] - start_color[i]) / (num_increments - 1) for i in range(len(start_color))]
        color_list: list[list[float]] = [start_color]
        for multiplier in range(1, num_increments):
            new_color = [start_color[i] + (multiplier * increments[i]) for i in range(len(start_color))]
            color_list.append(new_color)

        return color_list
