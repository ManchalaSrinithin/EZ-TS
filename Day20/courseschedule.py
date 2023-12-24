class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d={i:[] for i in range(numCourses)}
        for i in prerequisites:
            d[i[0]].append(i[1])
        print(d)
        def dfs(source,vis):
            if source in vis:
                return False
            if d[source]==[]:
                return True
            vis.add(source)
            for i in d[source]:
                if not dfs(i,vis):
                    return False
            vis.remove(source)
            d[source]=[]
            return True
        for i in d:
            if dfs(i,set())==False:
                return False
        return True 
        