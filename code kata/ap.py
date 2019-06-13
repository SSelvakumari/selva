def sumOfAP(a,d,n):
  tot=(n/2)*(2*a+(n-1)*d)
  return int(tot)
n,a,d=map(int,input().split())
print(sumOfAP(a,d,n))
