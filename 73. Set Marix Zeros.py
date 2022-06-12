class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero = False
        
        
        def setRowZero(row):
            for i in range(cols):
                matrix[row][i] = 0
        
        def setColZero(col):
            for i in range(rows):
                matrix[i][col] = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0    
                    if j == 0:
                        first_col_zero = True
                    else:
                        matrix[0][j] = 0
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                setRowZero(i)
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                setColZero(j)
        
        if matrix[0][0] == 0:
            setRowZero(0)
        if first_col_zero:
            setColZero(0)
            
