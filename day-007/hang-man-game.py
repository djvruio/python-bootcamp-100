#TODO-1 Randomly choose a word from the word_list
#and assign it to a variable called chosen_word.

import random

word_list = ["picture", "europe", "ardvark", "baboon", "camel"]

# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)
#Testing code
print(f'the solution is {chosen_word}')

#TODO-2 Ask the user to guess a letter and assign their answer to
#a variable called guess. Make guess lowercase.

display = []
for letter in chosen_word:
        display.append("_")
print(f'display init: {display}')

while ''.join(display) != chosen_word: 
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f'display end: {display}')
    x = ''.join(display)
    print(f'display end str: {x}')
    print(f'chosen word end: {chosen_word}')
print("You win!!!")