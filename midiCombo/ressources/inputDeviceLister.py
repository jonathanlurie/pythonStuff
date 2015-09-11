"""
Pints the list of MIDI devices available for inpout use.

"""

import sys
import os

import pygame
import pygame.midi
from pygame.locals import *

try:  # Ensure set available for output example
    set
except NameError:
    from sets import Set as set


def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()

def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            print("\t- Name: " + str(name) + "\tInterface: " + str(interf) )


if __name__ == '__main__':

    print("\nHere is the list of MIDI devices available for INPUT:")

    print_device_info()

    print("\n")
