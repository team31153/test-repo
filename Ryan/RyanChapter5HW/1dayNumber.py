#!/usr/bin/env python3

day_number = int(input("Please enter day number: "))

def dayNumber(day_number):
    if day_number == 0:
        print("Day is Sunday.")
    if day_number == 1:
        print("Day is Monday.")
    if day_number == 2:
        print("Day is Tuesday.")
    if day_number == 3:
        print("Day is Wednesday.")
    if day_number == 4:
        print("Day is Thursday.")
    if day_number == 5:
        print("Day is Friday.")
    if day_number == 6:
        print("Day is Saturday.")

dayNumber(day_number)
