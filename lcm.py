a=120
b=140
# factors of a are 2,3,5,
if a>b:
    max = a
else:
    max = b
while(True):
    if(max%a == 0) and (max%b == 0):
        print(max)
        break 