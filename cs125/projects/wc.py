x# File: wc.py
# Date: 10/5/17
# Author: Seth Roller
# Purpose: To count the number of lines, words, and characters in a file 

def main():
    print()
    print("Program to calculate the number of newlines,")
    print("words and characters in a file")
    print("You will be asked to enter the name of a file.")
    print("Written by Seth Roller.")

    print()

    # asking the user to input a file name

    file = input("Enter the name of a file: ")
    print()
    print()

    file_read = open(file,"r")

    line_count = 0
    char_count = 0
    word_count = 0 

    for counting in file_read:
        line_count = line_count + 1
        
        # each time the loop goes through a line line_count adds 1
        
        word_count = word_count + len(counting.split())

        # I split up all the words in file_read and took the length
        # this gives the number of words in the file
        
        char_count = char_count + len(counting)

        # I took the length of the entire file
        # this counts every character/byte
        
    print("",line_count,word_count,char_count,file)

    file_read.close()
    
    print()
        
main()
