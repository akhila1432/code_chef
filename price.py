t = int(input())
for _ in range(t) :
    n = int(input())
    count = 0
    for i in [100,50,10,5,2,1] :
        while n>=i :
            n=n-i
            count += 1 
    print(count)