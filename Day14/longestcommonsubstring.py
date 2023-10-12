def longestcommonsubstring(text1,text2):
    res=[]
    for i in range(len(text1)):
        for j in range(i+1,len(text1)):
            res.append(text1[i:j+1])
        res2=[]
    for i in range(len(text2)):
        for j in range(i+1,len(text2)):
            res2.append(text2[i:j+1])
    print(res)
    print(res2)
    res3=[]
    max=0
    for i in res:
        for j in res2:
            if i==j:
                res3.append(i)
                p=len(i)
                if p>max:
                    max=p
                    r=i
    print(max)
    return r
s=input()
s1=input()
print(longestcommonsubstring(s,s1))