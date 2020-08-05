#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    for num in arr:
        if num > 0:
            positiveCount += 1
        elif num < 0:
            negativeCount += 1
        else:
            zeroCount += 1
    print("{0:.6f}".format(positiveCount/len(arr)))
    print("{0:.6f}".format(negativeCount/len(arr)))
    print("{0:.6f}".format(zeroCount/len(arr)))
    
n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
