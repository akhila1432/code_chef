s1="a?a"
s2="??a"
x2=s2.replace("??","ab")
x1=s1.replace("?","b")
print(x1)
print(x2)
for i in range(len(x2)):
    x2[0]=x2[1]
    print(x2)