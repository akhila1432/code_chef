for _ in range(int(input())):
    a=input()
    l=list((a))
    s=set((a))
    l2=[]
    l3=[]
    for x in s:
      l2.append(l.count(x))
    max_count=max(l2)
    if max_count==len(a)-max_count:
        print('Yes')
    else:
        print('No')
      