def isPowerOfTwo (n): 
   return (n and (not(n & (n - 1))) ) 
n=int(input())
if(isPowerOfTwo(n)): 
    print('yes') 
else: 
    print('no') 
