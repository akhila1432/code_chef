for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
       a=int(input())
       l.append(a)
    for x in l:
        if l.count(x)%2==1:
            print(x)
            break