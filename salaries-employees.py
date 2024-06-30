##############################################
### Code: Calculating Employees Salary      ##
### Author: Karim Toulba                    ##
### Date: 29/06/2024                        ##
##############################################

weight = int(input("Enter Shipment Weight: "))
ground_shipping = 0

#Ground Shipping
if weight <= 2:
  ground_shipping = 20 + (1.5*weight)
  print ("Ground Shipping Rate is: $", ground_shipping)
elif 2 < weight >= 6:
  ground_shipping = 20 + (3*weight)
  print ("Ground Shipping Rate is: $", ground_shipping)
elif 6 < weight >= 10:
  ground_shipping = 20 + (4*weight)
  print ("Ground Shipping Rate is: $", ground_shipping)
else: 
  ground_shipping = 20 + (4.75*weight)
  print ("Ground Shipping Rate is: $", ground_shipping)