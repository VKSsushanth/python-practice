num = int(input("enter a number : "))
#order = len(num)
sum = 0
temp = num
while temp > 0:
  n = temp % 10
  sum = sum + n** 3
  temp = temp // 10
if num == sum:
  print(num,"is a armstrong number")
else:
  print(num,"is not a armstrong number")

