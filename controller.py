"""
help class for event types and actions
contains motion control keys for shapes
"""

import pygame as pg
from slices import Slice
from math import pi

class Controller(object):
    """
    Using arrow keys to control movement of slices
    """
    def __init__(self):
        self = self

    def keys(self, event, poly):
        if event.key == pg.K_UP:
            if poly.layer > 1:
                pg.display.update(poly.init(dlayer=-1.))
            return poly.theta, poly.layer
        elif event.key == pg.K_DOWN:
            if poly.layer < 4:
                pg.display.update(poly.init(dlayer=1.))
            return poly.theta, poly.layer
        elif event.key == pg.K_LEFT:
            pg.display.update(poly.init(dtheta=-pi/2))
            return poly.theta, poly.layer
        elif event.key == pg.K_RIGHT:
            pg.display.update(poly.init(dtheta=pi/2))
            return poly.theta, poly.layer
        else:
            print "keyboard sequence no recognized"
            return poly.theta, poly.layer

