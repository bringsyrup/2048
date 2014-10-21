"""
Creating array to track values
"""

from math import pi
import pygame as pg
import random



class ArrayManipulation():

	def __init__(self, polys):
		self.ValueMap = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

	def Polys2Array(self, polys):
		"""converts list of polygons to matrix ValueMap"""
		
		for poly in polys:
			self.ValueMap[int((poly.theta)*(-2. / pi) + 3)][poly.layer - 1] = poly.value		#switching from theta to i and layer to j

		return self.ValueMap


	def UP(self):
		"""when up is pressed"""

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


		return ArrayToPolys()


	def DOWN(self):
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


		return ArrayToPolys()


	def LEFT(self):
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

		return ArrayToPolys()


	def RIGHT(self):
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
		for i in range(0,4):
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

		return ArrayToPolys()

"""
	def RandomPopup(self):
		openspots = []
		for i in range(4)
			for j in range(f)
				if self.ValueMap[i][j] == 0:
					openspots.append((i,j))
		(a,b) = random.choice(openspots)
		ValueMap[a][b] = 2

	"""
	def ArrayToPolys(self):
		polys_list = []
		for i in range(4):
			for j in range(4):
				if self.ValueMap[i][j] != 0:
					polys_list.append([int((pi / 2) * (3 - i)), j + 1, self.ValueMap[i][j]])		#populating list of form: [[theta, layer, value], [...]]

		return polys_list