
import re
import json

TEMPLATE_KEY_REGEX = r'(?P<spaces>\s*)(?P<key>[A-Za-z0-9]+) = '
def read_text_file(path: str) -> str:
    with open(path, 'r', encoding="utf-8") as file_connection:
        content = file_connection.read()
    return content


def read_lrtemplate(path: str) -> str:
    template = read_text_file(path)
    template_lines = template.split('\n')
    for i, line in enumerate(template_lines):
        match = re.search(TEMPLATE_KEY_REGEX, line)
        if match:
            key = match['key']
            indent_level = match['spaces']
            as_json_key = str(indent_level) + f'"{key}": '
            template_lines[i] = re.sub(TEMPLATE_KEY_REGEX, as_json_key, line, count = 1)

    l = '\n'.join(template_lines)
    l = '{' + l + '}'
    return json.loads(l)

print(read_lrtemplate("assets/example_template.lrtemplate"))