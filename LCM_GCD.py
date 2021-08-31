def lcm(a,b):
         if a>b:
            max=a
         else:
            max=b
         while(True):
            if (max%a == 0 and max%b == 0):
                maxi = max 
                break
            max=max+1
 return maxi

def gcd(a,b):
    
         i=1
         while(i<=a and i<=b):
             gcde=i
         i=i+1
    return gcde
    

t=int(input())
for i in range(t):
    while t>0:
        d,n=map(int,input().split())
t=int(input())
for i in range(t):
    while t>0:
        d,n=map(int,input().split())
maxi = lcm(a,b)
gcde = gcd(a,b) 
print(maxi)
print(gcde)