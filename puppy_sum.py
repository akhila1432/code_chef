t=int(input())
for i in range(t):
    while t>0:
        d,n=map(int,input().split())
        
        def sum(d,n):
            if d==0:
                return n
            count=(n*(n+1))//2
            n=count
            d-=1
            return sum(d,count)
        print(sum(d,n))
        t-=1