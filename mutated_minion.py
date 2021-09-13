for _ in range(int(input())):
    a,b= input().split()
    l=list((map(int,input().split())))
    l1=[]
    for i in range(len(l)):
        l1.append(l[i]+int(b))
        for index in l1:
            if index%7==0:
                break
    
    print(index)
                