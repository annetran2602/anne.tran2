# Anne Tran (UCID: 30286177)
# DATA 221_Assignment 1_Q2

def dict(listOfString):
    dict={}
    for str in listOfString:
        length=len(str)
        dict[str]={} # create sublist for each word
        dict[str]['length']=length # the length of each word
        if length%2==0: # check if the num of characters in word is even or odd
            dict[str]['parity']="even"
        else:
            dict[str]['parity']="odd"
    print(dict)

def main():
    listOfString=["data", "science"]
    print(dict(listOfString)) # print the result
main()

