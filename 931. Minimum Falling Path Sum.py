class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Use 1d dp array
        oldRow = [x for x in matrix[0]]

        for i in range(1, n):
            newRow = [0 for i in range(n)]
            for j in range(n):
                if j == 0:
                    newRow[j] = min(oldRow[j], oldRow[j+1]) + matrix[i][j]
                
                elif j == n-1:
                    newRow[j] = min(oldRow[j], oldRow[j-1]) + matrix[i][j]
                
                else:
                    newRow[j] = min(oldRow[j], oldRow[j+1], oldRow[j-1]) + matrix[i][j]

            
            oldRow = newRow
        
        return min(oldRow)

        # O(n) space, O(n^2) time
