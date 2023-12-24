def dfs(start, vis, map1):
    vis.add(start)
    for i in map1[start]:
        if i not in vis:
            dfs(i, vis, map1)

n = int(input())
map1 = {i: [] for i in range(n)}

for _ in range(n):
    u, v = map(int, input().split())
    map1[u].append(v)
    map1[v].append(u)

vis = set()
start = int(input("Enter the starting node: "))
dfs(start, vis, map1)
print("Nodes visited in DFS:", vis)
