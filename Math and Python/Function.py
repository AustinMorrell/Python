from graphics import *

def GameLoop():
	print("Give me a number of seconds.")
	p = (filename = raw_input())
	h = (p /60) /60
	m = p / 60
	print("Hours = ") 
	print(h)
	print("Minutes = ") 
	print(m)
	print("Seconds = ")
	print(p)