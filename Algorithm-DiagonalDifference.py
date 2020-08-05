#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    dimension = len(arr)
    primaryDiagonal = 0
    secondaryDiagonal = 0
    for i in range(0,dimension):
        primaryDiagonal += arr[i][i]
        secondaryDiagonal += arr[i][dimension-1-i]
    return abs(primaryDiagonal - secondaryDiagonal)

n = int(input("Dimension of Array: ").strip())

arr = []

print("Array Input : ")
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(str(result))

"""
limit: array input only takes inputs in the order of their dimensions
Example test case
input:
Dimension : 3
Array Input :
1 2 3
4 5 6
7 8 9
output:
0
because (1+5+9) - (3+5+7) = 0
"""