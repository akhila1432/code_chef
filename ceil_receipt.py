arr = [1,2,3,4,5]
t = int(input())
for _ in range(t) :
    p = int(input())
    items = 0
    for i in [2048,1024,512,256,128,64,32,16,8,4,2,1] :
        while p>=i :
            p=p-i
            items += 1 
    print(items)
        
        