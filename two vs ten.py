try:
 t = int(input())
 for _ in range(t):
    n=int(input())
    if n%10==0:
        print("0")
    else:
        n%10!=0
        n=n*2
        if n%10==0:
            print("1")
        else:
            print("-1")
except:
    pass
            