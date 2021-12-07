# Leap Year - Año Bisiesto
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.

# 1. See if the number is evenly divisible by 4.
#    1997/4 = 499.25 It's not a leap year
#    2000/4 = 500 It's likely a Leap year
# 2. Confirm the number isn't evenly divisible by 100. 
#    If a year is evenly divisible by 4, but it is not evenly divisible 100, then it is a leap year. 
#    If a year is divisible by both 4 and 100, then it might not be a leap year, and you will have to
#    perform 1 more calculation to check.
# 3. Check if the number is evenly divisible by 400 to confirm a leap year. 
#    If a year is divisible by 100, but not 400, then it is not a leap year. 
#    If a year is divisible by both 100 and 400, then it is a leap year.

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if (year / 100).is_integer():
        if (year / 400).is_integer():
            print(f'Leap year.')
        else:
            print(f'Not leap year.')
    else:
        print(f'Leap year.')
else:
     print(f'Not leap year.')