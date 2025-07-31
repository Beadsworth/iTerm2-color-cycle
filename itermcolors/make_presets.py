#!/usr/bin/env python3

import pathlib

templates = {
    "black": (63, 66, 80),
    "red": (110, 51, 51),
    "orange": (110, 86, 51),
    "yellow": (108, 110, 51),
    "green": (51, 110, 69),
    "blue": (51, 96, 110),
    "indigo": (51, 63, 110),
    "violet": (84, 51, 110),
    "magenta": (110, 51, 106),
}


def make_new_itermcolors(
    original_path: pathlib.Path,
    name: str,
    r: int,
    g: int,
    b: int,
    output_dir: pathlib.Path
):
    print(r, g, b)

    # preprend "template." to filename
    new_name = original_path.name.replace("template.", f'{name}.')
    output_path = output_dir / new_name

    # rgb calc
    (rr, gr, br) = (f'{r/255.0:.17f}', f'{g/255.0:.17f}', f'{b/255.0:.17f}')
    print(rr, gr, br)

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

    print(output_txt)

    # write file
    with open(output_path, mode="w+") as file:
        file.write(output_txt)


original_path = pathlib.Path(r"/Users/james.beadsworth/Library/Application Support/iTerm2/Scripts/itermcolors/templates/template.PaleNightHC.itermcolors")
output_dir = pathlib.Path(r'/Users/james.beadsworth/Library/Application Support/iTerm2/Scripts/itermcolors/derivatives')
for name, (r, g, b) in templates.items():
    make_new_itermcolors(
        original_path=original_path,
        name=name,
        r=r, g=g, b=b,
        output_dir=output_dir
        )
