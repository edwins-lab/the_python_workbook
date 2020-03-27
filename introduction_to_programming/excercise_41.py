s1=float(input('Enter the first side length of triangle'))
s2=float(input('Enter the second side length of triangle'))
s3=float(input('Enter the third side length of triangle'))
if s1==s2 and s2==s3 and s3==s1:
	print('its a equvilateral triangle')
elif  s1!=s2 and s2!=s3 and s3!=s1:
	print('scalene')
else:
	print('isosceles')


