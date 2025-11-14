#Solving Array - DS
#!/bin/python3

#entire import is taken from hackerrank DB
import math
import os
import random
import re
import sys

# Complete the 'reverseArray' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.

def reverseArray(a):
    # Write your code here
    n = len(a) #find length of an a using len)() we assign it in the n
    temp = [0]*n #assign in the temporary. n is multiplying inside the box [] and as 0
    
    for i in range(n): #loop the n & temp 
        temp[i] = a[n-i-1] #make reversed array by using this syntax
        
    for i in range(n):
        a[i] = temp[i] #put the reversed number by loop into the def a
        
    return a
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()