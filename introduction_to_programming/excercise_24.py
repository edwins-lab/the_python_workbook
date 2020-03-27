days=float(input("enter the number of days"))
hours=float(input("enter the number of hours"))
minutes=float(input("Enter the number of minutes"))
sec1=float(input("Enter the number of seconds"))
sec2=days*86400
sec3=hours*3600
sec4=minutes*60
sec=sec1+sec2+sec3+sec4
print("the total no of seconds is",sec)
