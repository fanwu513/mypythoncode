#!/usr/bin/env python3
## create file object in "r"ead mode

files = input("Enter file name")

with open(files, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

file = open(files, "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

print(line_count)

print("Number of lines are ", line_count)

## each item of the list now has the "\n" characters back
print(configlist)

