#Number Guessing Game Objectives:

# Include an ASCII art logo.
# For logo creation use http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def create_random_number():
    return random.randint(1, 100)

def check_answer(number_to_guess, user_answer):
    if number_to_guess == user_answer:
        return 1 #you win
    elif number_to_guess > user_answer:
        return 2 #too low
    else:
        return 3 #too high 

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def guessing_number_game():
    
    number_to_guess = create_random_number()
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f'pssst, number to guess is:{number_to_guess}')
    
    number_of_attempts = set_difficulty()
    is_number_guessed = False

    while not is_number_guessed and number_of_attempts > 0:
        
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_answer = int(input("Make a guess: "))

        if check_answer(number_to_guess, user_answer) == 1:
            print(f"You got it! The answer was {user_answer}")
            is_number_guessed = True
        elif check_answer(number_to_guess, user_answer) == 2:
            print("Too low")
            is_number_guessed = False
            number_of_attempts -= 1
        else:
            print("Too high")
            is_number_guessed = False
            number_of_attempts -= 1

    if number_of_attempts == 0:   
        print("You've run out of guesses, you lose.")

guessing_number_game()