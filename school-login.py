#######################################################
### Code: School Student Login System               ###
### Author: Karim Toulba                            ###
### Date: 01/07/2024                                ###
#######################################################

readiness_checker = input("Are you ready? Enter \"yes\" to proceed: ")

while readiness_checker == "yes":

# Request input from school admin to generate login_name to students + String Validation for firstname and lastname

    try: 
        student_firstname = str(input("Please enter student firt name: "))
        student_lastname = str(input("Please enter student last name: "))
        student_id = input("Please enter student ID: ")
    except ValueError:
        print ("The entered value is not correct")

# Get the first three characters of the student’s first name. (If the first name is less than three characters in length, use the entire first name.) 

    if len(student_firstname) < 3:
        part1 = student_firstname[:3]
    else:
        part1 = student_firstname

# Get the first three characters of the student’s last name. (If the last name is less than three characters in length, use the entire last name.) 

    if len(student_lastname) < 3:
        part2 = student_lastname[:3]
    else:
        part2 = student_lastname

# Get the last three characters of the student’s ID number. (If the ID number is less than three characters in length, use the entire ID number.) 

    if len(student_id) < 3:
        part3 = student_id[:3]
    else:
        part3 = student_id

# Concatenate the three sets of characters to generate the login name. 

    login_name = part1 + part2 + part3
    print("The student login name is: {}".format(login_name))

# Request Password from User

    while len(login_name) > 1:

        login_password = input("Please create a new password: ")

# Validate the password if correct according to requirements
# The password must be at least seven characters long.
# It must contain at least one uppercase letter. 
# It must contain at least one lowercase letter.
# It must contain at least one numeric digit. 

        is_valid = False
        has_upper = False
        has_lower = False
        has_digit = False

        if len(login_password) >= 7:
            is_valid = True
    
        for character in login_password:
            if character.isupper():
                has_upper = True
            if character.islower():
                has_lower = True
            if character.isdigit():
                has_digit = True

#print the login_name and password and start over
        
        if is_valid and has_upper and has_lower and has_digit:
            print("You've successfully set a password")
            print("Your login name is: {}".format(login_name))
            print("Your login password is: {}".format(login_password))
            break

        if is_valid == False or has_upper == False or has_lower == False or has_digit == False:
            print("Password is not correct. Please try again!")

            
