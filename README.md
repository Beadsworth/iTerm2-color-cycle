# Cycle Color Presets

This python script runs with iTerm2 to cycle color presets on specific profiles.
## Pre-Reqs
1. `iTerm2` version 3.5 (I'm using Build 3.5.13)
2. `iTerm2` python runtime (I'm using 3.10.4) with `iterm2` package installed

## Setup
1. create color presets and import them into iTerms
   - create your own presets or use the template in this project with `./itermcolors/make_presets.py`
2. update `enabled_profiles` and `enabled_presets` in `AutoLaunch/cycle_color_presets.py`
3. copy `AutoLaunch/cycle_color_presets.py` to this folder on macos:
    - `/Users/SomeUser/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/cycle_color_presets.py`
