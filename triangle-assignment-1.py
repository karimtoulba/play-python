############################
## Code: Check Numbers    ##
## Author: Karim Toulba   ##
## Date: 28/06/2024       ##
############################

#request input from user
entry = input("Please enter 4-lower-case letters string: ")

#check input 4 letters
if len(entry) == 4:
    print ("Great! The string is 4 letters")
else:
    print ("This is not 4-letters string")

#check input lower-case letters
if (97 <= ord(entry[0]) <= 122) and (97 <= ord(entry[1]) <= 122) and (97 <= ord(entry[2]) <= 122) and (97 <= ord(entry[3]) <= 122):
    print ("Great! The string is lower-case")
else: 
    print ("The string is not lower-case")

#check sorting
sort = True

if (ord(entry[0]) > (ord(entry[1]))) or (ord(entry[1]) > (ord(entry[2]))) or (ord(entry[2]) > (ord(entry[3]))):
    sort = False
else:
    sort = True

#Print

if sort == True:
    print("The value is correct")
else: 
    print ("The value is wrong")

