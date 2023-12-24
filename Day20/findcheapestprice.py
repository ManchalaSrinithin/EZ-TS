class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp=[float('inf')]*n
        dp[src]=0
        for i in range(k+1):
            temp=dp.copy()
            for s,d,w in flights:
                if dp[s]!=float('inf') and dp[s]+w<temp[d]:
                    temp[d]=dp[s]+w
            dp=temp
        return -1 if dp[dst]==float('inf') else dp[dst]