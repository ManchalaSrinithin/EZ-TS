def maxarray(l,start,end):
    if start==end:
        return l[start]
    mid=(start+end)//2
    left=maxarray(l,start,mid)
    right=maxarray(l,mid+1,end)
    return left if left>right else right    
l=list(map(int,input().split()))
start=0
end=len(l)-1
print(maxarray(l,start,end))