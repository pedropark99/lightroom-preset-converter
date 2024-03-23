'''Lookup tables with informations about Lightroom parameters'''
from typing import Tuple

def parameter_scale(parameter_name: str) -> Tuple[int, int]:
    try:
        scale = LR_PARAMETERS_SCALE[parameter_name]
    except KeyError:
        scale = (-100,100)
    return scale

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