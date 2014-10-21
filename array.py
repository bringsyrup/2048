"""
Creating array to track values
"""

from random import randint
import pygame as pg

ValueMap = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ValueMap = [randint(0,3)][randint(0,3)] = 2		#start with one 2

def direction(ValueMap, event):
	if event.key == pg.K_UP:
		i=0
		for j in range(0,4):
			if ValueMap[i][j]!=0 or ValueMap[i+1][j]!=0 or ValueMap[i+2][j]!=0 or ValueMap[i+3][j]!=0:
			"""when you press up and there's nothing in the top row"""
				if ValueMap[i][j] == 0:
					while ValueMap[i][j] == 0:
						ValueMap[i][j] = ValueMap[i+1][j]
						ValueMap[i+1][j] = ValueMap[i+2][j]
						ValueMap[i+2][j] = ValueMap[i+3][j]
						ValueMap[i+3][j] = 0
				if ValueMap[i+1][j] == 0 and (ValueMap[i+2][j]!=0 or ValueMap[i+3][j]!=0):
					while ValueMap[i+1][j] == 0:
						ValueMap[i+1][j] = ValueMap[i+2][j]
						ValueMap[i+2][j] = ValueMap[i+3][j]
						ValueMap[i+3][j] = 0
				if ValueMap[i+2][j] == 0 and ValueMap[i+3][j]!=0:
					while ValueMap[i+2][j] == 0:
						ValueMap[i+2][j] = ValueMap[i+3][j]
						ValueMap[i+3][j] = 0