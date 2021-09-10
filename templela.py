t= 1
while t>0:
    n=5
    l = [1,2,3,2,1]
    m = n//2 + 1
    #the left index 0 should be 1 and the as the indexes the values need to increase by 1
    if l[0]==l[n-1] and n%2!=0 and l[n//2]==m:
        print("yes")
    else:
        print("no")
    t=t-1
    
    