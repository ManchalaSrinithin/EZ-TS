def bellmanford(map1,n):
    dp=[float('inf')]*n
    for i in range(n+1):
        temp=dp.copy()
        i=0
        for s,d,w in map1[i]:
            if dp[s]!=float('inf') and dp[s]+w<temp[d]:
                temp[d]=dp[s]+w
            i+=1
            dp=temp
    return -1 if dp[d]==float('inf') else dp[d] 
k=int(input())
n=int(input())
map1={}
for i in range(k):
    u,v,w=map(int,input().split())
    if u not in map1:
        map1[u]=[]
    map1[u].append((u,v,w))
print(bellmanford(map1,n))