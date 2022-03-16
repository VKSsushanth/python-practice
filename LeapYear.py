a = int(input("enter a year of your chioice : "))

if (a % 400 == 0) and (a % 100 ==0):
  print("the following year {0} is a leap year".format(a))

elif (a % 400 == 0) and (a % 100 != 0 ):
  print("the following year is not a leap year".format(a))

else:
  print("it is not a leap year")