# Anne Tran (UCID 30286177)
# DATA 221_Assignment1_Q5

import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    # Calculate area
    area1=(radiusOfCircle1**2)*math.pi
    area2=(radiusOfCircle2**2)*math.pi

    # Calculate the percentage of the larger circle's area to the smaller one
    percentage=0
    if area1<area2: # Check if area1 is smaller than area2
        percentage=(area1/area2)*100
    elif area1>area2: # Check if area2 is smaller than area1
        percentage=(area2/area1)*100
    elif area1==area2: # Check if both areas are equal
        percentage=100
    return percentage # print out the result

def main():

    # Input radius of circle 1 & validate
    radiusOfCircle1 = float(input("Enter radius of circle 1"))
    while not int(radiusOfCircle1):
        print("Invalid radius values!!! Have to be integers")
        radiusOfCircle1 = float(input("Enter radius of circle 1"))

    while radiusOfCircle1<0:
        print("Invalid radius values!!! Have to be positive")
        radiusOfCircle1 = float(input("Enter radius of circle 1"))

    # Input radius of circle 2 & validate
    radiusOfCircle2 = float(input("Enter radius of circle 2"))
    while not int(radiusOfCircle2):
        print("Invalid radius values!!! Have to be integers")
        radiusOfCircle2 = float(input("Enter radius of circle 2"))

    while radiusOfCircle2<0:
        print("Invalid radius values!!! Have to be positive")
        radiusOfCircle2 = float(input("Enter radius of circle 2"))

    percent=circleAreaCoverage(radiusOfCircle1, radiusOfCircle2)
    print(f"The coverage percentage is {percent:.02f}%") # print the result
main()



