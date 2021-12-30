class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(r, c):
            q = collections.deque()
            board[r][c] = 'Y'
            q.append((r,c))
            
            while len(q):
                row, col = q.popleft()
                for i, j in moves:
                    if 0 <= row+i < m and 0 <= col+j < n and board[row+i][col+j] == 'O':
                        board[row+i][col+j] = "Y"
                        q.append((row+i, col+j))
                
        for row in range(m):
            for col in range(n):
                if row == 0 or row == m-1 or col == 0 or col == n-1:
                    if board[row][col] == 'O':
                        bfs(row, col)
                    
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'Y':
                    board[row][col] = 'O'
                
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                
        
