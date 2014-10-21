"""
helper class for event types and actions
contains motion control keys for shapes
recieves, sends process requests, and returns updated slice placement
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

    def keys(self, event, polys):
        if event.key == pg.K_UP:
            polypos = list()
            for poly in polys:
                if poly.layer > 1:
                    poly.layer -= 1
                    polypos.append([poly.theta, poly.layer, poly.value])
                else:
                    polypos.append([poly.theta, poly.layer, poly.value])
            return polypos
        elif event.key == pg.K_DOWN:
            polypos = list()
            for poly in polys:
                if poly.layer < 4:
                    poly.layer += 1
                    polypos.append([poly.theta, poly.layer, poly.value])
                else:
                    polypos.append([poly.theta, poly.layer, poly.value])
            return polypos
        elif event.key == pg.K_LEFT:
            polypos = list()
            for poly in polys:
                if poly.theta != 0.0:
                    poly.theta -= pi/2.
                    polypos.append([poly.theta, poly.layer, poly.value])
                else:
                    polypos.append([poly.theta, poly.layer, poly.value])
            return polypos
        elif event.key == pg.K_RIGHT:
            polypos = list()
            for poly in polys:
                if poly.theta != 3*pi/2:
                    poly.theta += pi/2.
                    polypos.append([poly.theta, poly.layer, poly.value])
                else:
                    polypos.append([poly.theta, poly.layer, poly.value])
            return polypos
        else:
            print "keyboard sequence no recognized"
            polypos = list()
            for poly in polys:
                polypos.append([poly.theta, poly.layer, poly.value])
            return polypos
