import random
from hangman_words import word_list
from hangman_art import logo, stages
import os

print(logo)

chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is "{chosen_word}"')

display = []
end_of_game = False
lives = 6

for letter in chosen_word:
        display.append("_")

while not end_of_game: 
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
        print(f'You\'ve already guessed "{guess}" letter.')
    # check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position} Current letter: {letter} Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed "{guess}" that\'s not in the word.\nYou lose a life. Remaining lives: {lives}')
        if lives == 0:
            end_of_game = True
            print("You lose :-(")
            print(f"Word to guess was: {chosen_word}")

    print(f'Your word guess: {display}')
    
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])