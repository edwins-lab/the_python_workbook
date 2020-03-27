import math
t1=float(input("Enter the latitude of  first point"))
g1=float(input("Enter the longitude of first point"))
t2=float(input("Enter the latitude of second point"))
g2=float(input("Enter the longitude of second point"))
ft1=math.radians(t1)
fg1=math.radians(g1)
ft2=math.radians(t2)
fg2=math.radians(g2)
distance=6371.01*math.acos(math.sin(ft1)*math.sin(ft2)+math.cos(ft1)*math.cos(ft2)*math.cos(fg1-fg2))
print("Distance between point1 and point2 is",distance)


