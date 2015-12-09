import math

class Vector3(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __add__(self, other):
		c = Vector3(0,0,0)
		c.x = other.x + self.x
		c.y = other.y + self.y
		c.z = other.z + self.z
		return c	
	
	def __sub__(self, other):
		c = Vector3(0,0,0)
		c.x = self.x - other.x
		c.y = self.y - other.y
		c.z = self.z - other.z
		return c
		
	def __mul__(self, other):
		c = Vector3(0,0,0)
		c.x = self.x * other.x
		c.y = self.y * other.y
		c.z = self.z * other.z
		return c
		
	def __truediv__(self, other):
		c = Vector3(0,0,0)
		c.x = round((self.x / other.x), 2)
		c.y = round((self.y / other.y), 2)
		c.z = round((self.z / other.z), 2)
		return c
		
	def Magnitude(self):
		Thesqrt = 0
		A = 0
		A = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
		Thesqrt = round((math.sqrt(A)), 2)
		return Thesqrt
		
	def Normal(self):
		c = Vector3(0,0,0)
		Thesqrt = 0
		A = 0
		A = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
		Thesqrt = math.sqrt(A)
		c.x = round((self.x / Thesqrt), 2)
		c.y = round((self.y / Thesqrt), 2)
		c.z = round((self.z / Thesqrt), 2)
		return c
		
	def DotP(self, b):
		A = 0
		A = (self.x * b.x) + (self.y * b.y) + (self.z * b.z)
		return A
		
	def Cross(self, b):
		c = Vector3(0,0,0)
		t = Vector3(0,0,0)
		Cr = Vector3(0,0,0)
		c.x = self.y * b.z;
		t.x = self.z * b.y;
		Cr.x = c.x - t.x;
		c.y = self.z * b.x;
		t.y = self.x * b.z;
		Cr.y = c.y - t.y;
		c.z = self.x * b.y;
		t.z = self.y * b.x;
		Cr.z = c.z - t.z;
		return Cr;
		
	def Terp(self, b):
		