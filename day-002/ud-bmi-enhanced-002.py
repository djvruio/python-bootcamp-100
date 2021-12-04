# BMI Calculator
# Program that calculates the Body Mass Index (BMI)
# from a user's weight and height
# BMI = weight (kg) / height ^2 (m^2) 

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight) / float(height) ** 2
print(int(BMI))