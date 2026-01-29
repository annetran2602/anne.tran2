# Anne Tran (UCID 30286177)
# DATA 221_Assignment 1_Q3

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
def exponential(x,y): # define power function
    return x**y

result=[]
for x,y in pairs: # extract x,y from the list
    if y<0: # remove any y less than 0
        continue
    result.append(exponential(x,y)) # power result add to a list
print(result) # print result



