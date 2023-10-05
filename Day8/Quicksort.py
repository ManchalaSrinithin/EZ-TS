def qsorting(l,start,end):
            pi=l[end]
            i=start-1
            for j in range(start,end):
                if l[j]<pi:
                    i+=1
                    l[j],[i]=l[i],l[j]
            l[i+1],l[end]=l[end],l[i+1]
            return i+1
def Quicksort(l,start,end):
    if start<end:
        pi=qsorting(l,start,end)
        Quicksort(l,start,pi-1)
        Quicksort(l,pi+1,end)
l=list(map(int,input().split()))
start=0
end=len(l)-1
Quicksort(l,start,end)
print(l)