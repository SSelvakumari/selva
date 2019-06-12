num=int(input())
x=num
temp=0
while x!=0:
  temp=(temp*10)+(x%10)
  x=x//10
if(num==temp):
  print("yes")
else:
  print("no")
