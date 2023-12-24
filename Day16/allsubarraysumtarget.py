n=int(input())
l=list(map(int,input().split()))
i=0
j=0
res=l[0]
while j<len(l):
    if res==n:
        print(i,j,res)
        break
    elif res<n:
        res+=l[j]
        j+=1
    else:
        res-=l[i]
        i+=1
        
        
        