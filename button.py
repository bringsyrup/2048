
"""
button class! 
imorts buttAction to make live buttons a thing
static buttons are just rectangles
"""

import pygame as pg
from buttActions import buttAction

class Button(object):
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
            buttAction(buttNumb)
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
        return (fill, border, text)


