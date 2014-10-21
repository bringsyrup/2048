#! /bin/env python

     
""" Ruby ____ Brian
________/2048\_______
        \____/       """


import pygame as pg
import sys
from pygame.locals import *
from button import Button
from controller import Controller
from math import pi, cos, sin
from slices import Slice
from random import randint

class Game(object):

    def __init__(self, fillColor=(255,255,255), polyBorder=(100,100,100), layers=4, width=200):
        """
        initialize Game class with background color, circle color and number of circles
        """
        self.fillColor = fillColor
        self.polyBorder = polyBorder
        self.layers = layers
        self.width = width

    def make_butts(self, dims, screen):
        button_list = tuple()
        live_butts = list()
        '''make NEW GAME dynamic button'''
        newGame = Button(
                    screen,
                    [200, 50],
                    [dims[0]/2-100, dims[1]-75],
                    ["new game", 20],
                    [(210, 210, 255), (200, 200, 230), (0, 0, 0)]
                    )
        live_butts.append(newGame)
        button_list += newGame.staticButton()
        '''make PAUSE dynamic button'''
        pause = Button(
                    screen,
                    [100, 50],
                    [dims[0]/4-100, dims[1]-75],
                    ["pause", 20],
                    [(230, 200, 200), (230, 100, 100), (0, 0, 0)]
                    )
        live_butts.append(pause)
        button_list += pause.staticButton()
        '''make HIGH SCORE static button'''
        highScore = Button(
                    screen,
                    [100, 50],
                    [dims[0]/2-100, 20],
                    ["HIGH SCORE:", 20],
                    [(255, 255, 255), (255, 255, 255), (0, 0, 0)]
                    )
        button_list += highScore.staticButton()
        return button_list, live_butts

    def init(self, dims, polypos=[[0, 4, 2], [0, 3, 2]]):
        """
        initial game setup
        """
        pg.init()
        screen = pg.display.set_mode(dims, HWSURFACE|DOUBLEBUF|RESIZABLE )
        screen.fill(self.fillColor)
        pg.display.set_caption("2048 on crack")
        buttons, live_butts = self.make_butts(dims, screen) 
        for i in range(1, self.layers+1):
            pg.draw.polygon(
                    screen, 
                    self.polyBorder, 
                    [
                        [(.5*dims[0] + i/4.*self.width*cos(0)), (.5*dims[1] + i/4.*self.width*sin(0))], 
                        [(.5*dims[0] + i/4.*self.width*cos(pi/4)), (.5*dims[1] + i/4.*self.width*sin(pi/4))],
                        [(.5*dims[0] + i/4.*self.width*cos(pi/2)), (.5*dims[1] + i/4.*self.width*sin(pi/2))], 
                        [(.5*dims[0] + i/4.*self.width*cos(3*pi/4)), (.5*dims[1] + i/4.*self.width*sin(3*pi/4))], 
                        [(.5*dims[0] + i/4.*self.width*cos(pi)), (.5*dims[1] + i/4.*self.width*sin(pi))], 
                        [(.5*dims[0] + i/4.*self.width*cos(5*pi/4)), (.5*dims[1] + i/4.*self.width*sin(5*pi/4))], 
                        [(.5*dims[0] + i/4.*self.width*cos(6*pi/4)), (.5*dims[1] + i/4.*self.width*sin(6*pi/4))], 
                        [(.5*dims[0] + i/4.*self.width*cos(7*pi/4)), (.5*dims[1] + i/4.*self.width*sin(7*pi/4))] 
                        ],
                    3
                    )
        pg.display.flip()
        pg.display.update(buttons)
        polys = list()
        for poly in polypos:
            new_poly = Slice(screen, dims, self.width, poly[0], poly[1], poly[2])
            polys.append(new_poly)
            pg.display.update(new_poly.init())
        return screen, live_butts, polys
    
    def quit(self):
        print "thanks for playing Ruby and Brian's 2048!"
        pg.quit()
        sys.exit()

    def run(self):
        """
        function that runs the game. like the cpu of the game. kind of.
        """
        rand_outer = [0., pi/2., pi, 3.*pi/2.]
        curr_polypos = [[rand_outer[randint(0, 3)], randint(1, 2), 2], [rand_outer[randint(0, 3)], randint(3, 4), 2]]
        curr_dims = (1600, 875)
        screen, buttons, polys = self.init(curr_dims, polypos=curr_polypos)
        control = Controller()
        while True:
            pg.event.pump()
            for event in pg.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == VIDEORESIZE:
                    curr_dims = (event.w, event.h)
                    screen, buttons, polys = self.init(curr_dims, polypos=curr_polypos)
                elif event.type == MOUSEBUTTONUP:
                    for i, butt in enumerate(buttons):
                        buttNumb =  butt.liveButton(i)
                        if buttNumb == 0:
                            print "new game"
                            self.run()
                        else:
                            print "game paused"
                            break
                elif event.type == KEYDOWN:
                    if event.key != K_ESCAPE:
                        curr_polypos = control.keys(event, polys)
                        screen, buttons, polys = self.init(curr_dims, polypos=curr_polypos)
                    else:
                        self.quit()
            pg.display.update()
                   
if __name__=="__main__":
    
    newGame = Game()
    newGame.run()
