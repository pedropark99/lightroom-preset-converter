import re

TOML_KEY_REGEX = r'^(?P<key>[A-Za-z0-9]+)( )?='

toml_text = '''
Auto=false
Clip=0.02
Compensation=0
Brightness=0
Contrast=0
Saturation=0
Black=0
HighlightCompr=0
HighlightComprThreshold=0
ShadowCompr=50
HistogramMatching=true
CurveFromHistogramMatching=true
ClampOOG=true
CurveMode=FilmLike
CurveMode2=Standard
Curve=4;0;0;0.050000000000000003;0.025915307334948689;0.12;0.094013162586586096;0.21799999999999997;0.26066079610420401;0.35519999999999996;0.54004663005862086;0.54727999999999999;0.8161151428792226;0.81619199999999992;0.97119514854912681;1;1;
Curve2=0;
'''


lines = toml_text.split('\n')
for line in lines:
    match = re.search(TOML_KEY_REGEX, line)
    if match:
        print(f"'{match['key']}',")