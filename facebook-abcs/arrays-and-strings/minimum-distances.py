#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    minDist = -1
    track = dict()
    for i in range(len(a)):
        if a[i] in track:
            if minDist==-1 or i-track.get(a[i])<minDist:
                minDist = i-track.get(a[i])
        else:
            track[a[i]] = i
    return minDist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
