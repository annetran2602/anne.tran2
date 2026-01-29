# Anne Tran (UCID: 30286177)
# DATA 221_Assignment 1_Q7


#Global variable & constant
HRS_TO_SECONDS=3600
MINS_T0_SECONDS=60

def convert(seconds):
    hours=0
    mins=0


    # Convert to hrs
    hours=seconds//HRS_TO_SECONDS
    if hours<1:
        hours=0
    else:
        seconds=seconds-(hours*HRS_TO_SECONDS)

    if hours >=12:
        dayNight="PM"
    else:
        dayNight="AM"

    # Convert to mins
    mins=seconds//MINS_T0_SECONDS
    if mins<1:
        mins=0
    else:
        seconds=seconds-(mins*MINS_T0_SECONDS)
    return hours, mins, seconds, dayNight

def main():
    seconds = 7260
    seconds=float(input("Enter the seconds"))
    while not int(seconds):
        print("Invalid type of input!!! Has to be an integer")
        seconds=float(input("Enter the seconds"))
    while seconds < 0:
        print("Invalid input!!! Input must be greater than and equal to 0")
        seconds=float(input("Enter the second"))
    hours, mins, seconds, dayNight=convert(seconds)
    print(f"{hours:.0f} {mins:.0f} {seconds:.0f} {dayNight}")
main()


