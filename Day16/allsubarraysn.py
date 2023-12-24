n=int(input())
l=list(map(int,input().split()))
i=0
j=0
res=0
p=[]
while j<=len(l):
    if res==n:
        p.append(l[i:j])
        res-=l[i]
        i+=1
    elif res<n:
        if j<len(l):
            res+=l[j]
            j+=1
        else:
            break
    else:
        res-=l[i]
        i+=1
print(p)
        