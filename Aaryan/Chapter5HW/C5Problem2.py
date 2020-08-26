#!/usr/bin/env python3
def daysOfTheWeek(x):
  if x == 0:
      return("Sunday")
  elif x == 1:
      return("Monday")
  elif x == 2:
      return("Tuesday")
  elif x == 3:
      return("Wednesday")
  elif x == 4:
      return("Thursday")
  elif x == 5:
      return("Friday")
  elif x == 6:
      return("Saturday")
  else:
      return("Invalid input")
def vacation():
  EnterDay = int(input("Input the day of the week."))
  VacationLength = int(input("Input the amount of time you are on vacation."))
  ReturnDate = (EnterDay + VacationLength) % 7
  print(daysOfTheWeek(ReturnDate))
vacation()
