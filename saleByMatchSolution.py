#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def occurence(val,arr):
    count = 0
    for i in arr:
        if i == val:
            count += 1
    return count

def sockMerchant(n, ar):
    sortedar = sorted(ar)
    count = 0
    
    
    
    nw = [occurence(i,sortedar)//2 for i in set(sortedar) if occurence(i,sortedar)//2 > 0]
    return sum(nw)
        #if sortedar[i] in sortedar:
            #count +=
    #print(nw)   
        #print(nw)
            
    #print(sortedar[])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
