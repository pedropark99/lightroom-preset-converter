'''Mapping from Lightroom to RawTherapee.'''

LR_TO_RT_MAPPING = {
    "Exposure": {'section': 'Exposure', 'key': 'Compensation'},
    "Contrast": {'section': 'Exposure', 'key': "Contrast"},
    "Highlights": {'section': 'ToneEqualizer', 'key': "Band3"},
    "Shadows": {'section': 'ToneEqualizer', 'key': "Band1"},
    "Whites": {'section': 'ToneEqualizer', 'key': "Band4"},
    "Blacks": {'section': 'ToneEqualizer', 'key': "Band0"},
    "Temperature": {'section': 'White Balance', 'key': 'Temperature'},
    'Tint': {'section': 'White Balance', 'key': 'Green'},
    "Texture": {},
    "Clarity": {},
    "Dehaze": {'section': 'Dehaze', 'key': 'Strength'},
    "Vibrance": {'section': 'Vibrance', 'key': 'Pastels'},
    "Saturation": {'section': 'Exposure', 'key': 'Saturation'},
    # When ParametricShadows, etc.. are setted they affect the parametric Curve at Exposure Section
    # In RT, the curve in Exposure section is defined by the "Curve" element in PP3 files.
    # Curve=2;0.25;0.5;0.75;33;18;-20;42;
    "ParametricShadows": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricDarks": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricLights": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricHighlights": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricShadowSplit": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricMidtoneSplit": {'section': 'Exposure', 'key': 'Curve'},
    "ParametricHighlightSplit": {'section': 'Exposure', 'key': 'Curve'},
    # Sharpness tool in Lightroom goes from 0 to 150
    "Sharpness": {'section': 'Sharpening', 'key': 'Amount'},
    "SharpenRadius": {'section': 'Sharpening', 'key': 'Radius'},
    "SharpenDetail": {},
    "SharpenEdgeMasking": {},
    "LuminanceSmoothing": {'section': 'Directional Pyramid Denoising', 'key': 'Luma'},
    "LuminanceNoiseReductionDetail": {'section': 'Directional Pyramid Denoising', 'key': 'Ldetail'},
    "HueAdjustmentRed": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentOrange": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentYellow": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentGreen": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentAqua": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentBlue": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentPurple": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "HueAdjustmentMagenta": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentRed": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentOrange": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentYellow": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentGreen": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentAqua": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentBlue": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentPurple": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "SaturationAdjustmentMagenta": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentRed": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentOrange": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentYellow": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentGreen": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentAqua": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentBlue": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentPurple": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    "LuminanceAdjustmentMagenta": {'section': 'HSV Equalizer', 'key': 'HCurve'},
    'ToneCurvePV': {},
    'ToneCurvePVRed': {'section': 'ColorToning', 'key': 'Redlow'},
    'ToneCurvePVGreen': {'section': 'ColorToning', 'key': 'Greenlow'},
    'ToneCurvePVBlue': {'section': 'ColorToning', 'key': 'Bluelow'},
    "GrainAmount": {},
    "GrainSize": {},
    "GrainFrequency": {}
}

def empty_dict(d: dict) -> bool:
    if len(d.keys()) == 0:
        return True
    return False

NOT_SUPPORTED_FEATURES = list()
for key, value in LR_TO_RT_MAPPING.items():
    if empty_dict(value):
        NOT_SUPPORTED_FEATURES.append(key)



# This is a list of LR parameters that can be
# directly translated into RT parameters by
# simply scaling their values
LR_TO_RT_PARAMETERS_FOR_DIRECT_CONVERSION = [
    "Exposure",
    "Contrast",
    "Highlights",
    "Shadows",
    "Whites",
    "Blacks",
    "Dehaze",
    "Vibrance",
    "Saturation",
    "Sharpness",
    "SharpenRadius",
    "LuminanceSmoothing",
    "LuminanceNoiseReductionDetail"
]