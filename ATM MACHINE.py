for _ in range(int(input())):
    a,b=map(int,input().split())
    c =list(map(int,input().split()))
    for x in c:
          if x<=b:
              b=b-x
              print(1,end='')
          else:
              print(0,end='')
    print()
            