def subset(l,n,len1):
    if n==0:
        return True
    if len1==0:
        return False
    if l[len1-1]>n:
        return subset(l,n,len1-1)
    else:
        return subset(l,n-l[len-1],len-1) or subset(l,n.len-1)
    
l=list(map(int,input().split(',')))
n=int(input())
len1=len(l)
print(subset(l,n,len1))