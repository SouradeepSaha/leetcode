class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[row])):
                if obstacleGrid[row][col] == 1 and (row or col):
                    obstacleGrid[row][col] = 0
                
                elif (not row and col) or (not col and row):
                    obstacleGrid[row][col] = obstacleGrid[row][col-1] if col else obstacleGrid[row-1][col]
                    
                elif row and col:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
                    
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
    
