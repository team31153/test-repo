#!/usr/bin/env python3
n = int(input("Please enter the number of your day\n "))
print("%s is... " % n)
if n == 0:
  print("Sunday")
elif n == 1:
 print("Monday")
elif n == 2:
 print("Tuesday")
elif n == 3:
 print("Wednesday")
elif n == 4:
 print("Thursday")
elif n == 5:
 print("Friday")
elif n == 6:
 print("Saturday")
else:
 print("not a valid day number")
