n=int(input())
k=int(input())
n=n&(1<<(k-1))
if n:
    print("set")
else:
    print("Not set")