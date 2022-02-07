# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 5 to 20, print Weird
# If  is even and greater than 20 , print Not Weird
# Constraints
# 1 <= n <= 100
# Input -> Ouput
# 3     -> Weird
# 24    -> Not Weird

# import math
# import os
import random

n = random.randint(1, 100)
print(f'The random number is: {n}')

if n >= 1 and n <= 100:
    if n % 2 == 0  and n > 20:
        print("Not Weird")
    if n % 2 == 0 and n in range(6,21,1):
        print("Weird")
    if n % 2 == 0 and n in range(2,6,1):
        print("Not Weird")
    if n % 2 != 0:
        print("Weird")
    
    
    
    