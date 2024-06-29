############################
## Code: Forming a triangle
## Author: Karim Toulba
## Date: 28/06/2024
############################

try: 

    a = float(input ("Please enter line a length: "))
    b = float(input ("Please enter line b length: "))
    c = float(input ("Please enter line c length: "))

    if a < 0:
        print (a, "is not positive float! Please re-enter A")
    elif b < 0:
        print (b, "is not positive float! Please re-enter B")
    elif c < 0: 
        print (c, "is not positive float! Please re-enter C")

except ValueError:
    print ("Values are not correct!")

#cannot form a triangle

longest = a
line1 = b
line2 = c

if a > b and a > c:
    print ("Longest is ", longest)

elif b > a and b > c:
    longest = b
    line1 = a
    line2 = c
    print ("Longest is ", longest)

elif c > a and c > b:
    longest = c
    line1 = a
    line2 = b
    print ("Longest is ", longest)

#triangle is right/acut/obtuse

if longest >= (line1 + line2):
    print("The segments cannot form a triangle")

elif (longest**2) == ((line1**2) + (line2**2)):
    print("The triangle is right")

elif (longest**2) < ((line1**2) + (line2**2)):
    print("The triangle is acute")

elif (longest**2) > ((line1**2) + (line2**2)):
    print("The triangle is obtuse")



