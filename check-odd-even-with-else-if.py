# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

if __name__ == '__main__':
    n = int(input().strip())

#using modulo operator
#remember always add +1 to each end number because python starts counting from 0
if n % 2 != 0:
    print("Weird")
elif n in range(2, 6): #asked range 2 to 5 but we put 2, 6
    print("Not Weird")
elif n in range(6, 21): #asked range 6 to 20 but we put 2, 6
    print("Weird")
elif n > 20:
    print("Not Weird")
            