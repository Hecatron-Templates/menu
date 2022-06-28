#!/usr/bin/env python3

from asciimatics.renderers import FigletText, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
from pyfiglet import Figlet
import sys

# With asciimatics things are layered as screen -> scenes -> effects -> frames
# With a frame being an a subclass of an effect
# frame is layered as frame -> layout -> widgets
# https://asciimatics.readthedocs.io/en/stable/widgets.html#layouts-in-more-detail



def demo(screen):
    scenes = []

    logotext = "Test"
    # Fonts - http://www.figlet.org/
    logofont = "banner"


    text = Figlet(font=logofont, width=200).renderText(logotext)
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
            Fire(screen.height, 80, text, 0.4, 40, screen.colours),
            0,
            speed=1,
            transparent=False),
        Print(screen,
            FigletText(logotext, logofont),
            screen.height - 9, x=(screen.width - width) // 2 + 1,
            colour=Screen.COLOUR_BLACK,
            bg=Screen.COLOUR_BLACK,
            speed=1),
        Print(screen,
            FigletText(logotext, logofont),
            screen.height - 9,
            colour=Screen.COLOUR_WHITE,
            bg=Screen.COLOUR_WHITE,
            speed=1),
    ]
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
