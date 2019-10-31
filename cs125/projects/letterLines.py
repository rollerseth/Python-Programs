# File: letterLines.py
# Date: 11/16/17
# Author: Seth Roller
# Purpose: To take in a file and count the numbers and characters

def intro():
    print()
    print("Program to count letters in each line")
    print("in a file.")
    print("You will enter the name of a file.")
    print("The program will create an output file.")
    print("Written by Seth Roller.")
    print()

def convertName(infileName):
    outfiles = infileName.split(".")
    outfileName = outfiles[0]+".out"
    outfile = open(outfileName, "w")
    return outfileName,outfile 

def retrieve():
    infileName = input("Enter name of input file:  ")
    print()
    outfileName,outfile = convertName(infileName)
    print("The name of the output file is",outfileName)
    print()
    infile = open(infileName, "r")
    return infile,infileName
    

def counting():
    infile,infileName = retrieve()
    outfileName,outfile = convertName(infileName)
    line_count = 0
    number_num = ["0","1","2","3","4","5","6","7","8","9"]
    total = [0,0,0,0,0,0,0,0,0,0]
    for line in infile:
        let_count = 0
        line_count = line_count + 1
        
        # Dr. Koch helped me forumulate this loop
        
        for i in range(len(number_num)):
            total[i] = total[i] + line.count(number_num[i])
            
        for coun in line:
            if ord(coun) >= ord("a") and ord(coun) <= ord("z"):
                let_count = let_count + len(coun)
            elif ord(coun) >= ord("A") and ord(coun) <= ord("Z"):
                let_count = let_count + len(coun)
            
        print("{}: ".format(let_count) + line, file=outfile)
        
    print("Number of lines: {0:>15}".format(line_count))
    
    for b in range(10):
        print("Number of {1:>0}'s:{0:>18}".format(total[b],b))
        
    infile.close()
    outfile.close()
    return

def main():
    intro()
    counting()
    print()

    
main()

