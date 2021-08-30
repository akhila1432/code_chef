lead1 =0
lead2 =0
w=0
p=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    lead1+=a
    lead2+=b
    if a>b:
      c=a-b
      w1=1
    else:
        b>a
        c=b-a
        w1=2
    if c>p:
        w=w1
        p=c
        
print(w,p)