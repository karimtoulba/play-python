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
        student_lastname = str(input("Please enter student firt name: "))
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