# File: sqrt.py
# Date: 12/5/17
# Author: Seth Roller
# Purpose: We will find the square root of a number inputed by a user

from math import *

def intro():
    print()
    print("This program will calculate the square root")
    print("of a number using Newton's Method.")
    print("You will enter the number and the size of the")
    print("delta between Newton's Method square root")
    print("and the real square root.")
    print("Written by Seth Roller.")
    print()


def getInputs():
    number = float(input("Enter the number to find its square root: "))
    print()
    print()
    delta = float(input("Enter the delta: "))
    print()
    print()
    return number,delta

def calculations(number,delta):
    guess = 1
    times = 0
    while True:
        newGuess = (guess + number / guess) / 2
        times = times + 1
        if abs(guess - newGuess) < delta:
            break
        guess = newGuess
    return newGuess, times

def main():
    intro()
    number,delta = getInputs()
    newGuess,times = calculations(number,delta)
    print("For the square root of",number,"after",times,"tries")
    print("with a delta of {0:0}:".format(delta))
    print("The calculated square root is {0:0.11f}".format(newGuess))
    print("The real square root is",5 *" ","{0:0.11f}".format(sqrt(number)))
    print("The difference is",11 * " ",abs(newGuess- sqrt(number)))
    print()


if __name__ == "__main__":
    main()









