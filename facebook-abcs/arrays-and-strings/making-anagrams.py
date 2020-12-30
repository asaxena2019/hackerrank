#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    total = len(s1) + len(s2)
    count = 0
    s1dict = dict()
    s2dict = dict()
    for elem1 in s1:
        if elem1 in s1dict:
            s1dict[elem1]=s1dict[elem1]+1
        else:
            s1dict[elem1]=1
    for elem2 in s2:
        if elem2 in s2dict:
            s2dict[elem2]=s2dict[elem2]+1
        else:
            s2dict[elem2]=1
    for letter1 in s1:
        if letter1 in s2dict and s2dict[letter1]>0:
            count = count + 1
            s2dict[letter1] = s2dict[letter1] - 1
    for letter2 in s2:
        if letter2 in s1dict and s1dict[letter2]>0:
            count = count + 1
            s1dict[letter2] = s1dict[letter2] - 1
    return total-count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
