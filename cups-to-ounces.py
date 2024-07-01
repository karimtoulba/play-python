def main():
  f_temp = int(input("Please enter F: "))
  f_to_c(f_temp)

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print("C Temp is: ", c_temp)

main()