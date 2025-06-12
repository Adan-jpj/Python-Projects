# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [1,2,34234,53,623423,64,745,45,55]

def greater(a, b):
    if (a>b):
        return a 
    return b

print(reduce(greater, l))
