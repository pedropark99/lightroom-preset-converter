from typing import Dict, Any

from read_xmp import parse_xmp, XMP_EXAMPLES
from mappings.lr_to_rt_mapping import LR_TO_RT_PARAMETERS_FOR_DIRECT_CONVERSION
from mappings.lr_mapping import (
    LightRoomValue,
    LR_PARAMETRIC_CURVE_PARAMETERS
)


def convert_to_rt(path: str):
    xmp = parse_xmp(path)
    lr_to_rt = LRToRTParameters(xmp)
    lr_to_rt = rt_convert_direct_parameters(lr_to_rt)
    lr_to_rt = rt_convert_parametric_curve(lr_to_rt)
    return lr_to_rt.rt


class LRToRTParameters:
    '''Class to hold the LR and RT parameters during the conversion.'''
    def __init__(self, lr_parameters: Dict[str, LightRoomValue]) -> None:
        self.lr = lr_parameters
        self.rt = dict()



def rt_convert_direct_parameters(parameters: LRToRTParameters):
    for lr_key, lr_value in parameters.lr.items():
        if lr_key in LR_TO_RT_PARAMETERS_FOR_DIRECT_CONVERSION:
            rt_parameter = lr_value.corresponding_rt_parameter()
            rt_parameter_key = f"{rt_parameter['section']}:{rt_parameter['key']}"
            parameters.rt[rt_parameter_key] = lr_value.as_rt_value()

    return parameters


def rt_convert_parametric_curve(parameters: LRToRTParameters):
    return parameters        


a = convert_to_rt(XMP_EXAMPLES[3])
print(a)