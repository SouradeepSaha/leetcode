class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp, maxlen = {}, 0
        
        def recurse(row, col):
            nonlocal maxlen
            if row >= len(matrix) or col >= len(matrix[0]):
                return 0
                
            if (row, col) not in dp:
                down = recurse(row+1, col)
                right = recurse(row, col+1)
                diag = recurse(row+1,col+1)
                
                dp[(row,col)] = 0 if matrix[row][col] == "0" else min(down, right, diag) + 1
                maxlen = max(maxlen, dp[(row,col)])
            
            return dp[(row,col)]
            
        
        recurse(0,0)
        return maxlen ** 2
