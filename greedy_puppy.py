n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    k=[]
    for i in range(1,b+1):
        k.append(a%i)
    print(max(k))