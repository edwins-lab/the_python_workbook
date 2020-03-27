airtemp=float(input("Enter the air temperature"))
windspeed=float(input("Enter the wind speed"))
windchill=13.12+0.6215*airtemp-11.37*windspeed**0.16+0.3965*airtemp*windspeed**0.16
wind=int(windchill)
print(wind)
