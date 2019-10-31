# File: pizza.py
# Date: 9/28/17
# Author: Seth Roller
# Purpose: To calculate the cost per square inch of a pizza

import math #imported the math library to use pi

def main():
    print()
    print("Program to calculate the area and cost")
    print("per square inch of a pizza.")
    print("You will be asked to enter the diameter")
    print("of the pizza in inches and the cost in dollars.")
    print("Written by Seth Roller.")
    print()

    diam = float(input("Enter the diameter (in inches): "))
    print()
    print()
    
    money = float(input("Enter the cost (in dollars): "))
    print()
    print()

    area = (math.pi) * (diam / 2)**2

    # finding the area of the pizza by the area formula of a circle 
    
    cost = money / area

    # the if statements determine whether to print the diameter as an integer
    # or a float number
    # the formating function was obtained from ch. 5 section 8 of the book
    
    if diam > int(diam):
        print("For a diameter of",diam, "inches")
    else:
        print("For a diameter of",int(diam), "inches")
    print("and a cost of ${0:0.2f}:".format(money))
    print("Area in square inches: {0:0.3f}".format(area,))
    print("Cost per square inch:  ${0:0.2f}".format(cost))

    print()

    
main()
