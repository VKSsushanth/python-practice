import math
a = float(input("enter the value of a : "))
b = float(input("enter the value of b : "))
c = float(input("enter the value of c : "))

sol_1 = float((-b + math.sqrt(b*b - 4*a*c) )/ (2*a))

sol_2 = float((-b - math.sqrt(b*b - 4*a*c)) / (2*a))

if (b*b - 4*a*c > 0 or b*b - 4*a*c == 0 ):
  print("the roots are {0} and {1} ".format(sol_1,sol_2))
else:
  print("imaginary roots")