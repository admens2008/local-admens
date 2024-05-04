#!/usr/bin/python3

#Conditional Statements--checking if one is eligible and the price associated 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm: "))
bill = 0


if height >= 120:
	print("You can ride the rollercoster")
	age = int(input("What is your age?: "))
	if age < 12:
		print("Children's tickets are $5.")
		bill = 5
	elif age <= 18:
		print("Youth's tickets are $7.")
		bill = 7
	#providing free ride for persons btn 45 and 55
	elif age >= 45 and age <= 55:
		print("Ride free- your ticket is $0")
		#bill = 0
	else:
		print("Adult's tickets are  $12")
		bill = 12
	#adding extra ticket to persons who want to take photos
	photo = input("Do you want to take photos? Y/N: ").lower()
	if photo == "y":
		bill += 3
	print(f"Your bill is ${bill}")
else:
	print("Sorry, you have to grow taller before you can ride.")
