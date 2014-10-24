"""
helper class for event types and actions
contains motion control keys for shapes
recieves, sends process requests, and returns updated slice placement
"""

import pygame as pg
from slices import Slice
from math import pi
from model import ArrayManipulation as AM

class Controller(object):
    """
    Using arrow keys to control movement of slices
    """
    def __init__(self):
        self = self

    def keys(self, event, polys, highScore):
        if event.key == pg.K_UP:
            return AM(polys).UP()
        elif event.key == pg.K_DOWN:
            return AM(polys).DOWN()
        elif event.key == pg.K_LEFT:
            return AM(polys).LEFT()
        elif event.key == pg.K_RIGHT:
            return AM(polys).RIGHT()
        else:
            print "keyboard sequence no recognized"
            polypos = list()
            for poly in polys:
                polypos.append([poly.theta, poly.layer, poly.value, poly.color])
            return polypos, highScore
