# File: encode.py
# Date: 9/26/17
# Author: Seth Roller
# Purpose: To encode and decode a message for a user with a specific key

def main():
    print()
    print("This program will encode a message using")
    print("a Caesar cipher.")
    print("You will enter a key (number between 1 and 25).")
    print("Written by Seth Roller")
    print()

    key = int(input("Enter a key (number between 1 and 25): "))
    print()
    print() # for turnin

    # if statements are checking the key 
    
    if key >= -25:
        if key <= 25:
            
    
            plaintext = input("Enter a sentence: ")
            print()
            print()

            print("With a key of", key)
            print()

            # makes the sentence entirely lowercase 

            small = plaintext.lower()

            print("Original line:", small)
            print()

            cipher_text = ""

            # if statements within a loop to encode the message

            for ch in small:
                outChar = ch

                if ch >= "a":
                    if ch <= "z":
                        num = ord(ch) + key
                        outChar = chr(num)

                        if outChar > "z":
                            outChar = chr(num - 26)

                        if outChar < "a":
                            outChar = chr(num + 26)



                cipher_text = cipher_text + outChar

            print("Encoded line: ", cipher_text)

            # else statements inform user of invalid input
            
        else:
            print("Error: key must be between -25 and 25, not", key)
    else:
        print("Error: key must be between -25 and 25, not", key)
        
    print()
    

main()
