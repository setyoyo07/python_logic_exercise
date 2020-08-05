#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k = 1
    for i in range(0,n):
        for j in range(0,n):
            if j < n-k:
                print(" ", end='')
            else:
                print("#", end= '')
        k += 1
        print("\n", end='')

n = int(input())

staircase(n)
