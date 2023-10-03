n=list(map(int,input().split()))
res=0
for i in range(len(n)):
    res=n[i]^(n[i]<<(i-1))
print(res)
