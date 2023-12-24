class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for key in rooms[i]:
                dfs(key)
        dfs(0)
        return len(visited)==len(rooms)        