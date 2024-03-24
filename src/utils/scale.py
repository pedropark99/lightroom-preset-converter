from typing import Tuple, Union


def scaled_value(percentage: Union[float, int], scale: Tuple[float, float]) -> float:
    smin = scale[0]
    smax = scale[1]
    tmax = (smax + abs(smin))
    scaled_value = percentage * tmax
    return scaled_value - abs(smin)

def value_as_percentage(value: Union[float, int], scale: Tuple[float, float]) -> float:
    smin = scale[0]
    smax = scale[1]
    try:
        p = (value + abs(smin)) / (smax + abs(smin))
        return p
    except ZeroDivisionError:
        return 0.0