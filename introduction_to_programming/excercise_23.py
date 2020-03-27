import math
length=float(input("Enter the length of the sides"))
sides=int(input("Enter the number of sides"))
area=(sides*length**2)/4*math.tan(math.pi/sides)
print(area)
