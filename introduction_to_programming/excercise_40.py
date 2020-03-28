sound = int(input('enter the sound level in db'))
if sound==130:
	print('Jackhammer')
elif sound==106:
	print('gas lawnmower')
elif sound==70:
	print('alarm clock')
elif sound ==40:
	print('quiet room')
elif sound>40 and sound <70:
	print('range between quiet room and alarm clock')
elif sound>70 and sound <106:
	print('range between alarm clock and lawn mover')
elif sound >106 and sound<130:
	print('range between lawnmower and jackhammer')
else:
	print('error')
