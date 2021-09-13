N=3
i=1
res=0
while(N>0):
    N-=i
    i+=1
    if N<0:
     break
    else:
        res+=1
print(res)