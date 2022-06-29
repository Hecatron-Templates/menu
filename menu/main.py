#!/usr/bin/env python3

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from tui_logo import get_logo_effects
from tui_selector import SelectorFrame
from config import MenuConfig
import sys

# With asciimatics things are layered as screen -> scenes -> effects -> frames
# With a frame being an a subclass of an effect
# frame is layered as frame -> layout -> widgets
# https://asciimatics.readthedocs.io/en/stable/widgets.html#layouts-in-more-detail

cfg = MenuConfig()

def setup_screen(screen):
    scenes = []
    effects = []
    effects += get_logo_effects(screen)
    effects.append(SelectorFrame(screen, cfg, args))
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)

def menu(argv):
    cfg.read()
    global args
    args = argv
    while True:
        try:
            Screen.wrapper(setup_screen)
            break
        except ResizeScreenError:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("at least one argument is required")
    menu(sys.argv)
