n1 = int(input("enter the lower_range value greater than 1: "))
n2 = int(input("enter the upper_range value: "))
for num in range(n1,n2+1):
      for i in range(2,num):
         if num%i == 0:
             break
      else:
        print(num)
