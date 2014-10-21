"""
Creating array to track values
"""

from random import randint
import pygame as pg


class ArrrayManipulation():

	def __init__(self, polys):

		self.ValueMap = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		self.ValueMap[randint(0,3)][randint(0,3)] = 2		#start with one 2


	def Polys2Array(self, polys):
		"""converts list of polygons to matrix ValueMap"""
		###something here###
	return ValueMap


	def UP(self, ValueMap):
		"""when up is pressed"""

		"""Moving numbers to empty spaces"""
		i = 0
		for j in range(0,4):
			if self.ValueMap[i][j]!=0 or self.ValueMap[i+1][j]!=0 or self.ValueMap[i+2][j]!=0 or self.ValueMap[i+3][j]!=0:""
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


	return self.ValueMap


	def DOWN(self, ValueMap):
		"""when down is pressed"""

		"""Moving numbers to empty spaces"""
		i = 0
		for j in range(0,4):
			if self.ValueMap[i][j]!=0 or self.ValueMap[i+1][j]!=0 or self.ValueMap[i+2][j]!=0 or self.ValueMap[i+3][j]!=0:
				if self.ValueMap[i+3][j] == 0:
					while self.ValeMap[i+3][j] == 0:
						self.ValueMap[i+3][j] = self.ValueMap[i+2][j]
						self.ValueMap[i+2][j] = self.ValueMap[i+1][j]
						self.ValueMap[i+1][j] = self.ValueMap[i][j]
						self.ValueMap[i][j] = 0
				if self.ValueMap[i+2][j] == 0:
					while self.ValueMap[i+2][j] == 0:
						self.ValueMap[i+2][j] = self.ValueMap[i+1][j]
						self.ValueMap[i+1][j] = self.ValueMap[i][j]
						self.ValueMap[i][j] = 0
				if self.ValueMap[i+1][j] == 0:
					while self.ValueMap[i+1][j] ==0:
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

	return self.ValueMap


	def LEFT(self, ValueMap):
		"""when left is pressed"""

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
				if self.ValueMap[i][j+1] == 0:
					while self.ValueMap[i][j+1] == 0:
						self.ValueMap[i][j+1] = self.ValueMap[i][j+2]
						self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
						self.ValueMap[i][j+3] = 0
				if self.ValueMap[i][j+2] == 0:
					while self.ValueMap[i][j+2] == 0:
						self.ValueMap[i][j+2] = self.ValueMap[i][j+3]
						self.ValueMap[i][j+3] = 0

		"""Adding similar numbers in adjacent spaces"""
		j = 0
		for i in range(0,4):
			if self.ValueMap[i][j] == self.ValueMap[i][j+1]:
				self.ValueMap[i][j] = self.ValueMap[i][j] + self.ValueMap[i][j+1]
				self.ValueMap[i][j] = self.ValueMap[i][j+1]
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

	return self.ValueMap


	def RIGHT(self, ValueMap):
		"""when right is pressed"""

		"""Moving numbers to empty spaces"""
		j = 0
		for i in range(0,4):
			if self.ValueMap[i][j]!=0 or self.ValueMap[i][j+1]!=0 or self.ValueMap[i][j+2]!=0 or self.ValueMap[i][j+3]!= 0:
				if self.ValueMap[i][j+3] == 0:
					while self.ValueMap[i][j+3] == 0:
						self.ValueMap[i][j+3] = self.ValueMap[i][j+2]
						self.ValueMap[i][j+2] = self.ValueMap[i][j+1]
						self.ValueMap[i][j+1] = self.ValueMap[i][j]
						self.ValueMap[i][j] = 0
				if self.ValueMap[i][j+2] == 0:
					while self.ValueMap[i][j+2] == 0:
						self.ValueMap[i][j+2] = self.ValueMap[i][j+1]
						self.ValueMap[i][j+1] = self.ValueMap[i][j]
						self.ValueMap[i][j] = 0
				if self.ValueMap[i][j+1] == 0:
					while self.ValueMap[i][j+1] == 0:
						self.ValueMap[i][j+1] = self.ValueMap[i][j]
						self.ValueMap[i][j] = 0

		"""Adding similar sumbers in adjacent spaces"""
		j = 0
		for i in range(0,4)
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

	return self.ValueMap


	def ArrayToPolys(self, ValueMap):

	return polys