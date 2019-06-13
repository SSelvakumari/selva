a=int(input())
l=list(map(int,input().split()))
if len(l)==a:
  for i in range(a):
    print(l[i],i)
