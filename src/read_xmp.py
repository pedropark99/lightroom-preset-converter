import re
import warnings
import xml.etree.ElementTree as ET
from typing import (
    List,Dict,Any
)


from parse_values import parse_float, parse_int, LightRoomValue
from lr_mapping import parameter_scale
from lr_to_rt_mapping import NOT_SUPPORTED_FEATURES, LR_TO_RT_MAPPING

RDF_NAMESPACE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
CRS_NAMESPACE = '{http://ns.adobe.com/camera-raw-settings/1.0/}'
XMP_EXAMPLES = [
    'assets/lightroom-presets/example-preset1.xmp',
    'assets/lightroom-presets/example-preset2.xmp',
    'assets/lightroom-presets/example-preset3.xmp',
    'assets/lightroom-presets/example-preset4.xmp'
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
    message = message + f' As consequence, we are ignoring the attribute "{key}={value}" in the original template .xmp file'
    warnings.warn(message)



def parse_xmp(path: str):
    xmp = read_xmp(path)
    template_descriptions = get_description(xmp)
    parsed_template = dict()
    for description in template_descriptions:
        for key, value in description.items():
            if key in NOT_SUPPORTED_FEATURES:
                _report_non_supported_feature(key, value)
                continue
            if key not in LR_TO_RT_MAPPING.keys():
                continue

            if re.search(r'^[0-9+-]+$', value):
                parsed_value = parse_int(value)
            elif re.search(r'^[0-9+-.]+$', value):
                parsed_value = parse_float(value)
            else:
                parsed_value = value
            
            scale = parameter_scale(key)
            parsed_template[key] = LightRoomValue(parsed_value, scale)

    return parsed_template
    


a = parse_xmp(XMP_EXAMPLES[3])
print(a)