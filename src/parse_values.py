from read_xmp import read_xmp, XMP_EXAMPLES, get_description
from typing import Union, Any, Tuple

def parse_int(input: Union[str, int]) -> int:
    if isinstance(input, int):
        return input
    
    input = input.replace('+', '')
    return int(input)

def parse_float(input: Union[str, float]):
    if isinstance(input, float):
        return input
    
    input = input.replace('+', '')
    return float(input)


class LightRoomValue:
    '''Class to represent a value created by Lightroom'''
    def __init__(self, value: Any, scale: Tuple[float, float]) -> None:
        value = value
        scale = scale


xmp = read_xmp(XMP_EXAMPLES[3])
data = get_description(xmp)
print(data)