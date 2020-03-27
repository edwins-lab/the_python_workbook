pressure=float(input("Enter the pressure"))
volume=float(input("Enter the volume"))
temp=float(input("Enter the temperature"))
temp1=temp+273.15
n=(pressure*volume)/(8.314*temp1)
print("The number of moles in gas is",n)


