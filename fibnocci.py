n = int(input("enter the number of terms you want to find the series : "))
n1 = 0 
n2 = 1
print("the fibnocci series for the following is : ")
print(n1)
print(n2)
temp = 0
if n <= 0:
  print("ERROR!")
elif n == 1:
  print(n1)
else : 
 # print("the fibnocci series for the following is : ")
  for i in range (0,n+1):
  
    temp = n1 + n2
    print(temp)
    n1 = n2
    n2 = temp
  