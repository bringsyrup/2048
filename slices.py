"""
class for a single slidy thing given outer layer, width of layer, screen dimensions and initial angle position
"""

import pygame as pg
from math import sin, cos, pi

class Slice(object):
    def __init__(self, screen, dims, width, theta, layer, value, color):
        self.screen = screen
        self.dims = dims
        self.width = width
        self.theta = theta
        self.layer = float(layer)
        self.value = value
        self.color = color
        self.x = "x = .5*self.dims[0] + nlayer/4*self.width*cos(ntheta)"
        self.y = "y = .47*self.dims[1] + nlayer/4*self.width*sin(ntheta)"

    def points(self, ntheta, nlayer):
        """points to define polygon"""
        exec self.x
        exec self.y
        return [x, y]

    def init(self):
        pg.draw.polygon(
                self.screen, 
                self.color,
                [self.points(self.theta, self.layer),
                    self.points(self.theta, self.layer-1),
                    self.points(pi/4+self.theta, self.layer-1),
                    self.points(pi/2+self.theta, self.layer-1),
                    self.points(pi/2+self.theta, self.layer),
                    self.points(pi/4+self.theta, self.layer)
                    ]
                )
        """filled in polygon"""
        pg.draw.polygon(
                self.screen, 
                (200, 200, 200),
                [self.points(self.theta, self.layer),
                    self.points(self.theta, self.layer-1),
                    self.points(pi/4+self.theta, self.layer-1),
                    self.points(pi/2+self.theta, self.layer-1),
                    self.points(pi/2+self.theta, self.layer),
                    self.points(pi/4+self.theta, self.layer)
                    ],
                5
                )
        self.screen.blit(
                pg.font.SysFont('Arial', 11).render(str(self.value), True, (075, 075, 075)),
                (
                    self.points(pi/4+self.theta, self.layer-1)[0] + ((self.points(pi/4+self.theta, self.layer)[0]-self.points(pi/4+self.theta, self.layer-1)[0])/2) - 5,
                    self.points(pi/4+self.theta, self.layer)[1] + ((self.points(pi/4+self.theta, self.layer-1)[1]-self.points(pi/4+self.theta, self.layer)[1])/2) - 4
                    )
                )
