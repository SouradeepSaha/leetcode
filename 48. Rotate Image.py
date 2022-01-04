# Algorithm: Rotate gropus of 4 cells
# on each loop, process and remove the outer layer
# visualize using 2x2 and 3x3 matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        
        while left < right:
            top, bottom = left, right
            for i in range(right-left):
                
                # Store the topleft element
                topleft = matrix[top][left+i]
                
                # Replace topleft with bottomleft
                matrix[top][left+i] = matrix[bottom-i][left]
                
                # Replace bottomleft with bottomright
                matrix[bottom-i][left] = matrix[bottom][right-i]
                
                # replace bottomleft with topright
                matrix[bottom][right-i] = matrix[top+i][right]
                
                # Replace topright with topleft
                matrix[top+i][right] = topleft
            
            left, right = left+1, right-1
