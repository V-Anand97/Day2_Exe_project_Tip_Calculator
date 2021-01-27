print("Life In Weeks")
age= int(input('how old are you?\n'))
remainder = 90 - age
months = int(remainder*12)
weeks = int(remainder*52)
days = int(remainder*365)
print(f' You have {days} days, {weeks} weeks and {months} months left')