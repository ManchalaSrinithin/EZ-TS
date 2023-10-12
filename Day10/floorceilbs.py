def floorin(l,target,start,end,floor):
    if start<=end:
        mid=start+(end-start)//2
        if l[mid]==target:
            return mid
        elif l[mid]<target:
            floor=mid
            floorin(l,target,mid+1,end,floor)
        else:
            floorin(l,target,start,mid-1,floor)
    return floor
def ceilin(l,target,start,end,ceil):
    if start<=end:
        mid=start+(end-start)//2
        if l[mid]==target:
            return mid
        elif l[mid]<target:
            floorin(l,target,mid+1,end,ceil)
        else:
            ceil=mid
            floorin(l,target,start,mid-1,ceil)
    return ceil
l=list(map(int,input().split()))
target=int(input())
start=0
end=len(l)
floor=-1
ceil=float('inf')
print(floorin(l,target,start,end,floor))
start=0
end=len(l)
print(ceilin(l,target,start,end,ceil))
        