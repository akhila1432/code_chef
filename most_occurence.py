n = 123222
N = str(n)
list1 = list((N))
set1 = set((list1))
list2 = list((set1))
list3= []
for x in list2:
        if x == "4":
         list3.append(list1.count(x))
         print(list3) 