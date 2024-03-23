'''Mapping from Lightroom to RawTherapee.'''

LR_TO_RT_MAPPING = {
    "Exposure": {'section': 'Exposure', 'key': 'Compensation'},
    "Contrast": {'section': 'Exposure', 'key': "Contrast"},
    "Highlights": {'section': 'ToneEqualizer', 'key': "Band3"},
    "Shadows": {'section': 'ToneEqualizer', 'key': "Band1"},
    "Whites": {'section': 'ToneEqualizer', 'key': "Band4"},
    "Blacks": {'section': 'ToneEqualizer', 'key': "Band0"},
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
    # Method=LabRegions
    "SplitToningShadowHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'},
    "SplitToningShadowSaturation": {},
    "SplitToningHighlightHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'},
    "SplitToningHighlightSaturation": {},
    "ColorGradeMidtoneHue": {'section': 'ColorToning', 'key': 'LabRegionA_1'},
    "ColorGradeMidtoneSat": {},
    "ColorGradeShadowLum": {},
    "ColorGradeMidtoneLum": {},
    "ColorGradeHighlightLum": {},
    "ColorGradeBlending": {},
    "ColorGradeGlobalHue": {},
    "ColorGradeGlobalSat":{},
    "ColorGradeGlobalLum" :{} ,
    "GrainAmount": {},
    "GrainSize": {},
    "GrainFrequency": {},
    "PostCropVignetteAmount" :{},
    "ShadowTint" :{},
    "RedHue" :{},
    "RedSaturation": {},
    "GreenHue": {},
    "GreenSaturation" :{},
    "BlueHue" : {},
    "BlueSaturation": {},
    "OverrideLookVignette": {},
    "ToneCurveName": {},
    "HasSettings": {}
}

def empty_dict(d: dict) -> bool:
    if len(d.keys()) == 0:
        return True
    return False

NOT_SUPPORTED_FEATURES = list()
for key, value in LR_TO_RT_MAPPING.items():
    if empty_dict(value):
        NOT_SUPPORTED_FEATURES.append(key)























RT_PP3_TOML_SECTIONS = {
    "Version": ["AppVersion", "Version"],
    "General": ["ColorLabel", "InTrash"],
    "Exposure": [
        "Auto",
        "Clip",
        "Compensation",
        "Brightness",
        "Contrast",
        "Saturation",
        "Black",
        "HighlightCompr",
        "HighlightComprThreshold",
        "ShadowCompr",
        "HistogramMatching",
        "CurveFromHistogramMatching",
        "ClampOOG",
        "CurveMode",
        "CurveMode2",
        "Curve",
        "Curve2",
    ],
    "HLRecovery": ["Enabled", "Method", "Hlbl", "Hlth"],
    "Retinex": [
        "Enabled",
        "Str",
        "Scal",
        "Iter",
        "Grad",
        "Grads",
        "Gam",
        "Slope",
        "Median",
        "Neigh",
        "Offs",
        "Vart",
        "Limd",
        "highl",
        "skal",
        "complexMethod",
        "RetinexMethod",
        "mapMethod",
        "viewMethod",
        "Retinexcolorspace",
        "Gammaretinex",
        "CDCurve",
        "MAPCurve",
        "CDHCurve",
        "LHCurve",
        "Highlights",
        "HighlightTonalWidth",
        "Shadows",
        "ShadowTonalWidth",
        "Radius",
        "TransmissionCurve",
        "GainTransmissionCurve",
    ],
    "Local Contrast": ["Enabled", "Radius", "Amount", "Darkness", "Lightness"],
    "Channel Mixer": ["Enabled", "Red", "Green", "Blue"],
    "Black & White": [
        "Enabled",
        "Method",
        "Auto",
        "ComplementaryColors",
        "Setting",
        "Filter",
        "MixerRed",
        "MixerOrange",
        "MixerYellow",
        "MixerGreen",
        "MixerCyan",
        "MixerBlue",
        "MixerMagenta",
        "MixerPurple",
        "GammaRed",
        "GammaGreen",
        "GammaBlue",
        "Algorithm",
        "LuminanceCurve",
        "BeforeCurveMode",
        "AfterCurveMode",
        "BeforeCurve",
        "AfterCurve",
    ],
    "Luminance Curve": [
        "Enabled",
        "Brightness",
        "Contrast",
        "Chromaticity",
        "Gamutmunse",
        "RedAndSkinTonesProtection",
        "LCredsk",
        "LCurve",
        "aCurve",
        "bCurve",
        "ccCurve",
        "chCurve",
        "lhCurve",
        "hhCurve",
        "LcCurve",
        "ClCurve",
    ],
    "Sharpening": [
        "Enabled",
        "Contrast",
        "Method",
        "Radius",
        "BlurRadius",
        "Amount",
        "Threshold",
        "OnlyEdges",
        "EdgedetectionRadius",
        "EdgeTolerance",
        "HalocontrolEnabled",
        "HalocontrolAmount",
        "DeconvRadius",
        "DeconvAmount",
        "DeconvDamping",
        "DeconvIterations",
    ],
    "Vibrance": [
        "Enabled",
        "Pastels",
        "Saturated",
        "PSThreshold",
        "ProtectSkins",
        "AvoidColorShift",
        "PastSatTog",
        "SkinTonesCurve",
    ],
    "SharpenEdge": ["Enabled", "Passes", "Strength", "ThreeChannels"],
    "SharpenMicro": ["Enabled", "Matrix", "Strength", "Contrast", "Uniformity"],
    "White Balance": [
        "Enabled",
        "Setting",
        "Temperature",
        "Green",
        "Equal",
        "TemperatureBias",
        "StandardObserver",
        "CompatibilityVersion",
    ],
    "Color appearance": [
        "Enabled",
        "Degree",
        "AutoDegree",
        "Degreeout",
        "AutoDegreeout",
        "Surround",
        "complex",
        "ModelCat",
        "CatCat",
        "Surrsrc",
        "AdaptLum",
        "Badpixsl",
        "Model",
        "Illum",
        "Algorithm",
        "RSTProtection",
        "AdaptScene",
        "AutoAdapscen",
        "YbScene",
        "Autoybscen",
        "SurrSource",
        "Gamut",
        "Tempout",
        "Autotempout",
        "Greenout",
        "Tempsc",
        "Greensc",
        "Ybout",
        "Datacie",
        "Tonecie",
        "CurveMode",
        "CurveMode2",
        "CurveMode3",
        "Curve",
        "Curve2",
        "Curve3",
    ],
    "Impulse Denoising": ["Enabled", "Threshold"],
    "Defringing": ["Enabled", "Radius", "Threshold", "HueCurve"],
    "Dehaze": ["Enabled", "Strength", "ShowDepthMap", "Depth", "Saturation"],
    "Directional Pyramid Denoising": [
        "Enabled",
        "Enhance",
        "Median",
        "Luma",
        "Ldetail",
        "Chroma",
        "Method",
        "LMethod",
        "CMethod",
        "C2Method",
        "SMethod",
        "MedMethod",
        "RGBMethod",
        "MethodMed",
        "Redchro",
        "Bluechro",
        "AutoGain",
        "Gamma",
        "Passes",
        "LCurve",
        "CCCurve",
    ],
    "EPD": [
        "Enabled",
        "Strength",
        "Gamma",
        "EdgeStopping",
        "Scale",
        "ReweightingIterates",
    ],
    "FattalToneMapping": ["Enabled", "Threshold", "Amount", "Anchor"],
    "Shadows & Highlights": [
        "Enabled",
        "Highlights",
        "HighlightTonalWidth",
        "Shadows",
        "ShadowTonalWidth",
        "Radius",
        "Lab",
    ],
    "ToneEqualizer": [
        "Enabled",
        "Band0",
        "Band1",
        "Band2",
        "Band3",
        "Band4",
        "Regularization",
        "Pivot",
    ],
    "Crop": [
        "Enabled",
        "X",
        "Y",
        "W",
        "H",
        "FixedRatio",
        "Ratio",
        "Orientation",
        "Guide",
    ],
    "Coarse Transformation": ["Rotate", "HorizontalFlip", "VerticalFlip"],
    "Common Properties for Transformations": ["Method", "AutoFill"],
    "Rotation": ["Degree"],
    "Distortion": ["Amount"],
    "LensProfile": [
        "LcMode",
        "LCPFile",
        "UseDistortion",
        "UseVignette",
        "UseCA",
        "LFCameraMake",
        "LFCameraModel",
        "LFLens",
    ],
    "Perspective": [
        "Method",
        "Horizontal",
        "Vertical",
        "CameraCropFactor",
        "CameraFocalLength",
        "CameraPitch",
        "CameraRoll",
        "CameraShiftHorizontal",
        "CameraShiftVertical",
        "CameraYaw",
        "ProjectionShiftHorizontal",
        "ProjectionPitch",
        "ProjectionRotate",
        "ProjectionShiftVertical",
        "ProjectionYaw",
        "ControlLineValues",
        "ControlLineTypes",
    ],
    "Gradient": ["Enabled", "Degree", "Feather", "Strength", "CenterX", "CenterY"],
    "Locallab": ["Enabled", "Selspot"],
    "PCVignette": ["Enabled", "Strength", "Feather", "Roundness"],
    "CACorrection": ["Red", "Blue"],
    "Vignetting Correction": ["Amount", "Radius", "Strength", "CenterX", "CenterY"],
    "Resize": [
        "Enabled",
        "Scale",
        "AppliesTo",
        "Method",
        "DataSpecified",
        "Width",
        "Height",
        "LongEdge",
        "ShortEdge",
        "AllowUpscaling",
    ],
    "PostDemosaicSharpening": [
        "Enabled",
        "Contrast",
        "AutoContrast",
        "AutoRadius",
        "DeconvRadius",
        "DeconvRadiusOffset",
        "DeconvIterCheck",
        "DeconvIterations",
    ],
    "PostResizeSharpening": [
        "Enabled",
        "Contrast",
        "Method",
        "Radius",
        "Amount",
        "Threshold",
        "OnlyEdges",
        "EdgedetectionRadius",
        "EdgeTolerance",
        "HalocontrolEnabled",
        "HalocontrolAmount",
        "DeconvRadius",
        "DeconvAmount",
        "DeconvDamping",
        "DeconvIterations",
    ],
    "Color Management": [
        "InputProfile",
        "ToneCurve",
        "ApplyLookTable",
        "ApplyBaselineExposureOffset",
        "ApplyHueSatMap",
        "DCPIlluminant",
        "WorkingProfile",
        "WorkingTRC",
        "Will",
        "Wprim",
        "WorkingTRCGamma",
        "WorkingTRCSlope",
        "Redx",
        "Redy",
        "Grex",
        "Grey",
        "Blux",
        "Bluy",
        "LabGridcieALow",
        "LabGridcieBLow",
        "LabGridcieAHigh",
        "LabGridcieBHigh",
        "LabGridcieGx",
        "LabGridcieGy",
        "LabGridcieWx",
        "LabGridcieWy",
        "Preser",
        "Fbw",
        "Gamut",
        "OutputProfile",
        "aIntent",
        "OutputProfileIntent",
        "OutputBPC",
    ],
    "Wavelet": [
        "Enabled",
        "Strength",
        "Balance",
        "Sigmafin",
        "Sigmaton",
        "Sigmacol",
        "Sigmadir",
        "Rangeab",
        "Protab",
        "Iter",
        "MaxLev",
        "TilesMethod",
        "complexMethod",
        "mixMethod",
        "sliMethod",
        "quaMethod",
        "DaubMethod",
        "ChoiceLevMethod",
        "BackMethod",
        "LevMethod",
        "DirMethod",
        "CBgreenhigh",
        "CBgreenmed",
        "CBgreenlow",
        "CBbluehigh",
        "CBbluemed",
        "CBbluelow",
        "Ballum",
        "Sigm",
        "Levden",
        "Thrden",
        "Limden",
        "Balchrom",
        "Chromfine",
        "Chromcoarse",
        "MergeL",
        "MergeC",
        "Softrad",
        "Softradend",
        "Strend",
        "Detend",
        "Thrend",
        "Expcontrast",
        "Expchroma",
        "Expedge",
        "expbl",
        "Expresid",
        "Expfinal",
        "Exptoning",
        "Expnoise",
        "Expclari",
        "LabGridALow",
        "LabGridBLow",
        "LabGridAHigh",
        "LabGridBHigh",
        "Contrast1",
        "Contrast2",
        "Contrast3",
        "Contrast4",
        "Contrast5",
        "Contrast6",
        "Contrast7",
        "Contrast8",
        "Contrast9",
        "Chroma1",
        "Chroma2",
        "Chroma3",
        "Chroma4",
        "Chroma5",
        "Chroma6",
        "Chroma7",
        "Chroma8",
        "Chroma9",
        "ContExtra",
        "HSMethod",
        "HLRange",
        "SHRange",
        "Edgcont",
        "Level0noise",
        "Level1noise",
        "Level2noise",
        "Level3noise",
        "Leveldenoise",
        "Levelsigm",
        "ThresholdHighlight",
        "ThresholdShadow",
        "Edgedetect",
        "Edgedetectthr",
        "EdgedetectthrHi",
        "Edgesensi",
        "Edgeampli",
        "ThresholdChroma",
        "CHromaMethod",
        "Medgreinf",
        "Ushamethod",
        "CHSLromaMethod",
        "EDMethod",
        "NPMethod",
        "BAMethod",
        "TMMethod",
        "ChromaLink",
        "ContrastCurve",
        "blcurve",
        "Pastlev",
        "Satlev",
        "OpacityCurveRG",
        "OpacityCurveBY",
        "wavdenoise",
        "wavdenoiseh",
        "OpacityCurveW",
        "OpacityCurveWL",
        "HHcurve",
        "Wavguidcurve",
        "Wavhuecurve",
        "CHcurve",
        "WavclCurve",
        "Median",
        "Medianlev",
        "Linkedg",
        "CBenab",
        "Lipst",
        "Skinprotect",
        "chrwav",
        "bluwav",
        "Hueskin",
        "Edgrad",
        "Edgeffect",
        "Edgval",
        "ThrEdg",
        "AvoidColorShift",
        "Showmask",
        "Oldsh",
        "TMr",
        "Sigma",
        "Offset",
        "Lowthr",
        "ResidualcontShadow",
        "ResidualcontHighlight",
        "ThresholdResidShadow",
        "ThresholdResidHighLight",
        "Residualradius",
        "Residualchroma",
        "Residualblur",
        "Residualblurc",
        "ResidualTM",
        "ResidualEDGS",
        "ResidualSCALE",
        "Residualgamma",
        "HueRangeResidual",
        "HueRange",
        "Contrast",
    ],
    "Spot removal": ["Enabled"],
    "Directional Pyramid Equalizer": [
        "Enabled",
        "Gamutlab",
        "cbdlMethod",
        "Mult0",
        "Mult1",
        "Mult2",
        "Mult3",
        "Mult4",
        "Mult5",
        "Threshold",
        "Skinprotect",
        "Hueskin",
    ],
    "HSV Equalizer": ["Enabled", "HCurve", "SCurve", "VCurve"],
    "SoftLight": ["Enabled", "Strength"],
    "Film Simulation": ["Enabled", "ClutFilename", "Strength"],
    "RGB Curves": ["Enabled", "LumaMode", "rCurve", "gCurve", "bCurve"],
    "ColorToning": [
        "Enabled",
        "Method",
        "Lumamode",
        "Twocolor",
        "Redlow",
        "Greenlow",
        "Bluelow",
        "Satlow",
        "Balance",
        "Sathigh",
        "Redmed",
        "Greenmed",
        "Bluemed",
        "Redhigh",
        "Greenhigh",
        "Bluehigh",
        "Autosat",
        "OpacityCurve",
        "ColorCurve",
        "SatProtectionThreshold",
        "SaturatedOpacity",
        "Strength",
        "HighlightsColorSaturation",
        "ShadowsColorSaturation",
        "ClCurve",
        "Cl2Curve",
        "LabGridALow",
        "LabGridBLow",
        "LabGridAHigh",
        "LabGridBHigh",
        "LabRegionsShowMask",
    ],
    "RAW": [
        "DarkFrame",
        "DarkFrameAuto",
        "FlatFieldFile",
        "FlatFieldAutoSelect",
        "FlatFieldFromMetaData",
        "FlatFieldBlurRadius",
        "FlatFieldBlurType",
        "FlatFieldAutoClipControl",
        "FlatFieldClipControl",
        "CA",
        "CAAvoidColourshift",
        "CAAutoIterations",
        "CARed",
        "CABlue",
        "HotPixelFilter",
        "DeadPixelFilter",
        "HotDeadPixelThresh",
        "PreExposure",
    ],
    "RAW Bayer": [
        "Method",
        "Border",
        "ImageNum",
        "CcSteps",
        "PreBlack0",
        "PreBlack1",
        "PreBlack2",
        "PreBlack3",
        "PreTwoGreen",
        "LineDenoise",
        "LineDenoiseDirection",
        "GreenEqThreshold",
        "DCBIterations",
        "DCBEnhance",
        "LMMSEIterations",
        "DualDemosaicAutoContrast",
        "DualDemosaicContrast",
        "PixelShiftMotionCorrectionMethod",
        "PixelShiftEperIso",
        "PixelShiftSigma",
        "PixelShiftShowMotion",
        "PixelShiftShowMotionMaskOnly",
        "pixelShiftHoleFill",
        "pixelShiftAverage",
        "pixelShiftMedian",
        "pixelShiftGreen",
        "pixelShiftBlur",
        "pixelShiftSmoothFactor",
        "pixelShiftEqualBright",
        "pixelShiftEqualBrightChannel",
        "pixelShiftNonGreenCross",
        "pixelShiftDemosaicMethod",
        "PDAFLinesFilter",
        "Method",
        "DualDemosaicAutoContrast",
        "DualDemosaicContrast",
        "Border",
        "CcSteps",
        "PreBlackRed",
        "PreBlackGreen",
        "PreBlackBlue",
    ],
    "MetaData": ["Mode", "ExifKeys"],
    "Film Negative": [
        "Enabled",
        "RedRatio",
        "GreenExponent",
        "BlueRatio",
        "ColorSpace",
        "RefInput",
        "RefOutput",
    ],
    "RAW Preprocess WB": ["Mode"],
}
