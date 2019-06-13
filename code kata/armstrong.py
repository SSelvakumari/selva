n = int(input())
s = 0
flag = n
while flag > 0:
   digit = flag % 10
   s += digit ** 3
   flag //= 10
if n == s:
   print("yes")
else:
   print("no")
