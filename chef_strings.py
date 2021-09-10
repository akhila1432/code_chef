for _ in range(1):
        s1 = "?abac"
        s2 = "aba?w"
        count=0
        diff=0
        for i in range(len(s1)):
            if s1[i]=='?' or s2[i]=='?':
                count+=1
            elif s1[i]!=s2[i]:
                diff+=1
        print(diff,diff+count)