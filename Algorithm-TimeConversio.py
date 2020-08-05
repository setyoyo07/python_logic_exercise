#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s
    pm = 0
    if 'PM' in time:
        pm = 12

    time = time[:-2].split(':')

    if time[0] == '12':
        time[0] = 0

    time[0] = str(int(time[0]) + pm)

    newtime = str()
    for x in time:
        newtime += x + ':'

    if len(newtime) < 9:
        newtime = '0' + newtime

    return (newtime[:-1])

s = input()

result = timeConversion(s)

print(result)
