class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        q=[source]
        vis=set()
        vis.add(set)
        while q:
            a=q.pop(0)
            for i in d[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False



        