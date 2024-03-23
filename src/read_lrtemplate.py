'''Read LightRoom templates.

This module contains functions that are essential to read
LightRoom template files (.lrtemplate). These files
are read first as plain text files, then, their contents
are translated into JSON files. And this JSON version
of the file is used.
'''
import re
import json
from typing import (
    Dict, Any
)

KEY_IN_KV_PAIR_REGEX = r'(?P<spaces>\s*)(?P<key>[A-Za-z0-9]+) = '
def read_text_file(path: str) -> str:
    with open(path, 'r', encoding="utf-8") as file_connection:
        content = file_connection.read()
    return content


def read_lrtemplate(path: str) -> Dict[Any, Any]:
    template = read_text_file(path)
    template_lines = template.split('\n')
    for i, line in enumerate(template_lines):
        match = re.search(KEY_IN_KV_PAIR_REGEX, line)
        if match:
            key = match['key']
            indent_level = match['spaces']
            as_json_key = str(indent_level) + f'"{key}": '
            template_lines[i] = re.sub(KEY_IN_KV_PAIR_REGEX, as_json_key, line, count = 1)

    template = '\n'.join(template_lines)
    template = fix_objects_into_arrays(template)
    template = '{' + template + '}'
    template_as_json = json.loads(template)
    if 's' in template_as_json.keys():
        return template_as_json['s']
    return template_as_json


def fix_objects_into_arrays(template):
    '''Util function to fix JSON objects that should be JSON arrays.'''
    template = re.sub(r"([0-9]+),(\s*)\}(?!$)", r"\1]", template)
    template = re.sub(r",(\s*)\}", r"}", template)
    template = re.sub(r"\{(\s*)([0-9]+),", r"[\2,", template)
    return template

