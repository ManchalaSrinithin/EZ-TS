class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return graph
        n=len(graph)
        vis=[]
        res=[] 
        def dfs(source,vis):
            if source==n-1:
                val=vis+[source]
                res.append(val)
            vis.append(source)
            for i in graph[source]:
                if i not in vis:
                    dfs(i,vis)
            vis.pop()
        dfs(0,vis)
        return res    