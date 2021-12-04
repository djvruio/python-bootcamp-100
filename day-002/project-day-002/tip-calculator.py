# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60 
# https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

print("-- Welcome to the tip calculator --")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))
bill_with_tip = bill * tip / 100 + bill
bill_per_person = round(bill_with_tip / people_to_split, 2)
message = f"Each person should pay: ${bill_per_person:.2f}"
print(message)



