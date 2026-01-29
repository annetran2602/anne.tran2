# Anne Tran (UCID 30286177)
# DATA 221_Assignment 1_Q4

from random import random # Import library
values=[random() for i in range (20)] # Generate list of random numbers
x=random()

values.sort() # sorted the list of random numbers

indexList=[]
for value in values: # check all elements in the sorted list
    if value >= x: # check if any elements
        index=values.index(value) # index of elements greater than and equal to x
        indexList.append(index) # add to the list of index of values greater than and equal to x


print(f"Sorted list is {values}") # print sorted value
print(f"The value of x is {x}") # print value of x
print(f"The first matching index is {indexList[0]} ") # print the index of first value in the list greater than and equal to x