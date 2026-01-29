# Anne Tran (UCID: 30286177)
# DATA 221_Assignment 1_Q1

threshold=100
product=1
currentNumber=1

while product <= threshold: # product less than & equal to 100
    product*=currentNumber
    currentNumber+=1 # add 1 values after multiplying

print(f"Final product: {product}")
print(f"The integer that caused the product exceed the threhold: {currentNumber} ") # print the last number once the prouct exxceed 100