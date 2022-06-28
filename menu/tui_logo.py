from asciimatics.renderers import FigletText, Fire, Plasma
from asciimatics.screen import Screen
from asciimatics.effects import Print
from pyfiglet import Figlet
import sys

def get_logo_effects(screen):
    logotext = "Hecatronic"
    logofont = "standard"

    # Text rendered as figlet - http://www.figlet.org/
    text = Figlet(font=logofont).renderText(logotext)
    width = max([len(x) for x in text.split("\n")])

    logo_y = 1 # Y offset from top
    logo_x = (screen.width - width) // 2 # X offset from the left
    fire_height = 10

    effects = [

        # Fire effect in background
        #Print(screen,
        #    Fire(logoheight + 9, 80, text, 0.4, 40, screen.colours),
        #    0,
        #    speed=1,
        #    transparent=False),
        #Print(screen,
        #    Plasma(plasma_height, screen.width, screen.colours),
        #    y=0,
        #    x=0,
        #    speed=1),


        Print(screen,
            Fire(height=fire_height,
                width=screen.width,
                emitter=text,
                intensity=0.4,
                spot=20,
                colours=screen.colours),
            y=0,
            x=0,
            speed=1,
            transparent=False),


        # Text shadown behind main text
        #Print(screen,
        #    FigletText(logotext, logofont),
        #    y=logo_y,
        #    x=logo_x,
        #    colour=Screen.COLOUR_BLACK,
        #    bg=Screen.COLOUR_BLACK,
        #    attr=Screen.COLOUR_BLACK,
        #    clear=True,
        #    speed=1),

        # Main text
        Print(screen,
            FigletText(logotext, logofont),
            y=logo_y,
            x=logo_x,
            colour=Screen.COLOUR_WHITE,
            #bg=Screen.COLOUR_BLUE,
            speed=1),
    ]
    return effects
