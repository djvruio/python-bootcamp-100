# BMI Calculator
# Program that calculates the Body Mass Index (BMI)
# from a user's weight and height
# BMI = weight (kg) / height ^2 (m^2) 

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_number = float(height)
weight_number = float(weight)

BMI = weight_number / height_number ** 2
BMI_int = int(BMI)

print(BMI_int)