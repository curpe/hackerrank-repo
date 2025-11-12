#To find the sum of elements in an array of integers in Python

def simpleArraySum(ar):
    # Write your code here
    
    tot_sum = 0
    
    for element in ar:
        tot_sum += element
    return tot_sum