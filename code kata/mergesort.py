n=int(input())
val=map(int,list(input().split()))
s=sorted(val)
for x in range(0,len(s)):
  print(s[x], end=' ')
