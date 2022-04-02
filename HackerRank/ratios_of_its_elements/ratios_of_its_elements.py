#!/bin/python3

import math
import os
import random
import re
import sys


#Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. Print the decimal value of each fraction on a new line with places 
# after the decimal.
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive_numbers = []
    negative_numbers = []
    zero_numbers = []
    for i in arr:
        if i == 0:
            zero_numbers.append(i)
        elif i > 0:
            positive_numbers.append(i)
        else:
            negative_numbers.append(i)
        
    print("{:.6f}".format(len(positive_numbers)/n))
    print("{:.6f}".format(len(negative_numbers)/n))
    print("{:.6f}".format(len(zero_numbers)/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
