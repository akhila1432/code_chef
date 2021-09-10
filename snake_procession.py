try:
    t=int(input())
    while t > 0:
        n=int(input())
        s=input()
        s=s.replace('.','')
        s=s.replace('HT','')
        if(len(s)==0):
           print('Valid')
        else:
           print('Invalid')
        
        t-1
except:
    pass