class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0])
        
        while left <= right:
            mid = left + (right-left)//2
            
            row, col = divmod(mid, len(matrix[0]))
            if row < 0 or col < 0 or row > len(matrix)-1 or col > len(matrix[0])-1:
                return False
            if matrix[row][col] == target:
                return True
            if target > matrix[row][col]:
                left = mid+1
            else:
                right = mid-1
        
        return False
            
