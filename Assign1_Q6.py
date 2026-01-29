# Anne Tran (UCID: 30286177)
# DATA 221_Assignment 1_Q6

numbers=[3,1,2,3,4,2] # input

def createDict(numbers):

    # Remove duplicate num from the list
    nonDuplicatedNumbers=[] # list contain unique num
    for num in numbers:
        if num not in nonDuplicatedNumbers:
            nonDuplicatedNumbers.append(num)

    # Sorted list (from smallest to largest)
    nonDuplicatedNumbers.sort()

    # Calculate percentage
    percentageList=[]
    total=len(numbers)
    dict={}
    for num in nonDuplicatedNumbers: # 1,2,3,4
        countNum=0
        for number in numbers: # 3,1,2,3,4,2
            if num>=number:
                countNum+=1 #count the number less than or equal to num
        percentage=(countNum/total)*100

        #Create dict
        dict[num]=f"{percentage:.02f}%"
    return dict

print(createDict(numbers))