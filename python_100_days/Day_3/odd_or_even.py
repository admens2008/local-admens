#!/usr/bin/python3

#Checks to see if a number is odd or even

number = int(input("Which number do you want to check: "))

if number % 2 == 0:
	print(f"{number} is an EVEN number.")
else:
	print(f"{number} is an ODD number.")
