#!/usr/bin/env python3

import pathlib

templates = {
    "black": (31, 33, 40),
    "magenta": (55, 25, 53),
    "violet": (42, 25, 55),
    "indigo": (25, 31, 55),
    "blue": (25, 48, 55),
    "green": (25, 55, 34),
    "yellow": (54, 55, 25),
    "orange": (55, 43, 25),
    "red": (55, 25, 25),
}


def make_new_itermcolors(
    original_path: pathlib.Path,
    name: str,
    r: int,
    g: int,
    b: int,
    output_dir: pathlib.Path
):

    # preprend "template." to filename
    new_name = original_path.name.replace("template.", f'{name}.')
    output_path = output_dir / new_name

    # rgb calc
    (rr, gr, br) = (f'{r/255.0:.17f}', f'{g/255.0:.17f}', f'{b/255.0:.17f}')

    # placeholder replacements
    replace_map = {
        r"{{background-color-red}}": rr,
        r"{{background-color-green}}": gr,
        r"{{background-color-blue}}": br,
    }

    # read file
    with open(original_path, mode="r") as file:
        template = file.read()

    # replace placeholders
    output_txt = template
    for placeholder, color_value in replace_map.items():
        assert placeholder in template, f"placeholder not found: {placeholder}"
        output_txt = output_txt.replace(placeholder, color_value)

    # write file
    with open(output_path, mode="w+") as file:
        file.write(output_txt)


original_path = pathlib.Path(r"templates/template.PaleNightHC.itermcolors")
output_dir = pathlib.Path(r'derivatives')
for name, (r, g, b) in templates.items():
    make_new_itermcolors(
        original_path=original_path,
        name=name,
        r=r, g=g, b=b,
        output_dir=output_dir
        )
