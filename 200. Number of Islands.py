from collections import deque
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while len(q):
                row, col = q.popleft()
                if (row, col) not in visited:
                    visited.add((row, col))
                    for i, j in moves:
                        newRow, newCol = row+i, col+j
                        if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1":
                            q.append((newRow, newCol))
            
        output = 0 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    output += 1
        
        return output
