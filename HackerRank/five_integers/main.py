#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimun_sum = arr
    maximun_sum = arr
    
    minimun_sum.sort()
    print(f'{sum(minimun_sum[0:4])}',end="")
    maximun_sum.sort(reverse=True)
    print(f' {sum(maximun_sum[0:4])}')
  
   

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
