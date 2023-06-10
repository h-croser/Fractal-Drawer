def hex_to_rgba(hex_str: str, opacity: float = 1.0) -> list[float]:
    if type(opacity) is not float:
        raise TypeError("opacity must be a float")
    if type(hex_str) is not str:
        raise TypeError("hex must be a string")

    hex_str = hex_str.lstrip('#')
    if (opacity < 0.0) or (opacity > 1.0):
        raise ValueError("opacity must be between 0.0 and 1.0")
    if len(hex_str) != 6:
        raise ValueError("hex must be of length 6 (when ignoring #)")

    # Each set of 2 characters is cast to decimal from base 16, and then divides by 255 to get a value 0 - 1
    rgb = [int(hex_str[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    rgba = rgb + [opacity]

    return rgba
