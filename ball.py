from random import random

class ball():
	def __init__(self, x, y, v_x, v_y):
		self.x = x
		self.y = y
		self.v_x = v_x
		self.v_y = v_y

	def move(self):
		self.x += self.v_x
		self.y += self.v_y
		if self.x + self.v_x <= 0:
			self.x = -self.x
			self.v_x = -self.v_x
		if self.y + self.v_y <= 0:
			self.y = -self.y
			self.v_y = -self.v_y
		if self.y + self.v_y >= 1:
			self.y = 2 - self.y
			self.v_y = -self.v_y
		
	