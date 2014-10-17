#! /bin/env python

     
""" Ruby ____ Brian
________/2048\_______
        \____/       """


import pygame as pg
from math import pi
import sys
from pygame.locals import *
import buttActions as butts
from button import Button

try:
    from pygame import gfxdraw
except:
    pass

class Game(object):

    def __init__(self, fillColor=(255,255,255), circBorder=(200,200,230), layers=4):
        """
        initialize Game class with background color, circle color and number of circles
        """
        self.fillColor = fillColor
        self.circBorder = circBorder
        self.layers = layers

    def init(self, dims=(1600, 875), buttCheck=False):
        """
        initial game setup
        """
        pg.init()
        screen = pg.display.set_mode(dims, HWSURFACE|DOUBLEBUF|RESIZABLE )
        screen.fill(self.fillColor)
        for i in range(1, self.layers+1):
            try:
                pg.gfxdraw.circle(screen, dims[0]/2, dims[1]/2, i*200/layers, self.circBorder)
            except:
                pg.draw.circle(screen, self.circBorder, (dims[0]/2, dims[1]/2), i*200/self.layers, 2)
        pg.display.set_caption("2048 on crack")
        '''make NEW GAME dynamic button'''
        newGame = Button(
                    screen,
                    [200, 50],
                    [dims[0]/2-100, dims[1]-75],
                    ["new game", 20],
                    [(210, 210, 255), (200, 200, 230), (0, 0, 0)]
                    )
        fillNG, borderNG, textNG = newGame.staticButton() 
        '''make PAUSE dynamic button'''
        pause = Button(
                    screen,
                    [100, 50],
                    [dims[0]/4-100, dims[1]-75],
                    ["pause", 20],
                    [(230, 210, 210), (230, 100, 100), (0, 0, 0)]
                    )
        fillPS, borderPS, textPS = pause.staticButton() 
        '''make HIGH SCORE static button'''
        highScore = Button(
                    screen,
                    [100, 50],
                    [dims[0]/2-100, 20],
                    ["HIGH SCORE:", 20],
                    [(255, 255, 255), (255, 255, 255), (0, 0, 0)]
                    )
        fillHS, borderHS, textHS = highScore.staticButton()
        pg.display.flip()
        pg.display.update((fillNG, borderNG, textNG, fillHS, borderHS, textHS, fillPS, borderPS, textPS))
        if buttCheck == False:
            return screen
        else:
            return [newGame, pause]
            
    def main(self):
        """
        function that runs the game. like the cpu of the game. kind of.
        """

        counter = 0
        while True:
            if counter == 0:
                screen = self.init()
            pg.event.pump()
            for event in pg.event.get():
                if event.type == QUIT:
                   print "thanks for playing Ruby and Brian's 2048!"
                   pg.quit()
                   sys.exit()
                elif event.type == VIDEORESIZE:
                    screen = self.init(dims=(event.w, event.h))
                elif event.type == MOUSEBUTTONUP:
                    screenSize = screen.get_size()
                    butts = self.init(dims=screenSize, buttCheck=True)
                    for i, butt in enumerate(butts):
                        butt.liveButton(i)
            pg.display.update()
            counter += 1
                   
if __name__=="__main__":
    
    newGame = Game()
    newGame.main()
