from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q1, q2 = deque(), deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q1.appendleft((row,col))
        
        time = 0
        while len(q1):
            
            row, col = q1.pop()
            if row > 0 and grid[row-1][col] == 1:
                q2.appendleft((row-1,col))
                grid[row-1][col] = 2
            
            if col > 0 and grid[row][col-1] == 1:
                q2.appendleft((row, col-1))
                grid[row][col-1] = 2
            
            if row < len(grid)-1 and grid[row+1][col] == 1:
                q2.appendleft((row+1, col))
                grid[row+1][col] = 2
            
            if col < len(grid[0])-1 and grid[row][col+1] == 1:
                q2.appendleft((row, col+1))
                grid[row][col+1] = 2
            
            if not len(q1) and len(q2):
                print(q2)
                time += 1
                q1, q2 = q2, deque()
                
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        
        return time
