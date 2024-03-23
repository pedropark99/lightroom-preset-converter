import xml.etree.ElementTree as ET
from typing import (
    List,Dict,Any
)

RDF_NAMESPACE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
CRS_NAMESPACE = '{http://ns.adobe.com/camera-raw-settings/1.0/}'

def read_xmp(path: str) -> ET:
    tree = ET.parse(path)
    root = tree.getroot()
    return root

root = read_xmp('assets/lightroom-presets/example-preset1.xmp')

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


d = get_description(root)
print(d)