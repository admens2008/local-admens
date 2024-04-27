#!/usr/bin/python3
#A Tip calclator

print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
gross_bill = (tip_percentage / 100) * bill + bill
qty_to_split = int(input("How many people to split the bill? "))
final_bill = gross_bill / qty_to_split
# final_bill_rnd_off = round(final_bill, 2)
final_bill_rnd_off = "{:.2f}".format(final_bill) #to make sure we get 2 decimals
print(f"Each person should pay: ${final_bill_rnd_off}")
