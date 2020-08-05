#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    resultArray = []
    for i in range(0, len(arr)):
        sum = 0
        for j in range(0, len(arr)):
            if i != j:
                sum += arr[j]
        resultArray.append(sum)
    
    print(min(resultArray), max(resultArray))

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
