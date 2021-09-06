def fruits(n,m,k):
     x = abs(n-m)
     y = x-k
     if y<0:
        print("0")
     else:
        print(y)
  
a=int(input())
for _ in range(a):
    n,m,k = map(int,input().split())   
    fruits(n,m,k)

            