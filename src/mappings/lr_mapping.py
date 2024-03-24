'''Lookup tables with informations about Lightroom parameters'''
from typing import Tuple, Any, Dict
from .lr_to_rt_mapping import LR_TO_RT_MAPPING
from .rt_mapping import rt_parameter_scale, RawTherapeeValue
from utils.scale import value_as_percentage, scaled_value


class LightRoomValue:
    '''Class to represent a value created by Lightroom'''
    def __init__(self, name: str, value: Any, scale: Tuple[float, float]) -> None:
        self.name = name
        self.value = value
        self.scale = scale

    def corresponding_rt_parameter(self) -> Dict[Any, Any]:
        try:
            return LR_TO_RT_MAPPING[self.name]
        except:
            return None

    def as_rt_value(self):
        rt_map = self.corresponding_rt_parameter()
        rt_scale = rt_parameter_scale(rt_map['key'], rt_map['section'])
        lr_scaled_value = value_as_percentage(self.value, self.scale)
        rt_scaled_value = scaled_value(lr_scaled_value, rt_scale)
        return RawTherapeeValue(rt_map, rt_scaled_value, rt_scale)


def lr_parameter_scale(parameter_name: str) -> Tuple[int, int]:
    return LR_PARAMETERS_SCALE[parameter_name]

LR_PARAMETERS_SCALE = {
    'Exposure': (-5, 5),
    'Contrast': (-100, 100),
    'Highlights': (-100, 100),
    'Blacks': (-100, 100),
    'Whites': (-100, 100),
    'Shadows': (-100, 100),
    'Temperature': (2000, 50000),
    'Tint': (-150, 150),
    "ParametricShadows": (-100, 100),
    "ParametricDarks": (-100, 100),
    "ParametricLights": (-100, 100),
    "ParametricHighlights": (-100, 100),
    "ParametricShadowSplit": (0, 100),
    "ParametricMidtoneSplit": (0, 100),
    "ParametricHighlightSplit": (0, 100),
    'Vibrance': (-100, 100),
    'Saturation': (-100, 100),
    'Dehaze': (-100, 100),
    'Sharpness': (0, 150),
    'SharpenRadius': (0.5, 3),
    'SharpenDetail': (0, 100),
    'SharpenEdgeMasking': (0, 100),
    'LuminanceSmoothing': (0, 100),
    'LuminanceNoiseReductionDetail': (0, 100),
    "HueAdjustmentRed": (-100, 100),
    "HueAdjustmentOrange": (-100, 100),
    "HueAdjustmentYellow": (-100, 100),
    "HueAdjustmentGreen": (-100, 100),
    "HueAdjustmentAqua": (-100, 100),
    "HueAdjustmentBlue": (-100, 100),
    "HueAdjustmentPurple": (-100, 100),
    "HueAdjustmentMagenta": (-100, 100),
    "SaturationAdjustmentRed": (-100, 100),
    "SaturationAdjustmentOrange": (-100, 100),
    "SaturationAdjustmentYellow": (-100, 100),
    "SaturationAdjustmentGreen": (-100, 100),
    "SaturationAdjustmentAqua": (-100, 100),
    "SaturationAdjustmentBlue": (-100, 100),
    "SaturationAdjustmentPurple": (-100, 100),
    "SaturationAdjustmentMagenta": (-100, 100),
    "LuminanceAdjustmentRed": (-100, 100),
    "LuminanceAdjustmentOrange": (-100, 100),
    "LuminanceAdjustmentYellow": (-100, 100),
    "LuminanceAdjustmentGreen": (-100, 100),
    "LuminanceAdjustmentAqua": (-100, 100),
    "LuminanceAdjustmentBlue": (-100, 100),
    "LuminanceAdjustmentPurple": (-100, 100),
    "LuminanceAdjustmentMagenta": (-100, 100)
}




LR_PARAMETRIC_CURVE_PARAMETERS = [
    "ParametricShadows",
    "ParametricDarks",
    "ParametricLights",
    "ParametricHighlights",
    "ParametricShadowSplit",
    "ParametricMidtoneSplit",
    "ParametricHighlightSplit"
]


LR_HSL_ADJUSTMENT_PARAMETERS = [
    "HueAdjustmentRed",
    "HueAdjustmentOrange",
    "HueAdjustmentYellow",
    "HueAdjustmentGreen",
    "HueAdjustmentAqua",
    "HueAdjustmentBlue",
    "HueAdjustmentPurple",
    "HueAdjustmentMagenta",
    "SaturationAdjustmentRed",
    "SaturationAdjustmentOrange",
    "SaturationAdjustmentYellow",
    "SaturationAdjustmentGreen",
    "SaturationAdjustmentAqua",
    "SaturationAdjustmentBlue",
    "SaturationAdjustmentPurple",
    "SaturationAdjustmentMagenta",
    "LuminanceAdjustmentRed",
    "LuminanceAdjustmentOrange",
    "LuminanceAdjustmentYellow",
    "LuminanceAdjustmentGreen",
    "LuminanceAdjustmentAqua",
    "LuminanceAdjustmentBlue",
    "LuminanceAdjustmentPurple",
    "LuminanceAdjustmentMagenta",
]