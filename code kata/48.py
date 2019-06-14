x=int(input())
l=list(map(int,input().split()))
if(x==len(l)):
  s=sum(l)
  y=s//x
print(y)
