#!/usr/bin/python3

#checking if a year is a leap or not
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
	if year % 100 != 0: #if year isn't cleanly divisible by 100
		print(f"{year} is a leap year")
	else:
		if year % 400 == 0:
			print(f"{year} is a leap year")
		else:
			print(f"{year} is NOT a leap year")
else:
	print(f"{year} is NOT a leap year")
