#  Write a program that tests the compatibility between two people.
#  To work out the love score between two people:
#  Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#  Then check for the number of times the letters in the word LOVE occurs. 
#  Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
joined_names = (name1 + name2).lower()

t = joined_names.count("t")
r = joined_names.count("r")
u = joined_names.count("u")
e = joined_names.count("e")

true_score = t + r + u + e

l = joined_names.count("l")
o = joined_names.count("o")
v = joined_names.count("v")
E = joined_names.count("e")

love_score = l + o + v + E

combined_score = int (str(true_score) + str(love_score))

if combined_score < 10 or combined_score > 90:
    print(f'Your score is {combined_score}, you go together like coke and mentos.')
elif combined_score >= 40 and combined_score <= 50:
    print(f'Your score is {combined_score}, you are alright together.')
else:
    print(f'Your score is {combined_score}.')
