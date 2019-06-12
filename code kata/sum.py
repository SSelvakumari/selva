n,m=map(int,input().split())
l=[]
a=0
l=map(int,input().split())
li=list(l)
if(len(li)==n):
  for i in range (len(li)):
    if(i<m):
      a=a+li[i]
  print(a)
