#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
wordtemp = ''
def solve(s):
    wordtemp = s
    b = list(s)
    for w in wordtemp:
        if w==' ':
            text=wordtemp.index('w')
            index2 = wordtemp[text]
            index1 = wordtemp[0]
            t = index2.upper()
            c = index1.upper()
            b[0] = c
            b[text] = t
            return "".join(b)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
