def sqrt(n):
    start=0
    end=n+1
    while start<end:
        mid=start+(end-start)//2
        if mid*mid>n:
            end=mid
        else:
            start=mid+1
    return start-1
n=int(input())
print(sqrt(n))


            