#!/usr/bin/env python3

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from tui_logo import get_logo_effects
from tui_selector import SelectorFrame
from copier import run_auto
import sys

# With asciimatics things are layered as screen -> scenes -> effects -> frames
# With a frame being an a subclass of an effect
# frame is layered as frame -> layout -> widgets
# https://asciimatics.readthedocs.io/en/stable/widgets.html#layouts-in-more-detail

def setup_screen(screen):
    scenes = []
    effects = []
    effects += get_logo_effects(screen)
    effects.append(SelectorFrame(screen))
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)

def menu():
    while True:
        try:
            Screen.wrapper(setup_screen)
            sys.exit(0)
        except ResizeScreenError:
            pass

if __name__ == "__main__":
    menu()

# TODO
# Wrapper for debugging copier launched scripts
#run_auto("./", "./temp/temp1")
