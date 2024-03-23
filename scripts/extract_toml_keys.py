import re

TOML_KEY_REGEX = r'^(?P<key>[A-Za-z0-9]+)( )?='
TOML_SECTION_REGEX = r'^\[(?P<key>[A-Za-z0-9& ]+)\]'
PP3_PATH = 'assets/rawtherapee-presets/IMG_7761.JPG.out.pp3'

with open(PP3_PATH, 'r', encoding='utf-8') as f:
    toml_text = f.read()

pp3_attrs = dict()
current_section = None
lines = toml_text.split('\n')
for line in lines:
    if re.search(TOML_SECTION_REGEX, line):
        match = re.search(TOML_SECTION_REGEX, line)
        current_section = match['key']
        pp3_attrs[current_section] = list()
    if re.search(TOML_KEY_REGEX, line):
        match = re.search(TOML_KEY_REGEX, line)
        pp3_attrs[current_section].append(match['key'])


print(pp3_attrs)