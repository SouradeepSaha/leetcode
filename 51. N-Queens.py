from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        
        res = []
        board = [['.' for col in range(n)] for row in range(n)]
        
        def backtrack(row):
            if row >= n:
                res.append(["".join(x) for x in board])
                print(board)
                return
            
            for col in range(n):
                if col not in cols and row+col not in posDiag and row-col not in negDiag:
                    board[row][col] = 'Q'
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)

                    backtrack(row+1)

                    board[row][col] = '.'
                    cols.remove(col)
                    posDiag.remove(row+col)
                    negDiag.remove(row-col)
        
        backtrack(0)
        return res
            
            
                
                
