import re
import warnings
import xml.etree.ElementTree as ET
from typing import (
    List,
    Dict,
    Any,
    Tuple,
    Union
)


from mappings.lr_mapping import lr_parameter_scale, LightRoomValue
from mappings.lr_to_rt_mapping import NOT_SUPPORTED_FEATURES, LR_TO_RT_MAPPING
from utils.parsing import parse_float

RDF_NAMESPACE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
CRS_NAMESPACE = '{http://ns.adobe.com/camera-raw-settings/1.0/}'
XMP_EXAMPLES = [
    'assets/lightroom-presets/example-preset1.xmp',
    'assets/lightroom-presets/example-preset2.xmp',
    'assets/lightroom-presets/example-preset3.xmp',
    'assets/lightroom-presets/example-preset4.xmp',
    'assets/lightroom-presets/only-temperature.xmp'
]


def read_xmp(path: str) -> ET:
    tree = ET.parse(path)
    root = tree.getroot()
    return root

def get_description(tree: ET) -> List[Dict[str, Any]]:
    descriptions = list()
    for description in tree.iter(RDF_NAMESPACE + 'Description'):
        attributes = description.attrib
        attributes_without_namespace = dict()
        for key, value in attributes.items():
            key = key.replace(RDF_NAMESPACE, '')
            key = key.replace(CRS_NAMESPACE, '')
            attributes_without_namespace[key] = value
        descriptions.append(attributes_without_namespace)

    return descriptions

def _report_non_supported_feature(key: str, value: str):
    message = f'[WARNING]: The current version of the converter does not support the feature {key}.'
    message = message + f' As consequence, we are ignoring the attribute "{key}={value}" in the original preset .xmp file'
    print(message)



def parse_xmp(path: str):
    xmp = read_xmp(path)
    preset_descriptions = get_description(xmp)
    parsed_preset = dict()
    for description in preset_descriptions:
        for key, value in description.items():
            key = key.replace('2012', '')
            if key in NOT_SUPPORTED_FEATURES:
                _report_non_supported_feature(key, value)
                continue
            if key not in LR_TO_RT_MAPPING.keys():
                continue

            if re.search(r'^[0-9+-.]+$', value):
                parsed_value = parse_float(value)
            else:
                parsed_value = value
            
            try:
                scale = lr_parameter_scale(key)
            except KeyError:
                print(f"[WARNING]: Could not find the LightRoom scale for parameter {key}. Ignoring this parameter...")
                continue

            parsed_preset[key] = LightRoomValue(key, parsed_value, scale)

    return parsed_preset
    

def get_tone_curves(tree: ET):
    tone_curves = list()
    tone_curves_tags = [
        'ToneCurvePV2012',
        'ToneCurvePV2012Red',
        'ToneCurvePV2012Green',
        'ToneCurvePV2012Blue'
    ]
    for tag in tone_curves_tags:
        for curve in tree.iter(CRS_NAMESPACE + tag):
            curve_tag = tag.replace('2012', '')
            print(curve_tag)



xmp = read_xmp(XMP_EXAMPLES[0])
preset_curves = get_tone_curves(xmp)