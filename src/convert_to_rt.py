from typing import Dict, Any, Union
import re
import toml

from read_xmp import parse_xmp, XMP_EXAMPLES
from mappings.rt_mapping import RawTherapeeValue, RT_PARAMETERS_SCALE
from utils.scale import value_as_percentage, scaled_value
from mappings.lr_to_rt_mapping import LR_TO_RT_PARAMETERS_FOR_DIRECT_CONVERSION
from mappings.lr_mapping import (
    LightRoomValue,
    LR_PARAMETRIC_CURVE_PARAMETERS,
    LR_HSL_ADJUSTMENT_PARAMETERS,
    LR_TONE_CURVES_PARAMETERS
)


class LRToRTParameters:
    '''Class to hold the LR and RT parameters during the conversion.'''
    def __init__(self, lr_parameters: Dict[str, LightRoomValue]) -> None:
        self.lr = lr_parameters
        self.rt = dict()




def convert_to_rt(path: str, print_result: bool = False):
    xmp = parse_xmp(path)
    lr_to_rt = LRToRTParameters(xmp)
    lr_to_rt = rt_convert_direct_parameters(lr_to_rt)
    lr_to_rt = rt_enable_used_sections(lr_to_rt)
    lr_to_rt = rt_parse_white_balance_values(lr_to_rt)
    lr_to_rt = rt_convert_tone_curves(lr_to_rt)
    lr_to_rt = rt_convert_parametric_curve(lr_to_rt)
    lr_to_rt = rt_convert_hsv_curve(lr_to_rt)
    if print_result:
        print(lr_to_rt.rt)

    return lr_to_rt.rt



def rt_enable_used_sections(parameters: LRToRTParameters):
    for lr_key, lr_value in parameters.lr.items():
        if lr_key.startswith('ToneCurve'):
            continue
        rt_parameter = lr_value.corresponding_rt_parameter()
        rt_section = rt_parameter['section']
        rt_enabled_key = rt_section + ':Enabled'
        if rt_enabled_key not in parameters.rt.keys():
            parameters.rt[rt_section + ':Enabled'] = 'true'

    if 'White Balance:Enabled' in parameters.rt.keys():
        if 'White Balance:Setting' not in parameters.rt.keys():
            parameters.rt['White Balance:Setting'] = 'Custom'

    return parameters



def rt_parse_white_balance_values(parameters: LRToRTParameters):
    '''Parse LightRoom White Balance values into their equivalents in RawTherapee.
    
    The White Balance controls from RawTherapee (RT) are slightly different than in LightRoom (LR).
    Specially in the color tint slider. In RT, the color tint slider goes from Magenta to Green.
    While in LR, the slider goes from Green to Magenta.

    Also, in LR, the slider is balanced, meaning that the middle between
    Green and Magenta is precisely at the middle of the scale (at 0).
    While in RT, the middle between Green and Magenta is at 1, and also,
    the scale is a lot bigger on the "green side", than it is on the
    "magenta side", making it a very unbalanced scale.

    Also, in RT, we have the Blue/Red slider control in
    the White Balance section. But LR does not have such
    control. As a result, looks like the photos in RT
    are always a little bit more red than in LR.

    As a result, for a more precise conversion, by default, we
    set this slider in RawTherapee to 0.950, which is 0.05 points less
    than the default value for this slider.
    '''
    if 'White Balance:Enabled' not in parameters.rt.keys():
        parameters.rt['White Balance:Enabled'] = 'true'
        parameters.rt['White Balance:Setting'] = 'Custom'

    if 'Temperature' in parameters.lr.keys():
        lr_temp_value = parameters.lr['Temperature']
        rt_map = lr_temp_value.corresponding_rt_parameter()
        rt_scale = RT_PARAMETERS_SCALE['White Balance:Temperature']
        parameters.rt['White Balance:Temperature'] = RawTherapeeValue(
            rt_map,
            lr_temp_value.value,
            rt_scale
        )

    if 'Tint' in parameters.lr.keys():
        lr_value = parameters.lr['Tint'].value
        if lr_value < 0:
            # More to the Green side
            scale = (1, 12)
            lr_value = abs(lr_value)
            rt_value = scaled_value(lr_value / 100, scale)
        else:
            # More to the Magenta side
            scale = (0, 1)
            lr_value = abs(lr_value)
            rt_value = scaled_value(lr_value / 100, scale)
            rt_value = 1 - rt_value
        
        parameters.rt['White Balance:Green'] = rt_value

    parameters.rt['White Balance:Equal'] = 0.950
    return parameters





def rt_convert_direct_parameters(parameters: LRToRTParameters):
    for lr_key, lr_value in parameters.lr.items():
        if lr_key in LR_TO_RT_PARAMETERS_FOR_DIRECT_CONVERSION:
            rt_parameter = lr_value.corresponding_rt_parameter()
            rt_parameter_key = f"{rt_parameter['section']}:{rt_parameter['key']}"
            parameters.rt[rt_parameter_key] = lr_value.as_rt_value()

    return parameters


def rt_convert_parametric_curve(parameters: LRToRTParameters):
    rt_curve_parameter_key = 'Exposure:Curve'
    if rt_curve_parameter_key in parameters.rt.keys():
        rt_curve_parameter_key = 'Exposure:Curve2'
    
    defaults = {
        "ParametricShadows": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0, (-100, 100)),
        "ParametricDarks": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0, (-100, 100)),
        "ParametricLights": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0, (-100, 100)),
        "ParametricHighlights": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0, (-100, 100)),
        "ParametricShadowSplit": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0.25, (0, 1)),
        "ParametricMidtoneSplit": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0.5, (0, 1)),
        "ParametricHighlightSplit": RawTherapeeValue({'section': 'Exposure', 'key': 'Curve'}, 0.75, (0, 1)),
    }

    for key in LR_PARAMETRIC_CURVE_PARAMETERS:
        if key in parameters.lr.keys():
            lr_parameter = parameters.lr[key]
            lr_value_as_percentage = value_as_percentage(lr_parameter.value, lr_parameter.scale)
            defaults[key].from_percentage(lr_value_as_percentage)
    
    # Formatting the curve values as following:
    # Curve=2;0.25;0.5;0.75;16;-12;15;-32;
    curve = [
        2,
        defaults['ParametricShadowSplit'].value,
        defaults['ParametricMidtoneSplit'].value,
        defaults['ParametricHighlightSplit'].value,
        defaults['ParametricHighlights'].value,
        defaults['ParametricLights'].value,
        defaults['ParametricDarks'].value,
        defaults['ParametricShadows'].value
    ]
    curve = ';'.join([str(i) for i in curve])
    parameters.rt[rt_curve_parameter_key] = curve
    return parameters




def rt_convert_hsv_curve(parameters: LRToRTParameters):
    '''Convert LR Hue Adjustments into an RT HSV Curve.
    
    In RawTherapee, each curve in the HSV Equalizer is composed by 6 points.
    Each point is described in PP3 files by a set of 4 values: 1) x coordinate
    of the point; 2) y coordinate of the point, which represents the amount of adjustment; 3) the strength of the
    transition curve (almost like an "angle value") between the current
    point and the point in the left; 2) another strength of the
    transition curve, but this time, from the current point to
    the point in the right.
    
    This function takes the LightRoom adjustments in HSL color space,
    and transform this adjustments into RawTherapee HSV Curves.
    '''
    hsv_toml = {'section': 'HSV Equalizer', 'key': 'HCurve'}
    curve_defaults = {
        'TransitionStrength': RawTherapeeValue(hsv_toml, value = 0.34999999999999998, scale = (0, 1)),
        'RedXCoordinate': RawTherapeeValue(hsv_toml, value = 0, scale = (0, 1)),
        'YellowXCoordinate': RawTherapeeValue(hsv_toml, value = 0.16666666666666666, scale = (0, 1)),
        'GreenXCoordinate': RawTherapeeValue(hsv_toml, value = 0.33333333333333331, scale = (0, 1)),
        'CyanXCoordinate': RawTherapeeValue(hsv_toml, value = 0.5, scale = (0, 1)),
        'PurpleXCoordinate': RawTherapeeValue(hsv_toml, value = 0.66666666666666663, scale = (0, 1)),
        'MagentaXCoordinate': RawTherapeeValue(hsv_toml, value = 0.83333333333333326, scale = (0, 1)),
    }
    # Adding Orange and Blue colors to the mix, because they are present
    # in LightRoom, but are not present by default in RawTherapee
    curve_defaults['OrangeXCoordinate'] = RawTherapeeValue(hsv_toml, value = 0.08333333333333333, scale = (0, 1))
    curve_defaults['BlueXCoordinate'] = RawTherapeeValue(hsv_toml, value = 0.583333333333333315, scale = (0, 1))

    for key in LR_HSL_ADJUSTMENT_PARAMETERS:
        if key in parameters.lr.keys():
            lr_parameter = parameters.lr[key]
            lr_value_as_percentage = value_as_percentage(lr_parameter.value, lr_parameter.scale)
            curve_type = _hsv_curve_type(key)
            color_name = _hsv_color_name(key)
            adjustment_key = curve_type + color_name + 'Adjustment'
            if curve_type == 'Hue':
                scale = (-0.05, 0.05)
                rt_scaled_value = scaled_value(lr_value_as_percentage, scale)
                rt_scaled_value = 0.5 + rt_scaled_value
            else:
                scale = (0, 1)
                rt_scaled_value = scaled_value(lr_value_as_percentage, scale)

            curve_defaults[adjustment_key] = RawTherapeeValue(hsv_toml, value = rt_scaled_value, scale = scale)
        else:
            # Add the default value
            curve_type = _hsv_curve_type(key)
            color_name = _hsv_color_name(key)
            adjustment_key = curve_type + color_name + 'Adjustment'
            curve_defaults[adjustment_key] = RawTherapeeValue(hsv_toml, value = 0.5, scale = (0, 0.15))


    curve = _compile_hsv_curve(curve_defaults)
    parameters.rt['HSV Equalizer:Enabled'] = 'true'
    parameters.rt['HSV Equalizer:HCurve'] = curve[0]
    parameters.rt['HSV Equalizer:SCurve'] = curve[1]
    parameters.rt['HSV Equalizer:VCurve'] = curve[2]
    return parameters

HSV_COLOR_NAMES = [
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Cyan',
    'Blue',
    'Purple',
    'Magenta'
]

def _compile_hsv_curve(curve_data: Dict[Any, Any]):
    transition_strength = curve_data['TransitionStrength'].value

    hcurve = ["1"]
    for color in HSV_COLOR_NAMES:
        color_x_coordinate = curve_data[color + 'XCoordinate'].value
        hue_adjustment = curve_data['Hue' + color + 'Adjustment'].value
        hcurve.append(str(color_x_coordinate))
        hcurve.append(str(hue_adjustment))
        hcurve.append(str(transition_strength))
        hcurve.append(str(transition_strength))
    
    scurve = ["1"]
    for color in HSV_COLOR_NAMES:
        color_x_coordinate = curve_data[color + 'XCoordinate'].value
        saturation_adjustment = curve_data['Saturation' + color + 'Adjustment'].value
        scurve.append(str(color_x_coordinate))
        scurve.append(str(saturation_adjustment))
        scurve.append(str(transition_strength))
        scurve.append(str(transition_strength))

    vcurve = ["1"]
    for color in HSV_COLOR_NAMES:
        color_x_coordinate = curve_data[color + 'XCoordinate'].value
        value_adjustment = curve_data['Value' + color + 'Adjustment'].value
        vcurve.append(str(color_x_coordinate))
        vcurve.append(str(value_adjustment))
        vcurve.append(str(transition_strength))
        vcurve.append(str(transition_strength))

    hsv_curves = list()
    hsv_curves.append(';'.join(hcurve) + ';')
    hsv_curves.append(';'.join(scurve) + ';')
    hsv_curves.append(';'.join(vcurve) + ';')
    return hsv_curves


def _hsv_curve_type(key: str) -> str:
    if 'Hue' in key:
        return 'Hue'
    if 'Saturation' in key:
        return 'Saturation'
    if 'Luminance' in key or 'Value' in key:
        return 'Value'
    
def _hsv_color_name(key: str) -> str:
    color_name_regex = r'Red|Orange|Yellow|Green|Aqua|Blue|Purple|Magenta'
    color_name = re.search(color_name_regex, key).group(0)
    if color_name == 'Aqua':
        color_name = 'Cyan'
    return color_name




def rt_convert_tone_curves(parameters: LRToRTParameters):
    for lr_parameter in LR_TONE_CURVES_PARAMETERS:
        if lr_parameter in parameters.lr.keys():
            lr_values = parameters.lr[lr_parameter]
            for point in lr_values:
                x = point.value['x']
                delta_y = x - point.value['y']
                rt_scaled_value = int(scaled_value(abs(delta_y), (0, 200)))
                if delta_y < 0:
                    rt_scaled_value = 0 - rt_scaled_value
                else:
                    rt_scaled_value = 0 + rt_scaled_value

                rt_curve_name = _rt_tone_curve_name(lr_parameter, x)
                rt_curve_key = 'ColorToning:' + rt_curve_name
                parameters.rt[rt_curve_key] = RawTherapeeValue(rt_curve_key, rt_scaled_value, (-100, 100))

        if 'ColorToning:Enabled' not in parameters.rt.keys():
            parameters.rt['ColorToning:Enabled'] = 'true'

    parameters.rt['ColorToning:Method'] = 'Splitco'
    return parameters


def _rt_tone_curve_name(lr_parameter, x):
    color_name_regex = r'Red|Green|Blue'
    color_name = re.search(color_name_regex, lr_parameter).group(0)
    if x < 0.25:
        region = 'low'
    elif x > 0.25 and x < 0.75:
        region = 'mid'
    else:
        region = 'high'
    return color_name + region










def write_pp3_string(rt_preset_data: Dict[str, Union[str, RawTherapeeValue]]):
    as_pp3_dict = dict()
    for rt_key, rt_value in rt_preset_data.items():
        if isinstance(rt_value, RawTherapeeValue):
            value = rt_value.value
        else:
            value = rt_value
        toml_section = rt_key.split(':')[0]
        toml_key = rt_key.split(':')[1]
        if toml_section not in as_pp3_dict.keys():
            as_pp3_dict[toml_section] = dict()
        as_pp3_dict[toml_section][toml_key] = value

    toml_string = toml.dumps(as_pp3_dict)
    toml_string = re.sub('[\'\"]', '', toml_string)
    toml_string = re.sub(' = ', '=', toml_string)
    return toml_string


a = convert_to_rt(XMP_EXAMPLES[0])
b = write_pp3_string(a)
print(b)