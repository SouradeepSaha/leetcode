# Time complexity: O(m+n)
# Space reduction: elimiate one row/col in each iteration
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        
        return False
            
