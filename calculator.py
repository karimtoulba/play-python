###############################
# Code: Calculator using if   #
# Author: Karim Toulba        #
# Date: 28/06/2024            #
###############################

# ask customer to enter the variables as int
varA = int(input("Please enter the variable A: "))
varB = int(input("Please enter the variable B: "))
varC = int(input("Please enter the variable C: "))
varX = int(input("Please enter the variable X: "))

# finding the maximum number
if varA > varB and varA > varC and varA > varX:
    print("The maximum number is A which is " + str(varA))
elif varB > varA and varB > varC and varB > varX:
    print ("The maximum number is B which is" + str(varB))
elif varC > varA and varC > varB and varC > varX:
    print ("The maximum number is C which is " + str(varC))
else:
    print("The maximum number is X which is " + str(varX))
  
