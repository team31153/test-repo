#!/usr/bin/env python3

day_number = int(input("Please enter day number: "))
daysAway = int(input("Please enter how long you are away in days: "))
finalDay = -1
day_number1 = -1

def calculate(day_number, daysAway):
    finalDay = (daysAway % 7) + day_number
    finalDay = finalDay % 7
    print(finalDay)
    if finalDay == 0:
        print("Day is Sunday.")
    elif finalDay == 1:
        print("Day is Monday.")
    elif finalDay == 2:
        print("Day is Tuesday.")
    elif finalDay == 3:
        print("Day is Wednesday.")
    elif finalDay == 4:
        print("Day is Thursday.")
    elif finalDay == 5:
        print("Day is Friday.")
    elif finalDay == 6:
        print("Day is Saturday.")


calculate(day_number, daysAway)
