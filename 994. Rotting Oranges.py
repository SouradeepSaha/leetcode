from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q1, q2, time = deque(), deque(), 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q1.appendleft((row,col))
        
        moves = [(-1, 0), (1,0), (0,1), (0, -1)]
        while len(q1):
            row, col = q1.pop()
            for r,c in moves:
                if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]) and grid[row+r][col+c] == 1:
                    q2.appendleft((row+r,col+c))
                    grid[row+r][col+c] = 2
                    
            if not len(q1) and len(q2):
                time += 1
                q1, q2 = q2, deque()
                
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        
        return time
