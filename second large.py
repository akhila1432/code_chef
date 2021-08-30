T = int(input())
for i in range (T):
    l = []
    a=map(int,input().split())
    for x in a:
        l.append(x)
        l.sort()
    print(l[1])