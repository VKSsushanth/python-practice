n = int(input())

if (n<0):
    print ("please enter a valid number")
elif(n==0):
    print("1")
else:
  for i in range (1,n):
    n = n * i
    b = int(n)
  print(b)