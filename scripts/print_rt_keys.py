

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
    "Saturation": {'section': 'ColorToning', 'key': 'LabRegionSaturation_1'},
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
    "GrainAmount": {},
    "GrainSize": {},
    "GrainFrequency": {},
    # Method=LabRegions
    "SplitToningShadowHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'},
    "SplitToningShadowSaturation": {},
    "SplitToningHighlightHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'},
    "SplitToningHighlightSaturation": {},
    "ColorGradeMidtoneHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'}
}


for value in LR_TO_RT_MAPPING.values():
    if len(value.keys()) == 0:
        continue
    k = value['key']
    print(f"'{k}': (),")