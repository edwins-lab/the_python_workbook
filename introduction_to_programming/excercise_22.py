import math
s1=float(input("Enter the length of side s1"))
s2=float(input("Enter the length of side s2"))
s3=float(input("Enter the length of side s3"))
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("The area of the triangle is ",area)



