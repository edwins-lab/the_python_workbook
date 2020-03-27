n=str(input('Enter the month'))
if n=='jan' or n=='mar' or n=='apr' or n=='may' or n=='jun' or n=='jul' or n=='aug' or n=='sep' or n=='oct' or n=='nov' or n=='dec':
	print(n,'has 31 days')
elif n=='feb':
	print(n,'has 28 days')
else:
	print('error')
