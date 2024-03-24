from typing import Union

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
