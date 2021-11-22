class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, ind):
            if ind >= len(word):
                return True
            if r > 0 and board[r-1][c] == word[ind]:
                board[r-1][c], temp = None, board[r-1][c]
                if dfs(r-1, c, ind+1):
                    return True
                board[r-1][c] = temp
            
            if c > 0 and board[r][c-1] == word[ind]:
                board[r][c-1], temp = None, board[r][c-1]
                if dfs(r, c-1, ind+1):
                    return True
                board[r][c-1] = temp
            
            if r < len(board)-1 and board[r+1][c] == word[ind]:
                board[r+1][c], temp = None, board[r+1][c]
                if dfs(r+1, c, ind+1):
                    return True
                board[r+1][c] = temp
            
            if c < len(board[0])-1 and board[r][c+1] == word[ind]:
                board[r][c+1], temp = None, board[r][c+1]
                if dfs(r, c+1, ind+1):
                    return True
                board[r][c+1] = temp
            
            return False
        
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    board[row][col], temp = None, word[0]
                    if dfs(row, col, 1):
                        return True
                    board[row][col] = temp
        
        return False
