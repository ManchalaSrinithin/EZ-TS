def sumofarray(l,start,end,sum1=0):
    if start==end:
        return l[start]
    mid=(start+end)//2
    left=sumofarray(l,start,mid)
    right=sumofarray(l,mid+1,end)
    return left+right    
l=list(map(int,input().split()))
start=0
end=len(l)-1
print(sumofarray(l,start,end))