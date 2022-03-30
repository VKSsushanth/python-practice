n = int(input("enter a number that u want to print a table : "))
for i in range(1,13):
  p = int(n * i)
  print("{0} * {1} = {2}".format(n,i,p))