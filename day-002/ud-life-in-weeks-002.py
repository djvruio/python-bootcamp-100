# Calculate how many days, weeks and months left if we live 90 years old.
# https://waitbutwhy.com/2014/05/life-weeks.html

age = input("What is your current age?")

#calculate days left if we live until 90 years old

days_until_today = float(age) * 365
days_until_90 = 90 * 365
days_left = days_until_90 - days_until_today 

# Calculate weeks left if we live until 90 years old

weeks_until_today = float(age) * 52
weeks_until_90 = 90 * 52
weeks_left = weeks_until_90 - weeks_until_today

# Calculate months left if we live until 90 years old

months_until_today = float(age) * 12
months_until_90 = 90 * 12
months_left = months_until_90 - months_until_today  

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")