#################################
### Code: Is Palindrome        ##
### Author: Karim Toulba       ##
### Date: 29/06/2024           ##
#################################


#enter string palindrome
palindrome = input("Please enter a palindrome: ")

#check palindrome length
palindromeLength = len(palindrome) - 1

#check if it is a text and not a number
if palindrome.isnumeric() == True:
    print ("This is not a text. Please enter a text!")
    exit(0)

#check if it is a palindrome
else:
    while palindromeLength > 0 : 
        #check palindrome length
        palindromeLength = len(palindrome) - 1

        #check if it is a palindrome
        if palindrome[0] == palindrome[palindromeLength]:
            print ( f"{palindrome} is a Palindrome")

        #check if not a palindrome
        elif palindrome[0] != palindrome[palindromeLength]:
            print( f"{palindrome} is not a palindrome")

        #re-ask
        palindrome = input("Please enter a palindrome: ")