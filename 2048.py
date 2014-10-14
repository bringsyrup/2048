#! /bin/env python

     
""" Ruby ____ Brian
________/2048\_______
        \____/       """


import pygame as pg
from math import pi
import sys
from pygame.locals import *
import buttActions as butts

try:
    from pygame import gfxdraw
except:
    pass

class Button(pg.sprite.Sprite):
    """
    button creator!
    """
    def __init__(self, surf, size, location, text, colors):
        self.surf = surf            # main screen
        self.size = size            # size as list ex. [200, 50]
        self.location = location    # location as list ex. [dims[0]/2, dims[1]-50] 
        self.text = text[0]         # raw text to go in button
        self.fontsize = text[1]     # fontsize
        self.fill = colors[0]       # first item in colors list
        self.border = colors[1]     # second item in colors list
        self.textColor = colors[2]
        self.font = pg.font.SysFont('Arial', self.fontsize)   # text[1] is fontsize

    def getText(self):
        x_len = .55*self.fontsize*len(self.text)
        y_len = self.fontsize
        x_txt = self.location[0] + .5*(self.size[0] - x_len)
        y_txt = self.location[1] + .5*(self.size[1] - y_len)
        return (x_txt, y_txt)

    def liveButton(self, buttNumb):
        pos = pg.mouse.get_pos()
        if pos[0] >= self.location[0] and pos[1] >= self.location[1] and pos[0] <= (self.location[0] + self.size[0]) and pos[1] <= (self.location[1] + self.size[1]):
            butts.buttAction(buttNumb)
        return self.staticButton()

    def staticButton(self):
        '''button fill'''
        fill = pg.draw.rect(
                self.surf,
                self.fill,
                (
                    self.location[0],
                    self.location[1],
                    self.size[0],
                    self.size[1]
                    )
                )
        '''button border'''
        border = pg.draw.rect(
                self.surf,
                self.border,
                (
                    self.location[0],
                    self.location[1],
                    self.size[0],
                    self.size[1]
                    ),
                3
                )
        textLocation = self.getText()
        text = self.surf.blit(
                self.font.render(self.text,
                    True,
                    self.textColor,
                    ),
                textLocation
                )
        return fill, border, text

def init(dims=(1600, 875), fillColor=(255,255,255), circBorder=(200,200,230), layers=4, buttCheck=False):
    """
    initial game setup
    """
    pg.init()
    screen = pg.display.set_mode(dims, HWSURFACE|DOUBLEBUF|RESIZABLE )
    screen.fill(fillColor)
    for i in range(1, layers+1):
        try:
            pg.gfxdraw.circle(screen, dims[0]/2, dims[1]/2, i*200/layers, circBorder)
        except:
            pg.draw.circle(screen, circBorder, (dims[0]/2, dims[1]/2), i*200/layers, 2)
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
        
def main():
    """
    function that runs the game. like the cpu of the game. kind of.
    """

    counter = 0
    while True:
        if counter == 0:
            screen = init()
        pg.event.pump()
        for event in pg.event.get():
            if event.type == QUIT:
               print "thanks for playing Ruby and Brian's 2048!"
               pg.quit()
               sys.exit()
            elif event.type == VIDEORESIZE:
                screen = init(dims=(event.w, event.h))
            elif event.type == MOUSEBUTTONUP:
                screenSize = screen.get_size()
                butts = init(dims=screenSize, buttCheck=True)
                for i, butt in enumerate(butts):
                    butt.liveButton(i)
        pg.display.update()
        counter += 1
               
if __name__=="__main__":
    main()
