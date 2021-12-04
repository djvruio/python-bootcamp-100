# Calculate how many days, weeks and months left if we live 90 years old.
# https://waitbutwhy.com/2014/05/life-weeks.html

age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 -age_as_int
days_remainig = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remainig} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(message)