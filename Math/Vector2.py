import math

class Vector2(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __add__(self, other):
		c = Vector2(0,0)
		c.x = other.x + self.x
		c.y = other.y + self.y
		return c	
	
	def __sub__(self, other):
		c = Vector2(0,0)
		c.x = self.x - other.x
		c.y = self.y - other.y
		return c
		
	def __mul__(self, other):
		c = Vector2(0,0)
		c.x = self.x * other.x
		c.y = self.y * other.y
		return c
		
	def __truediv__(self, other):
		c = Vector2(0,0)
		c.x = round((self.x / other.x), 2)
		c.y = round((self.y / other.y), 2)
		
		return c
		
	def Mag(self):
		Thesqrt = 0
		A = 0
		A = (self.x * self.x) + (self.y * self.y)
		Thesqrt = round((math.sqrt(A)), 2)
		return Thesqrt
		
	def Norm(self):
		c = Vector2(0,0)
		Thesqrt = 0
		A = 0
		A = (self.x * self.x) + (self.y * self.y)
		Thesqrt = math.sqrt(A)
		c.x = round((self.x / Thesqrt), 2)
		c.y = round((self.y / Thesqrt), 2)
		return c
		
	def Dot(self, b):
		A = 0
		A = (self.x * self.x) + (self.y * self.y)
		return A
		
	def Lerp(self, b):
		