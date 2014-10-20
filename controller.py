"""
help class for event types and actions
contains motion control keys for shapes
"""

import pygame as pg

class Controller(object):
    """
    Using arrow keys to control movement of slices
    """
    def __init__(self):
        self = self

    def keys(self, event):
        if event.key == pg.K_UP:
            print("Move In")
        elif event.key == pg.K_DOWN:
            print("Move Out")
        elif event.key == pg.K_LEFT:
            print("Move Clockwise")
        elif event.key == pg.K_RIGHT:
            print("Move Counter-Clockwise")


