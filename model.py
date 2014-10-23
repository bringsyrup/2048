"""
Creating array to track values
"""

from math import pi
from slices import Slice
import pygame as pg
import random


class ArrayManipulation():

    def __init__(self, polys):
        self.ValueMap = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.polys = polys

    def Polys2Array(self):
        """converts list of polygons to matrix ValueMap"""

        for poly in self.polys:
            self.ValueMap[int((poly.theta)*(2. / pi))][int(poly.layer - 1)] = int(poly.value)		#switching from theta to i and layer to j
        #return self.ValueMap


    def LEFT(self):
        """when left is pressed"""
        self.Polys2Array()
        """Moving numbers to empty spaces"""
        i = 0
        for j in range(0,4):
            if self.ValueMap[i][j]!=0 or self.ValueMap[i+1][j]!=0 or self.ValueMap[i+2][j]!=0 or self.ValueMap[i+3][j]!=0:
                if self.ValueMap[i][j] == 0:
                    while self.ValueMap[i][j] == 0:
                        self.ValueMap[i][j] = self.ValueMap[i+1][j]
                        self.ValueMap[i+1][j] = self.ValueMap[i+2][j]
                        self.ValueMap[i+2][j] = self.ValueMap[i+3][j]
                        self.ValueMap[i+3][j] = 0
                if self.ValueMap[i+1][j] == 0 and (self.ValueMap[i+2][j]!=0 or self.ValueMap[i+3][j]!=0):
                    while self.ValueMap[i+1][j] == 0:
                        self.ValueMap[i+1][j] = self.ValueMap[i+2][j]
                        self.ValueMap[i+2][j] = self.ValueMap[i+3][j]
                        self.ValueMap[i+3][j] = 0
                if self.ValueMap[i+2][j] == 0 and self.ValueMap[i+3][j]!=0:
                    while self.ValueMap[i+2][j] == 0:
                        self.ValueMap[i+2][j] = self.ValueMap[i+3][j]
                        self.ValueMap[i+3][j] = 0

        """Adding similar numbers in adjacent spaces"""
        i = 0
        for j in range(0,4):
            if self.ValueMap[i][j] == self.ValueMap[i+1][j]:
                self.ValueMap[i][j] = self.ValueMap[i][j] + self.ValueMap[i+1][j]
                self.ValueMap[i+1][j] = self.ValueMap[i+2][j]
                self.ValueMap[i+2][j] = self.ValueMap[i+3][j]
                self.ValueMap[i+3][j] = 0
            if self.ValueMap[i+1][j] == self.ValueMap[i+2][j]:
                self.ValueMap[i+1][j] = self.ValueMap[i+1][j] + self.ValueMap[i+2][j]
                self.ValueMap[i+2][j] = self.ValueMap[i+3][j]
                self.ValueMap[i+3][j] = 0
            if self.ValueMap[i+2][j] == self.ValueMap[i+3][j]:
                self.ValueMap[i+2][j] = self.ValueMap[i+2][j] + self.ValueMap[i+3][j]
                self.ValueMap[i+3][j] = 0

        return self.ArrayToPolys()


    def RIGHT(self):
        """when right is pressed"""
        self.Polys2Array()
        """Moving numbers to empty spaces"""
        i = 0
        for j in range(0,4):
            if self.ValueMap[i][j]!=0 or self.ValueMap[i+1][j]!=0 or self.ValueMap[i+2][j]!=0 or self.ValueMap[i+3][j]!=0:
                if self.ValueMap[i+3][j] == 0:
                    while self.ValueMap[i+3][j] == 0:
                        self.ValueMap[i+3][j] = self.ValueMap[i+2][j]
                        self.ValueMap[i+2][j] = self.ValueMap[i+1][j]
                        self.ValueMap[i+1][j] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0
                if self.ValueMap[i+2][j] == 0 and (self.ValueMap[i+1][j]!=0 or self.ValueMap[i][j]!=0):
                    while self.ValueMap[i+2][j] == 0:
                        self.ValueMap[i+2][j] = self.ValueMap[i+1][j]
                        self.ValueMap[i+1][j] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0
                if self.ValueMap[i+1][j] == 0 and self.ValueMap[i][j]!=0:
                    while self.ValueMap[i+1][j] == 0:
                        self.ValueMap[i+1][j] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0

        """Adding similar numbers in adjacent spaces"""
        i = 0
        for j in range(0,4):
            if self.ValueMap[i+3][j] == self.ValueMap[i+2][j]:
                self.ValueMap[i+3][j] = self.ValueMap[i+3][j] + self.ValueMap[i+2][j]
                self.ValueMap[i+2][j] = self.ValueMap[i+1][j]
                self.ValueMap[i+1][j] = self.ValueMap[i][j]
                self.ValueMap[i][j] = 0
            if self.ValueMap[i+2][j] == self.ValueMap[i+1][j]:
                self.ValueMap[i+2][j] = self.ValueMap[i+2][j] + self.ValueMap[i+1][j]
                self.ValueMap[i+1][j] = self.ValueMap[i][j]
                self.ValueMap[i][j] = 0
            if self.ValueMap[i+1][j] == self.ValueMap[i][j]:
                self.ValueMap[i+1][j] = self.ValueMap[i+1][j] + self.ValueMap[i][j]
                self.ValueMap[i][j] = 0

        return self.ArrayToPolys()


    def UP(self):
        """when up is pressed"""
        self.Polys2Array()
        """Moving numbers to empty spaces"""
        j = 0
        for i in range(0,4):
            if self.ValueMap[i][j]!=0 or self.ValueMap[i][j+1]!=0 or self.ValueMap[i][j+2]!=0 or self.ValueMap[i][j+3]!= 0:
                if self.ValueMap[i][j] == 0:
                    while self.ValueMap[i][j] == 0:
                        self.ValueMap[i][j] = self.ValueMap[i][j+1]
                        self.ValueMap[i][j+1] = self.ValueMap[i][j+2]
                        self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
                        self.ValueMap[i][j+3] = 0
                if self.ValueMap[i][j+1] == 0 :
                    while self.ValueMap[i][j+1] == 0 and (self.ValueMap[i][j+2]!=0 or self.ValueMap[i][j+3]!=0):
                        self.ValueMap[i][j+1] = self.ValueMap[i][j+2]
                        self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
                        self.ValueMap[i][j+3] = 0
                if self.ValueMap[i][j+2] == 0:
                    while self.ValueMap[i][j+2] == 0 and self.ValueMap[i][j+3]!=0:
                        self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
                        self.ValueMap[i][j+3] = 0

        """Adding similar numbers in adjacent spaces"""
        j = 0
        for i in range(0,4):
            if self.ValueMap[i][j] == self.ValueMap[i][j+1]:
                self.ValueMap[i][j] = self.ValueMap[i][j] + self.ValueMap[i][j+1]
                self.ValueMap[i][j+1] = self.ValueMap[i][j+2]
                self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
                self.ValueMap[i][j+3] = 0
            if self.ValueMap[i][j+1] == self.ValueMap[i][j+2]:
                self.ValueMap[i][j+1] = self.ValueMap[i][j+1] + self.ValueMap[i][j+2]
                self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
                self.ValueMap[i][j+3] = 0
            if self.ValueMap[i][j+2] == self.ValueMap[i][j+3]:
                self.ValueMap[i][j+2] = self.ValueMap[i][j+2] + self.ValueMap[i][j+3]
                self.ValueMap[i][j+3] = 0

        return self.ArrayToPolys()

    def DOWN(self):
        """when down is pressed"""
        self.Polys2Array()
        """Moving numbers to empty spaces"""
        j = 0
        for i in range(4):
            if self.ValueMap[i][j]!=0 or self.ValueMap[i][j+1]!=0 or self.ValueMap[i][j+2]!=0 or self.ValueMap[i][j+3]!= 0:
                if self.ValueMap[i][j+3] == 0:
                    while self.ValueMap[i][j+3] == 0:
                        self.ValueMap[i][j+3] = self.ValueMap[i][j+2]
                        self.ValueMap[i][j+2] = self.ValueMap[i][j+1]
                        self.ValueMap[i][j+1] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0
                if self.ValueMap[i][j+2] == 0  and (self.ValueMap[i][j+1]!=0 or self.ValueMap[i][j]!=0):
                    while self.ValueMap[i][j+2] == 0:
                        self.ValueMap[i][j+2] = self.ValueMap[i][j+1]
                        self.ValueMap[i][j+1] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0
                if self.ValueMap[i][j+1] == 0:
                    while self.ValueMap[i][j+1] == 0 and self.ValueMap[i][j]!=0:
                        self.ValueMap[i][j+1] = self.ValueMap[i][j]
                        self.ValueMap[i][j] = 0

        """Adding similar numbers in adjacent spaces"""
        j = 0
        for i in range(4):
            if self.ValueMap[i][j+3] == self.ValueMap[i][j+2]:
                self.ValueMap[i][j+3] = self.ValueMap[i][j+3] + self.ValueMap[i][j+2]
                self.ValueMap[i][j+2] = self.ValueMap[i][j+1]
                self.ValueMap[i][j+1] = self.ValueMap[i][j]
                self.ValueMap[i][j] = 0
            if self.ValueMap[i][j+2] == self.ValueMap[i][j+1]:
                self.ValueMap[i][j+2] = self.ValueMap[i][j+2] + self.ValueMap[i][j+1]
                self.ValueMap[i][j+1] = self.ValueMap[i][j]
                self.ValueMap[i][j] = 0
            if self.ValueMap[i][j+1] == self.ValueMap[i][j]:
                self.ValueMap[i][j+1] = self.ValueMap[i][j+1] + self.ValueMap[i][j]
                self.ValueMap[i][j] = 0

        return self.ArrayToPolys()

    def ArrayToPolys(self):
        polys_list = []
        for i in range(4):
            for j in range(4):
                if self.ValueMap[i][j] != 0:
                    polys_list.append([(pi/2.)*i, j + 1, self.ValueMap[i][j]])		#populating list of form: [[theta, layer, value], [...]]
        return polys_list