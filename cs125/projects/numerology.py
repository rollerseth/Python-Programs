# File: numerology.py
# Date: 9/21/17
# Author: Seth Roller
# Purpose: To find the numeric value of a name through a loop and if statement
 
def main():
    print()

    print("Program to calculate the numeric value of a name.")
    print("You will be asked to enter a name.")
    print("Written by Seth Roller.")
    print()
    
    name = input("Enter a name:  ")
    print()
    print()

    # name.lower() changes the name into all lowercase letters

    name_low = name.lower()

    print("Original name:", name)

    # assigning a value to a holding variable

    name_val = 0

    # Dr. Koch helped me with the writing the if statement below

    # Dr. Koch also helped me place the if statement in the correct place
    
    # I subtract by 96 due to the values of lowercase letters starting at 97

    # 3 test cases were performed: Seth Roller, John, and Rich Smith

    # The values were respectively 132, 47, and 107
    
    for numbers in name_low:
        if numbers >= 'a' and numbers <= 'z':
            name_val = ord(numbers) - 96 + name_val
    print("Numeric value:", name_val)
     
    print() 
    
main()
