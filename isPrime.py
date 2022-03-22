a = int(input("enter a number of your choice : "))

flag = False

if (a>1):
  for i in range(2,a):

    if (a%i==0):
      flag = True
      break

if flag:
  print(a , " is a composite number")
else:
  print(a , " is a prime number")






















































  