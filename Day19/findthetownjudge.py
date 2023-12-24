class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map={i:[] for i in range(1,n+1)}
        for i,j in trust:
            map[i].append(j)
        for i in range(1,n+1):
            if len(map[i])==0:
                cand=i
                for others in range(1,n+1):
                    if others!=cand and cand not in map[others]:
                        return -1
                return cand
        return -1
        