def isvalid(n,k,l,mid):
    prev=l[0]
    c=1
    for i in l:
        if i-(prev)>=mid:
            c+=1
            prev=i
    return True if k==c else False
def aggressivecows(n,k,l): 
    l.sort()
    low=0
    high=l[-1]-l[0]
    res=0
    while high>=low:
        mid=(high+low)//2
        if isvalid(n,k,l,mid):
            res=mid
            low=low+1
        else:
            high-=1
    return res
n=int(input())#number of aggressive cows
k=int(input())# number of stalls
l=list(map(int,input().split()))
print(aggressivecows(n,k,l))
        