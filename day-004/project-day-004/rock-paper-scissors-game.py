import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if human_choice == 0:
    print(rock)
elif human_choice == 1:
    print(paper)
elif human_choice == 2:
    print(scissors)
else:
    print("Does not exists what you choose :(")

print(f"Computer choose: {computer_choice}")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("Does not exists what the computer choose :(")

# apply rules
if human_choice == 0 and computer_choice == 2: # rock wins againts scissors
    print("You win!!")
elif human_choice == 1 and computer_choice == 0: # paper wins againts rock
    print("You win!!")
elif human_choice == 2 and computer_choice == 1: # scissors wins againts paper
    print("You win!!")
elif human_choice == computer_choice:
    print ("Ties, nobody wins")
elif human_choice >=3 or human_choice < 0:
    print("You typed and invalid number, you lose!!")
else:
    print("You lose")

