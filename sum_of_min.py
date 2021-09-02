for _ in range(int(input())):
    n=int(input())
    a=map(int,input().split())
    l=[]
    b=list((a))
    for j in b:
        l.append(j)
        l.sort()
    for i in range(len(l)):
        print(l[0]+l[1])
        break
    