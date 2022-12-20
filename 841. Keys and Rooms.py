class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0 for i in range(n)]

        def dfs(start):
            visited[start] = 1
            for v in rooms[start]:
                if not visited[v]:
                    dfs(v)
        
        dfs(0)
        return all(visited)
