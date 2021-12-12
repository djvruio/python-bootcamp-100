#Write your code below this row 👇
total_even = 0

for number in range(1, 101):
    if number % 2 == 0:
        total_even += number

print(f'Form 01: {total_even}')

total_even = 0
for number in range(2, 101, 2):
    total_even += number

print(f'Form 02: {total_even}')