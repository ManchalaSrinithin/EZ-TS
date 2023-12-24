class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d={i:[] for i in range(numCourses)}
        for i in prerequisites:
            d[i[0]].append(i[1])
        print(d)
        res=[]
        cycle=set()
        def dfs(source,vis):
            if source in cycle:
                return True
            if source in vis:
                return False
            vis.add(source)
            for i in d[source]:
                if not dfs(i,vis):
                    return False
            vis.remove(source)
            cycle.add(source)
            res.append(source)
            return True
        for i in d:
            if dfs(i,set())==False:
                return []
        return res
        
        