# File: sqrt2.py
# Date: 11/9/17
# Author: Seth Roller
# Purpose: Find the square root of a number through a series and math library

import math

def intro():
    print()
    print("Program to approximate the square root of 1 + x.")
    print("(|x| must be less than 1)")
    print("You will be asked to enter the value of x and")
    print("the number of terms.")
    print("Written by Seth Roller")
    print()

# Separated where I get my numbers,
# computing the actual, and the approx.  
    
def numbers():
    while True:
        value = float(input("Enter the value of x (|x| < 1): "))
        if abs(value) < 1:
            print()
            terms = int(input("Enter the number of terms to use: "))
            return value,terms
            break
        else:
            print()
            print()
            print("You entered",value,"you have to enter a", end = "")
            print(" number less than 1 and greater than -1.")
            print()
            break    
        break
def approximate(value,terms):
    approx = 0
    for b in range(terms):
        top_co = (((-1) ** b * factorial(2 * b)) * value ** b)
        bottom_co = ((1 - (2 * b)) * (factorial(b)) ** 2 * 4 ** b)
        approx = approx + top_co / bottom_co
    return approx
        
def factorial(n):
    # compute n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    # got this from lab 10 
    if n < 0:
        print ("ERROR! Factorial undefined for negative values!")
        return -1
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(n, 0, -1):  # loop from n downto 1
            product = product * i
        return product

def actual(value):
    act = math.sqrt(1 + value)
    return act

def printResults(act,approx):
    print("Function     Approx. Value    Actual Value    Difference")
    print("sqrt(1+x) {1:17.12f} {0:16.12f}".format(act,approx), end = "")
    print("{0:17.12f}".format(approx - act))
    return

def main():
    intro()
    # exception handling, if the try fails it goes to except 
    try:
        value,terms = numbers()
        print()
        print()
        print("For",terms,"terms and x is",str(value)+":")
        print()
        approx = approximate(value,terms)
        act = actual(value)
        printResults(act,approx)
        print()
    except:
        print("Try the program again.")
        print()
main()
