class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oc = image[sr][sc]
        visited = [[False for _ in image[i]] for i in range(len(image))]

        def dfs(row, col):
            if not (0 <= row < m) or not (0 <= col < n) or visited[row][col]:
                return
            
            if image[row][col] == oc:
                visited[row][col] = True
                image[row][col] = newColor
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
        
        dfs(sr, sc)
        return image
        
