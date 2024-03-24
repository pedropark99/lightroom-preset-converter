from read_xmp import parse_xmp, XMP_EXAMPLES


def convert_to_rt(path: str):
    xmp = parse_xmp(path)
    return xmp


a = convert_to_rt(XMP_EXAMPLES[3])
print(a)