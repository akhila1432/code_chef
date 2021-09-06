n,k = 6,4
l=[6,5,4,3,2,1]
l.sort(reverse=True)
m=k-1
count=0
for i in l:
    if i>=m:
        count+=1
    else:
        break
print(count)

