for _ in range(int(input())):
    a=list(map(float,input().split()))
    for i in range(len(a)):
        if a[0]>50 and a[1]<0.7 and a[2]>5600:
             print("10")
             break
        elif a[0]>50 and a[1]<0.7 and a[2]<5600:
             print("9")
             break
        elif a[0]<50 and a[1]<0.7 and a[2]>5600:
             print("8")
             break
        elif a[0]>50 and a[1]>0.7 and a[2]>5600:
             print("7")
             break
        elif a[0]>50 or a[1]<0.7 or a[2]>5600:
             print("6")
             break
        else:
             print("5")
             break