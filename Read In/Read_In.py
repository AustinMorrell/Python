def main():
	file = open("classNames.txt", "r")
	print(file.read())
	print("Enter a price: ")
	a = input()
	print("Price of Pizza = $", a)
	print("How many slices?: ")
	s = input()
	print("Slices = ", s)
	cost = a / s
	print("1 slice of pizza is: $", cost)
	
main()