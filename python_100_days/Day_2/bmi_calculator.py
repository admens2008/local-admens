#!/usr/bin/python3
#BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi_calc = weight / (height * height) 
# bmi_as_int = int(bmi_calc)
# print(bmi_as_int)
bmi_final = round(bmi_calc, 2) #round off to 2 decimal places
print(bmi_final)
