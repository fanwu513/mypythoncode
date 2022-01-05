#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

grade = input("What is your grade\n")

if grade == "A":
    print("You received a score between 90-100")
elif grade == "B":
    print("You received a score between 80-89")
elif grade == "C":
    print("You received a score between 70-79")
elif grade == "D":
    print("You received a score between 60-69")
elif grade == "F":
    print("You received a score of 59 or below")
else:
    print("You did not provide a grade")
