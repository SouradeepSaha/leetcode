class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        moves = [(-1,0), (0,-1), (1,0), (0,1)]
        dp = {}
        
        
        def dfs(row, col):
            temp = 1
            if (row, col) not in dp:
                for move in moves:
                    newrow, newcol = row+move[0], col+move[1]
                    if 0 <= newrow < rows and 0 <= newcol < cols and matrix[row][col] < matrix[newrow][newcol]:
                        temp = max(temp, 1+dfs(row+move[0], col+move[1]))
                dp[(row, col)] = temp
            return dp[(row, col)]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                x = dfs(i, j)
                res = max(res, x)
        
        return res
                
