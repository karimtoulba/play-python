############################
## Code: Print ASCII Code
## Author: Karim Toulba
## Date: 28/06/2024
############################

char = input("Please enter a single Uppercase Character: ")

if len(char) > 1:
    print ("This is not a single character")

elif ord(char) < 65 or ord(char) > 90:
    print ("This is not a capital character")

else: 
    print ("Character is ", char)
    print ("& ASCII code is ", ord(char))

