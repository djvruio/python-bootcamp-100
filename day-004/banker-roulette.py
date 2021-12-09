
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.replace(" ", "") #added
names = names.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenght_list = len(names)
toss = random.randint(0, lenght_list - 1)
person_selected = names[toss]
print(f'{person_selected} is going to buy the meal today!')



