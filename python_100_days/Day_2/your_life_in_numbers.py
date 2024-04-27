#!/usr/bin/python3
#Life in weeks assuming lifespan is 90
age = int(input("Wat is your current age? "))

year_left = 90 - age
days_left = 365 * year_left
weeks_left = year_left * 52
month_left = year_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {month_left} months left")
