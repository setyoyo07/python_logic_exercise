#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    point = [0, 0]
    for i in range(0,len(a)):
        if a[i] > b[i]:
            point[0] += 1
        elif a[i] < b[i]:
            point[1] += 1
    return point

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))

"""
limit: length of a and b must be same
Example test case
input:
1 2 3
3 1 3
output:
1 1
"""