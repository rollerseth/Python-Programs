# File: checkerboard.py
# Date: 11/14/17
# Author: Seth Roller
# Purpose: To create a checkerboard theme through for loops 

def intro():
    print()
    print("This program will display a checkerboard.")
    print("You will enter the number of rows, columns,")
    print("block size and the checkerboard character.")
    print("Written by Seth Roller.")
    print()


def getInput():
    rows = int(input("How many rows? "))
    print()
    cols = int(input("How many columns? "))
    print()
    size = int(input("What is the block size? "))
    print()
    character = input("What is the checkerboard character? ")
    print()
    print()

    return rows,cols,size,character



def checkerboard(rows, cols, size, character):
    for r in range(rows):
        if r % 2 == 0:
            writeRow(cols, size, character)
        else:
            writeRowIndented(cols, size, character)


def writeRow(cols, size, character):
    line = ""
    for c in range(cols):
        if c % 2 == 0:
            line = line + size * character
        else:
            line = line + size * " "

    for b in range(size):
        print(line)
    

    


def writeRowIndented(cols, size, character):
    line = ""
    for c in range(cols):
        if c % 2 == 1:
            line = line + size * character
        else:
            line = line + size * " "

    for b in range(size):
        print(line)



def main():
    intro()
    rows,cols,size,character = getInput()
    checkerboard(rows, cols, size, character)
    print()





main()


