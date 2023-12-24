class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        print(d)
        vis=set()
        def dfs(source,vis):
            vis.add(source)
            if source==destination:
                return True
            for i in d[source]:
                if i not in vis:
                    if dfs(i,vis):
                        return True
            return False
        return dfs(source,vis)



        