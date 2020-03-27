dy=10.5
hy=int(input('Enter the no of human years'))
hy1=hy-2
if  hy>0 and hy<=2:
	dy=10.5
elif hy>=3:
	dy=dy+hy1*4
print('the equivalent dog year is',dy)
if hy<=0:
	print('Invalid Input')
 
