N = int(input())
num1 = 0
num2 = 1
for Num in range(1, N+1):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = num1+ num2
                      num1 = num2
                      num2 = Next
           print(Next,end=" ")
