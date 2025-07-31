#!/usr/bin/env python3

import iterm2
import random


enabled_profiles = (
    "random-color",
)

enabled_presets = (
    "black.PaleNightHC",
    "blue.PaleNightHC",
    "green.PaleNightHC",
    "indigo.PaleNightHC",
    "magenta.PaleNightHC",
    "orange.PaleNightHC",
    "red.PaleNightHC",
    "violet.PaleNightHC",
    "yellow.PaleNightHC",
)


async def set_preset_and_tab_color(connection, session, preset_name):

    profile = await session.async_get_profile()
    if not profile or profile.name not in enabled_profiles:
        print("bad profile")
        return

    preset = await iterm2.ColorPreset.async_get(connection, preset_name)
    if not preset:
        print("bad preset")
        return

    # Query the actual background color from the session
    colors = preset.values
    preset_color_dict = {color.key: color for color in colors}
    bg_color = preset_color_dict["Background Color"]

    if not bg_color:
        print("no background color")
        return

    print(f'Changing profile {profile.name} to preset: {preset_name}')
    print(f'Changing tab color to {bg_color}')
    change = iterm2.LocalWriteOnlyProfile()
    change.set_background_color(bg_color)
    change.set_tab_color(bg_color)
    change.set_use_tab_color(True)
    await session.async_set_profile_properties(change)


async def main(connection):
    app = await iterm2.async_get_app(connection)
    # Note: in your environment you might need async_get_list instead of async_list_presets
    color_preset_names_all = await iterm2.ColorPreset.async_get_list(connection)
    color_preset_names = [
        preset_name for preset_name in color_preset_names_all
        if preset_name in enabled_presets
        ]

    async with iterm2.NewSessionMonitor(connection) as mon:
        while True:
            session_id = await mon.async_get()
            session = app.get_session_by_id(session_id)
            if session:
                chosen = random.choice(color_preset_names)
                await set_preset_and_tab_color(connection, session, chosen)


iterm2.run_forever(main)
