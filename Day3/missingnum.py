n=list(map(int,input().split()))
res=0
k=0
for i in range(0,len(n)):
    res=res^i
for i in range(0,len(n)-1):
    res=res^n[i]
print(res)