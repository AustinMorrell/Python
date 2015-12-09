import Vector2
from Vector2 import *

import Vector3
from Vector3 import *

import Vector4
from Vector4 import *

Me = Vector2(25, 11)
You = Vector2(34, 33)
Sex = Vector2(0, 0)

Me2 = Vector3(25, 11, 50)
You2 = Vector3(34, 33, 42)
Sex2 = Vector3(0, 0, 0)

Me3 = Vector4(25, 11, 50, 13)

def main():

	print("2D Vector Math: ")
	Sex = Me + You
	print("Adding: ", Sex.x, ",", Sex.y)
	
	Sex = Me - You
	print("Subtracting: ", Sex.x, ",", Sex.y)
	
	Sex = Me * You
	print("Multiplication: ", Sex.x, ",", Sex.y)
	
	Sex = Me / You
	print("Division: ", Sex.x, ",", Sex.y)
	
	Sex = Me.Lerp(You)
	print("Linear Interpulation: ", Sex.x, ",", Sex.y)
	
	print("Magnitude: ", Me.Mag())
	
	print("Normalized: ", Me.Norm().x, Me.Norm().y)
	
	print("Dot Product: ", Me.Dot(You), "\n")
	
	#--------------------------------------------------------------------------
	
	print("3D Vector Math: ")
	Sex2 = Me2 + You2
	print("Adding: ", Sex2.x, ",", Sex2.y, ",", Sex2.z)
	
	Sex2 = Me2 - You2
	print("Subtracting: ", Sex2.x, ",", Sex2.y, ",", Sex2.z)
	
	Sex2 = Me2 * You2
	print("Multiplication: ", Sex2.x, ",", Sex2.y, ",", Sex2.z)
	
	Sex2 = Me2 / You2
	print("Division: ", Sex2.x, ",", Sex2.y, ",", Sex2.z)
	
	Sex2 = Me2.Terp(You2)
	print("Linear Interpulation: ", Sex2.x, ",", Sex2.y)
	
	print("Magnitude: ", Me2.Magnitude())
	
	print("Normalized: ", Me2.Normal().x, Me2.Normal().y, Me2.Normal().z)
	
	print("Dot Product: ", Me2.DotP(You2), "\n")
	
	#--------------------------------------------------------------------------
	
	print("4D Vector Math: ")
	print("Normalized: ", Me3.Normalise().w, Me3.Normalise().x, Me3.Normalise().y, Me3.Normalise().z)

main()