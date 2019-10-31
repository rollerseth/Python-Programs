# File: speedboats.py
# Date: 11/30/17
# Author: Seth Roller
# Purpose: To create a table from a file a user inputed 

def intro():
    print()
    print("Program to output a monthly report",end = "")
    print(" of speedboat sales.")
    print("Written by Seth Roller.")
    print()
    filename = input("Enter the file name: ")
    print()
    print()
    print("For the file",filename+":")
    print()
    return filename

def reading():
    filename = intro()
    files = open(filename, "r")
    holdList = []
    for line in files:
        numbers = []
        numbers = numbers + line.split(" ")
        holdList.append(numbers)
    return holdList

def mkTable():
    holdList = reading()
    print(" " * 20 ,"Salesperson")
    print("  Model   :   1   2   3   4   5",end="")
    print("   6   7   8  :  Avg Totals")
    print(58 * "-")
    
    # this loop is to create the body of the table
    
    for i in range(len(holdList)):
        print("{0:5}     :".format(i + 1), end="")
        tot = 0
        for r in range(len(holdList[0])):
            # this is where Dr. Koch told me to use integers
            # instead of strings w/in the format command
            print(" {0:3}".format(int(holdList[i][r])), end="")
            tot = tot + int(holdList[i][r]) 
        print("  :  {0:3.1f}  {1:3}".format(tot / len(holdList[0]),tot))
    print("-" * 58)
    print(" Average  :", end="")

    # this loop is to formulate the avg in columns
    
    for b in range(len(holdList[0])):
        top = 0
        for r in range(len(holdList)):
            top = top + int(holdList[r][b])
            avg = top / len(holdList)
        print(" {0:3.1f}".format(avg), end = "")
        
    print()
    print(" Maximum  :", end = "")
    columns = []

    # this loop is to formulate the max w/in the columns 
    
    for fin in range(len(holdList[0])):
        listt = []
        for s in range(len(holdList)):
            listt.append(holdList[s][fin])
        columns.append(listt)
        print("   {0:1}".format(max(columns[fin])), end = "")
        
    print("  Totals  :", end = "")

    # this loop is to total all the columns

    fin_tot = 0
    
    for tot in range(len(holdList[0])):
        total = 0
        for y in range(len(holdList)):
            total = total + int(holdList[y][tot])
            fin_tot = fin_tot + int(holdList[y][tot]) 
        print("  {0:2}".format(total), end = "")
    print("  :      {0:4}".format(fin_tot), end = "")
    
    print()
    print()
    
def main():
    mkTable()


main()
