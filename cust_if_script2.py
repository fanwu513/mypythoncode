#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

storm = float(input("What is the windspeed\n"))

if storm >= 157:
    print("This is a category 5 hurricane")
elif storm in range(130, 156):
    print("This is a category 4 hurricane")
elif storm in range(111, 129):
    print("This is a category 3 hurricane")
elif storm in range(96, 110):
    print("This is a category 2 hurricane")
elif storm in range(74, 95):
    print("This is a category 1 hurricane")
elif storm in range(39, 73):
    print("This is a tropical storm")
elif storm in range(0, 38):
    print("This is a tropical depression")
else:
    print("The input is not a valid wind speed")
