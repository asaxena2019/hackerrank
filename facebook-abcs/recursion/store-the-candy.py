#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findNumJars' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER count
#  2. INTEGER capacity
#

def findNumJars(count, capacity):
    # Write your code here
    if count <= capacity:
        return 1
    else:
        return findNumJars(count//2, capacity) + findNumJars(count-(count//2), capacity)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = int(input().strip())

    result = findNumJars(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
