import math

class Vector4(object):
	def __init__(self, w, x, y, z):
		self.w = w
		self.x = x
		self.y = y
		self.z = z
		
	def Normalise(self):
		c = Vector4(0,0,0,0)
		A = 0
		Thesqrt = 0
		A = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
		Thesqrt = math.sqrt(A)
		c.x = round((self.x / Thesqrt), 2)
		c.y = round((self.y / Thesqrt), 2)
		c.z = round((self.z / Thesqrt), 2)
		c.w = round((self.w / Thesqrt), 2)
		return c