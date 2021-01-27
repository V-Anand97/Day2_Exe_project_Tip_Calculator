from typing import Union

print("Welcome to Tip Calculator")
initial_bill= float(input("What was the total bill?\n "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15 ?\n"))
split= int(input("How many people to split the bill ?\n"))
tip_percentage = float (tip/100)
final_bill = float(tip_percentage *initial_bill) + initial_bill
individual_due = float(round((final_bill/split),2))
# print('individual_due: ', individual_due)
print(f"Each person should pay {individual_due}")